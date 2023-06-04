import dataclasses
from typing import Annotated, Sequence

from fastapi import APIRouter, Depends, Query
from fastapi.responses import ORJSONResponse

from app.entities.category.category_codes import CategoryCode
from app.services.category_service import get_distinct_home_categories

router = APIRouter(prefix="/v1/home_categories", tags=["Home Category"], redirect_slashes=False)


@dataclasses.dataclass
class CoordinatesRequest:
    longitude: Annotated[float, Query(..., example=127.005926, gt=124, lt=132)]
    latitude: Annotated[float, Query(..., example=37.49006, gt=33, lt=39)]

    def __post_init__(self) -> None:
        self.longitude = round(self.longitude, 5)
        self.latitude = round(self.latitude, 5)


@dataclasses.dataclass
class CategoryResponse:
    categories: Sequence[CategoryCode]


@router.get(
    "/distinct",
    description="distinct 쿼리를 날려서 카테고리 목록을 구합니다.",
    response_class=ORJSONResponse,
)
async def api_get_categories_distinct(coordinates: Annotated[CoordinatesRequest, Depends()]) -> CategoryResponse:
    return CategoryResponse(categories=await get_distinct_home_categories(coordinates.longitude, coordinates.latitude))
