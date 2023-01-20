from fastapi import APIRouter
from sql_base.models import menu
import resolvers.menu


menu_router = APIRouter()

@menu_router.get("/get")
def get_menu():
    return f'Response:{{text:Страница с информацией о меню}}'

@menu_router.post("/create")
def new_menu(menu: menu,):
    new_id = resolvers.menu.new_menu(menu)
    return f"{{code: 201, id: {new_id}}}"

@menu_router.delete("/delete/{menu_id}")
def delete_menu(menu_id: int):
    return f'delete menu {menu_id}'
