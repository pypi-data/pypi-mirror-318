from __future__ import annotations

import logging
import textwrap
from datetime import datetime
from enum import Enum

from pydantic import AliasChoices, BaseModel, Field

from forecasting_tools.util.jsonable import Jsonable

logger = logging.getLogger(__name__)


class QuestionState(Enum):
    OPEN = "open"
    OTHER = "other"


class MetaculusQuestion(BaseModel, Jsonable):
    question_text: str
    page_url: str | None = None
    id_of_post: int = Field(
        validation_alias=AliasChoices("question_id", "post_id", "id_of_post")
    )
    id_of_question: int | None = None
    num_forecasters: int | None = None
    num_predictions: int | None = None
    state: QuestionState
    resolution_criteria: str | None = None
    fine_print: str | None = None
    background_info: str | None = None
    close_time: datetime | None = None
    actual_resolution_time: datetime | None = None
    scheduled_resolution_time: datetime | None = None
    date_accessed: datetime = Field(default_factory=datetime.now)
    api_json: dict = Field(
        description="The API JSON response used to create the question",
        default_factory=dict,
    )
    already_forecasted: bool = False

    @classmethod
    def from_metaculus_api_json(cls, post_api_json: dict) -> MetaculusQuestion:
        post_id = post_api_json["id"]
        logger.debug(f"Processing Post ID {post_id}")
        json_state = post_api_json["status"]
        question_state = (
            QuestionState.OPEN if json_state == "open" else QuestionState.OTHER
        )
        scheduled_resolution_time = cls._parse_api_date(
            post_api_json["scheduled_resolve_time"]
        )
        resolution_time_is_in_past = scheduled_resolution_time < datetime.now()
        question_json: dict = post_api_json["question"]

        try:
            forecast_values = question_json["my_forecasts"]["latest"][  # type: ignore
                "forecast_values"
            ]
            is_forecasted = forecast_values is not None
        except Exception:
            is_forecasted = False

        actual_resolve_time = (
            cls._parse_api_date(question_json["actual_resolve_time"])
            if question_json["actual_resolve_time"]
            else None
        )

        return MetaculusQuestion(
            state=question_state,
            question_text=question_json["title"],
            id_of_post=post_id,
            id_of_question=question_json["id"],
            background_info=question_json.get("description", None),
            fine_print=question_json.get("fine_print", None),
            resolution_criteria=question_json.get("resolution_criteria", None),
            page_url=f"https://www.metaculus.com/questions/{post_id}",
            num_forecasters=post_api_json["nr_forecasters"],
            num_predictions=post_api_json["forecasts_count"],
            close_time=cls._parse_api_date(
                post_api_json["scheduled_close_time"]
            ),
            actual_resolution_time=actual_resolve_time,
            scheduled_resolution_time=(
                scheduled_resolution_time
                if not resolution_time_is_in_past
                else None
            ),
            already_forecasted=is_forecasted,
            api_json=post_api_json,
        )

    @classmethod
    def _parse_api_date(cls, date_value: str | float) -> datetime:
        if isinstance(date_value, float):
            return datetime.fromtimestamp(date_value)
        assert isinstance(date_value, str)
        try:
            return datetime.strptime(date_value, "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass
        try:
            return datetime.strptime(date_value, "%Y-%m-%dT%H:%M:%SZ")
        except ValueError:
            pass
        return datetime.strptime(date_value, "%Y-%m-%d")

    @classmethod
    def get_api_type_name(cls) -> str:
        raise NotImplementedError(
            f"This function doesn't apply for base class {type(cls)}"
        )

    def give_question_details_as_markdown(self) -> str:
        today_string = datetime.now().strftime("%Y-%m-%d")
        question_details = textwrap.dedent(
            f"""
            The main question is:
            {self.question_text}

            Here is the resolution criteria:
            {self.resolution_criteria}

            Here is the fine print:
            {self.fine_print}

            Here is the background information:
            {self.background_info}

            Today is (YYYY-MM-DD):
            {today_string}
            """
        )
        return question_details.strip()


class BinaryQuestion(MetaculusQuestion):
    community_prediction_at_access_time: float | None = None

    @classmethod
    def from_metaculus_api_json(cls, api_json: dict) -> BinaryQuestion:
        normal_metaculus_question = super().from_metaculus_api_json(api_json)
        try:
            q2_center_community_prediction = api_json["question"]["aggregations"]["recency_weighted"]["latest"]["centers"]  # type: ignore
            assert len(q2_center_community_prediction) == 1
            community_prediction_at_access_time = (
                q2_center_community_prediction[0]
            )
        except (KeyError, TypeError):
            community_prediction_at_access_time = None
        return BinaryQuestion(
            community_prediction_at_access_time=community_prediction_at_access_time,
            **normal_metaculus_question.model_dump(),
        )

    @classmethod
    def get_api_type_name(cls) -> str:
        return "binary"


class BoundedQuestionMixin:
    @classmethod
    def _get_bounds_from_api_json(
        cls, api_json: dict
    ) -> tuple[bool, bool, float, float, float | None]:
        try:
            open_upper_bound = api_json["question"]["open_upper_bound"]  # type: ignore
            open_lower_bound = api_json["question"]["open_lower_bound"]  # type: ignore
        except KeyError:
            logger.warning(
                "Open bounds not found in API JSON defaulting to 'open bounds'"
            )
            open_lower_bound = True
            open_upper_bound = True

        upper_bound = api_json["question"]["scaling"]["range_max"]  # type: ignore
        lower_bound = api_json["question"]["scaling"]["range_min"]  # type: ignore
        zero_point = api_json["question"]["scaling"]["zero_point"]  # type: ignore

        assert isinstance(upper_bound, float), f"Upper bound is {upper_bound}"
        assert isinstance(lower_bound, float), f"Lower bound is {lower_bound}"
        return (
            open_upper_bound,
            open_lower_bound,
            upper_bound,
            lower_bound,
            zero_point,
        )


class DateQuestion(MetaculusQuestion, BoundedQuestionMixin):
    upper_bound: datetime
    lower_bound: datetime
    upper_bound_is_hard_limit: bool
    lower_bound_is_hard_limit: bool
    zero_point: datetime | None = None

    @classmethod
    def from_metaculus_api_json(cls, api_json: dict) -> DateQuestion:
        normal_metaculus_question = super().from_metaculus_api_json(api_json)
        (
            open_upper_bound,
            open_lower_bound,
            unparsed_upper_bound,
            unparsed_lower_bound,
            zero_point,
        ) = cls._get_bounds_from_api_json(api_json)

        if zero_point is not None:
            raise NotImplementedError(
                "Zero point not implemented for date questions yet"
            )

        return DateQuestion(
            upper_bound=cls._parse_api_date(unparsed_upper_bound),
            lower_bound=cls._parse_api_date(unparsed_lower_bound),
            upper_bound_is_hard_limit=not open_upper_bound,
            lower_bound_is_hard_limit=not open_lower_bound,
            **normal_metaculus_question.model_dump(),
        )

    @classmethod
    def get_api_type_name(cls) -> str:
        return "date"


class NumericQuestion(MetaculusQuestion, BoundedQuestionMixin):
    upper_bound: float
    lower_bound: float
    open_upper_bound: bool
    open_lower_bound: bool
    zero_point: float | None = None

    @classmethod
    def from_metaculus_api_json(cls, api_json: dict) -> NumericQuestion:
        normal_metaculus_question = super().from_metaculus_api_json(api_json)
        (
            open_upper_bound,
            open_lower_bound,
            upper_bound,
            lower_bound,
            zero_point,
        ) = cls._get_bounds_from_api_json(api_json)
        assert isinstance(upper_bound, float)
        assert isinstance(lower_bound, float)

        return NumericQuestion(
            upper_bound=upper_bound,
            lower_bound=lower_bound,
            open_upper_bound=open_upper_bound,
            open_lower_bound=open_lower_bound,
            zero_point=zero_point,
            **normal_metaculus_question.model_dump(),
        )

    @classmethod
    def get_api_type_name(cls) -> str:
        return "numeric"


class MultipleChoiceQuestion(MetaculusQuestion):
    options: list[str]

    @classmethod
    def from_metaculus_api_json(cls, api_json: dict) -> MultipleChoiceQuestion:
        normal_metaculus_question = super().from_metaculus_api_json(api_json)
        return MultipleChoiceQuestion(
            options=api_json["question"]["options"],  # type: ignore
            **normal_metaculus_question.model_dump(),
        )

    @classmethod
    def get_api_type_name(cls) -> str:
        return "multiple_choice"

    def give_question_details_as_markdown(self) -> str:
        original_details = super().give_question_details_as_markdown()
        final_details = (
            original_details
            + f"\n\nThe final options you can choose are:\n {self.options}"
        )
        return final_details.strip()
