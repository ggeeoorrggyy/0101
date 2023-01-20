from fastapi import FastAPI
from sql_base import base_worker
from settings import BASE_PATH
from routers.cafe import cafe_router
from routers.menu import menu_router
from routers.staff import staff_router
from routers.users import user_router


base_worker.set_base_path(BASE_PATH)

if not base_worker.check_base():
    base_worker.create_base('../sql/base.sql')

app = FastAPI()


app.include_router(cafe_router, prefix='/cafe')
app.include_router(menu_router, prefix='/menu')
app.include_router(staff_router, prefix='/staff')
app.include_router(user_router, prefix='/users')

