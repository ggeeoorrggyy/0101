from sql_base import base_worker
from sql_base import models

def get_cafe(cafe_id: int):
    return base_worker.insert_data("SELECT id, city, number, name, address, Menu_ID, Staff_ID  FROM cafe WHERE id =?",
                               (cafe_id,))
def new_cafe(cafe: models) -> int:
    new_id = base_worker.insert_data("INSERT INTO cafe (id, city, number, name, address, Menu_ID, Staff_ID)"
                                 "VALUES (?, ?, ?, ?, ?,?,?)"
                                 "RETURNING id",
                                 (cafe.id, cafe.city, cafe.number, cafe.name, cafe.address, cafe.Menu_ID, cafe.Staff_ID ))
    return new_id
def delete_cafe(cafe_id: int):
    return base_worker.execute(query="DELETE FROM cafe WHERE id=? ",
                              args=(cafe_id,))

