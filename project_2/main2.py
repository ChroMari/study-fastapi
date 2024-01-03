from fastapi import FastAPI
from models import UserId, UserAge
from data import user_id_data

app = FastAPI()


@app.get("/users")
async def user_id():
    user: UserId = UserId(**user_id_data)

    return user


@app.post("/user")
async def write_is_adult(user: UserAge):
    user = dict(user)
    user["is_adult"] = user["age"] >= 18

    return user




insert_reviewers_query = """
INSERT INTO reviewers
(uid, owner, now_data)
VALUES ( %s, %s, %s )
"""

def write_sql_information(transport_info):
    #current_datetime = datetime.now()
    transport_info = dict(transport_info)
    transport_info["now_data"] = datetime.now()

    # print(current_datetime)
    try:
        with connect(
            host="localhost",
            user="root",
            password="01289",
            database="transport",
        ) as connection:
            with connection.cursor() as cursor:
                cursor.executemany(insert_reviewers_query, transport_info)
                connection.commit()
    except Error as e:
        print(e)