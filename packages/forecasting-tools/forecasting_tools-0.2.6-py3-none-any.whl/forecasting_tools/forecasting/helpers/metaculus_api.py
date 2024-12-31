from __future__ import annotations

import json
import logging
import os
import random
import re
from datetime import datetime, timedelta
from typing import Any, Sequence, TypeVar

import requests
import typeguard

from forecasting_tools.forecasting.questions_and_reports.questions import (
    BinaryQuestion,
    DateQuestion,
    MetaculusQuestion,
    MultipleChoiceQuestion,
    NumericQuestion,
)
from forecasting_tools.util.misc import raise_for_status_with_additional_info

logger = logging.getLogger(__name__)

Q = TypeVar("Q", bound=MetaculusQuestion)


class MetaculusApi:
    """
    Documentation for the API can be found at https://www.metaculus.com/api/
    """

    AI_WARMUP_TOURNAMENT_ID = (
        3294  # https://www.metaculus.com/tournament/ai-benchmarking-warmup/
    )
    AI_COMPETITION_ID_Q3 = 3349  # https://www.metaculus.com/tournament/aibq3/
    AI_COMPETITION_ID_Q4 = 32506  # https://www.metaculus.com/tournament/aibq4/
    Q3_2024_QUARTERLY_CUP = 3366
    Q4_2024_QUARTERLY_CUP = 3672
    CURRENT_QUARTERLY_CUP_ID = Q4_2024_QUARTERLY_CUP

    API_BASE_URL = "https://www.metaculus.com/api"
    OLD_API_BASE_URL = "https://www.metaculus.com/api2"
    MAX_QUESTIONS_FROM_QUESTION_API_PER_REQUEST = 100

    @classmethod
    def post_question_comment(cls, post_id: int, comment_text: str) -> None:
        response = requests.post(
            f"{cls.API_BASE_URL}/comments/create/",
            json={
                "on_post": post_id,
                "text": comment_text,
                "is_private": True,
                "included_forecast": True,
            },
            **cls.__get_auth_headers(),  # type: ignore
        )
        logger.info(f"Posted comment on post {post_id}")
        raise_for_status_with_additional_info(response)

    @classmethod
    def post_binary_question_prediction(
        cls, question_id: int, prediction_in_decimal: float
    ) -> None:
        logger.info(f"Posting prediction on question {question_id}")
        if prediction_in_decimal < 0.01 or prediction_in_decimal > 0.99:
            raise ValueError("Prediction value must be between 0.001 and 0.99")
        payload = {
            "probability_yes": prediction_in_decimal,
        }
        cls._post_question_prediction(question_id, payload)

    @classmethod
    def post_numeric_question_prediction(
        cls, question_id: int, cdf_values: list[float]
    ) -> None:
        """
        If the question is numeric, forecast must be a dictionary that maps
        quartiles or percentiles to datetimes, or a 201 value cdf.
        In this case we use the cdf.
        """
        logger.info(f"Posting prediction on question {question_id}")
        if len(cdf_values) != 201:
            raise ValueError("CDF must contain exactly 201 values")
        if not all(0 <= x <= 1 for x in cdf_values):
            raise ValueError("All CDF values must be between 0 and 1")
        if not all(a <= b for a, b in zip(cdf_values, cdf_values[1:])):
            raise ValueError("CDF values must be monotonically increasing")
        payload = {
            "continuous_cdf": cdf_values,
        }
        cls._post_question_prediction(question_id, payload)

    @classmethod
    def post_multiple_choice_question_prediction(
        cls, question_id: int, options_with_probabilities: dict[str, float]
    ) -> None:
        """
        If the question is multiple choice, forecast must be a dictionary that
        maps question.options labels to floats.
        """
        payload = {
            "probability_yes_per_category": options_with_probabilities,
        }
        cls._post_question_prediction(question_id, payload)

    @classmethod
    def _post_question_prediction(
        cls, question_id: int, forecast_payload: dict
    ) -> None:
        url = f"{cls.API_BASE_URL}/questions/forecast/"
        response = requests.post(
            url,
            json=[
                {
                    "question": question_id,
                    **forecast_payload,
                },
            ],
            **cls.__get_auth_headers(),  # type: ignore
        )
        logger.info(f"Posted prediction on question {question_id}")
        raise_for_status_with_additional_info(response)

    @classmethod
    def get_question_by_url(cls, question_url: str) -> MetaculusQuestion:
        """
        URL looks like https://www.metaculus.com/questions/28841/will-eric-adams-be-the-nyc-mayor-on-january-1-2025/
        """
        match = re.search(r"/questions/(\d+)", question_url)
        if not match:
            raise ValueError(
                f"Could not find question ID in URL: {question_url}"
            )
        question_id = int(match.group(1))
        return cls.get_question_by_post_id(question_id)

    @classmethod
    def get_question_by_post_id(cls, post_id: int) -> MetaculusQuestion:
        logger.info(f"Retrieving question details for question {post_id}")
        url = f"{cls.API_BASE_URL}/posts/{post_id}/"
        response = requests.get(
            url,
            **cls.__get_auth_headers(),  # type: ignore
        )
        raise_for_status_with_additional_info(response)
        json_question = json.loads(response.content)
        metaculus_question = MetaculusApi.__metaculus_api_json_to_question(
            json_question
        )
        logger.info(f"Retrieved question details for question {post_id}")
        return metaculus_question

    @classmethod
    def get_all_open_questions_from_tournament(
        cls,
        tournament_id: int,
    ) -> list[MetaculusQuestion]:
        logger.info(f"Retrieving questions from tournament {tournament_id}")
        url_qparams = {
            "tournaments": [tournament_id],
            "with_cp": "true",
            "order_by": "-hotness",
            "statuses": "open",
        }

        metaculus_questions = cls.__get_questions_from_api(url_qparams)
        logger.info(
            f"Retrieved {len(metaculus_questions)} questions from tournament {tournament_id}"
        )
        return metaculus_questions

    @classmethod
    def get_benchmark_questions(
        cls, num_of_questions_to_return: int, random_seed: int | None = None
    ) -> list[BinaryQuestion]:
        cls.__validate_requested_benchmark_question_count(
            num_of_questions_to_return
        )
        questions = cls.__fetch_all_possible_benchmark_questions()
        filtered_questions = cls.__filter_retrieved_benchmark_questions(
            questions, num_of_questions_to_return
        )
        questions = cls.__get_random_sample_of_questions(
            filtered_questions, num_of_questions_to_return, random_seed
        )
        for question in questions:
            try:
                assert not question.api_json["question"]["include_bots_in_aggregates"]  # type: ignore
            except KeyError:
                pass
        return questions

    @classmethod
    def __get_auth_headers(cls) -> dict[str, dict[str, str]]:
        METACULUS_TOKEN = os.getenv("METACULUS_TOKEN")
        if METACULUS_TOKEN is None:
            raise ValueError("METACULUS_TOKEN environment variable not set")
        return {"headers": {"Authorization": f"Token {METACULUS_TOKEN}"}}

    @classmethod
    def __validate_requested_benchmark_question_count(
        cls, num_of_questions_to_return: int
    ) -> None:
        est_num_matching_filter = (
            130  # As of Nov 5, there were only 130 questions matching filters
        )
        assert (
            num_of_questions_to_return <= est_num_matching_filter
        ), "There are not enough questions matching the filter"
        if num_of_questions_to_return > est_num_matching_filter * 0.5:
            logger.warning(
                f"There are estimated to only be {est_num_matching_filter} questions matching all the filters. You are requesting {num_of_questions_to_return} questions."
            )

    @classmethod
    def __fetch_all_possible_benchmark_questions(cls) -> list[BinaryQuestion]:
        questions: list[BinaryQuestion] = []
        iterations_to_get_past_estimate = 3

        for i in range(iterations_to_get_past_estimate):
            limit = cls.MAX_QUESTIONS_FROM_QUESTION_API_PER_REQUEST
            offset = i * limit
            new_questions = (
                cls.__get_general_open_binary_questions_resolving_in_3_months(
                    limit, offset
                )
            )
            questions.extend(new_questions)

        logger.info(
            f"There are {len(questions)} questions matching filter after iterating through {iterations_to_get_past_estimate} pages of {cls.MAX_QUESTIONS_FROM_QUESTION_API_PER_REQUEST} questions that matched the filter"
        )
        return questions

    @classmethod
    def __filter_retrieved_benchmark_questions(
        cls, questions: list[BinaryQuestion], num_of_questions_to_return: int
    ) -> list[BinaryQuestion]:
        qs_with_enough_forecasters = cls.__filter_questions_by_forecasters(
            questions, min_forecasters=40
        )
        filtered_questions = [
            question
            for question in qs_with_enough_forecasters
            if question.community_prediction_at_access_time is not None
        ]

        logger.info(
            f"Reduced to {len(filtered_questions)} questions with enough forecasters"
        )

        if len(filtered_questions) < num_of_questions_to_return:
            raise ValueError(
                f"Not enough questions available ({len(filtered_questions)}) "
                f"to sample requested number ({num_of_questions_to_return})"
            )
        return filtered_questions

    @classmethod
    def __get_random_sample_of_questions(
        cls,
        questions: list[BinaryQuestion],
        sample_size: int,
        random_seed: int | None,
    ) -> list[BinaryQuestion]:
        if random_seed is not None:
            previous_state = random.getstate()
            random.seed(random_seed)
            random_sample = random.sample(questions, sample_size)
            random.setstate(previous_state)
        else:
            random_sample = random.sample(questions, sample_size)
        return random_sample

    @classmethod
    def __get_general_open_binary_questions_resolving_in_3_months(
        cls, number_of_questions: int, offset: int = 0
    ) -> Sequence[BinaryQuestion]:
        three_months_from_now = datetime.now() + timedelta(days=90)
        params = {
            "type": "forecast",
            "forecast_type": "binary",
            "status": "open",
            "number_of_forecasters__gte": 40,
            "scheduled_resolve_time__lt": three_months_from_now,
            "order_by": "publish_time",
            "offset": offset,
            "limit": number_of_questions,
        }
        questions = cls.__get_questions_from_api(params, use_old_api=True)
        checked_questions = typeguard.check_type(
            questions, list[BinaryQuestion]
        )
        return checked_questions

    @classmethod
    def __get_questions_from_api(
        cls, params: dict[str, Any], use_old_api: bool = False
    ) -> list[MetaculusQuestion]:
        num_requested = params.get("limit")
        assert (
            num_requested is None
            or num_requested <= cls.MAX_QUESTIONS_FROM_QUESTION_API_PER_REQUEST
        ), "You cannot get more than 100 questions at a time"
        if use_old_api:
            url = f"{cls.OLD_API_BASE_URL}/questions/"
        else:
            url = f"{cls.API_BASE_URL}/posts/"
        response = requests.get(url, params=params, **cls.__get_auth_headers())  # type: ignore
        raise_for_status_with_additional_info(response)
        data = json.loads(response.content)
        results = data["results"]
        supported_posts = [
            q
            for q in results
            if "notebook" not in q
            and "group_of_questions" not in q
            and "conditional" not in q
        ]
        removed_posts = [
            post for post in results if post not in supported_posts
        ]
        if len(removed_posts) > 0:
            logger.warning(
                f"Removed {len(removed_posts)} posts that "
                "are not supported (e.g. notebook or group question)"
            )

        questions = [
            cls.__metaculus_api_json_to_question(q) for q in supported_posts
        ]
        return questions

    @classmethod
    def __metaculus_api_json_to_question(
        cls, api_json: dict
    ) -> MetaculusQuestion:
        assert (
            "question" in api_json
        ), f"Question not found in API JSON: {api_json}"
        question_type_string = api_json["question"]["type"]  # type: ignore
        if question_type_string == BinaryQuestion.get_api_type_name():
            question_type = BinaryQuestion
        elif question_type_string == NumericQuestion.get_api_type_name():
            question_type = NumericQuestion
        elif (
            question_type_string == MultipleChoiceQuestion.get_api_type_name()
        ):
            question_type = MultipleChoiceQuestion
        elif question_type_string == DateQuestion.get_api_type_name():
            question_type = DateQuestion
        else:
            raise ValueError(f"Unknown question type: {question_type_string}")
        question = question_type.from_metaculus_api_json(api_json)
        return question

    @classmethod
    def __filter_questions_by_forecasters(
        cls, questions: list[Q], min_forecasters: int
    ) -> list[Q]:
        questions_with_enough_forecasters: list[Q] = []
        for question in questions:
            assert question.num_forecasters is not None
            if question.num_forecasters >= min_forecasters:
                questions_with_enough_forecasters.append(question)
        return questions_with_enough_forecasters
