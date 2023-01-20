from sql_base import base_worker
from sql_base import models

def get_menu(menu_id: int):
    return base_worker.insert_data("SELECT id, price, weight, ingredient, name_of_the_dish_ID  FROM menu WHERE id =?",
                               (menu_id,))
def new_menu(menu: models) -> int:
    new_id = base_worker.insert_data("INSERT INTO menu (id, price, weight, ingredient, name_of_the_dish_ID)"
                                 "VALUES (?, ?, ?, ?, ?)"
                                 "RETURNING id",
                                 (menu.id, menu.price, menu.weight, menu.ingredient, menu.name_of_the_dish_ID))
    return new_id
def delete_menu(menu_id: int):
    return base_worker.execute(query="DELETE FROM menu WHERE id=? ",
                              args=(menu_id,))