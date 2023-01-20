from fastapi import APIRouter
from sql_base.models import cafe
import resolvers.cafe


cafe_router = APIRouter()

@cafe_router.get("/get")
def get_cafe():
    return f'Response:{{text:Страница с информацией о кафе}}'

@cafe_router.post("/create")
def new_cafe(cafe: cafe,):
    new_id = resolvers.cafe.new_cafe(cafe)
    return f"{{code: 201, id: {new_id}}}"

@cafe_router.delete("/delete/{cafe_id}")
def delete_cafe(cafe_id: int):
    return f'delete cafe {cafe_id}'


