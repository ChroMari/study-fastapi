from fastapi import BackgroundTasks, Cookie, FastAPI, Response
from datetime import datetime

app = FastAPI()


def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)


@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks): # background_tasks - создаёт сам FastAPI
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}


# --- cookie
@app.get("/items/")
async def read_items(ads_id: str | None = Cookie(default=None)):
    return {"ads_id": ads_id}


# --- Доступ к файлам cookie
@app.get("/")
def root(last_visit = Cookie()):
    return  {"last visit": last_visit}


# --- Установка файлов cookie
@app.get("/new")
def root(response: Response):
    now = datetime.now()    # получаем текущую дату и время
    response.set_cookie(key="last_visit", value=now)
    return  {"message": "куки установлены"}

# --- Прочие возможности при работе с cookie
@router.post("/logout", status_code=204)
async def logout_user(response: Response):
    response.delete_cookie("example_access_token")