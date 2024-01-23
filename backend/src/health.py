from fastapi import APIRouter
from fastapi import status
from pydantic import BaseModel

router = APIRouter()


class HealthCheck(BaseModel):
    status: str = "OK"


@router.get(
    "/health",
    tags=["healthcheck"],
    summary="Health Check",
    response_description=" Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
def get_health() -> HealthCheck:
    return HealthCheck(status="OK")
