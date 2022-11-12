from fastapi import APIRouter
from api.endpoints import separation_endpoints

# TODO: In case we need more endpoints files
api_router = APIRouter()
api_router.include_router(separation_endpoints.router, tags=['separation flow'])
