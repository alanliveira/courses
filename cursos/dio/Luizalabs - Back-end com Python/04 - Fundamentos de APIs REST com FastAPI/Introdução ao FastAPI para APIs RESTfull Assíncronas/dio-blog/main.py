from datetime import datetime, timezone
from typing import Annotated

from fastapi import Cookie, FastAPI, Header, Response, status
from pydantic import BaseModel

app = FastAPI()

fake_db = [
    {
        "id": 1,
        "title": "Criando uma aplicação com o Rails",
        "date": datetime.now(timezone.utc).strftime("%d/%m/%Y"),
        "published": True,
    },
    {
        "id": 2,
        "title": "Internacionalizando uma app com o Rails",
        "date": datetime.now(timezone.utc).strftime("%d/%m/%Y"),
        "published": True,
    },
    {
        "id": 3,
        "title": "Internacionalizando uma app com o Django",
        "date": datetime.now(timezone.utc).strftime("%d/%m/%Y"),
        "published": True,
    },
    {
        "id": 4,
        "title": "Internacionalizando uma app com o Django",
        "date": datetime.now(timezone.utc).strftime("%d/%m/%Y"),
        "published": False,
    },
    {
        "id": 5,
        "title": "Internacionalizando uma app com o Flask",
        "date": datetime.now(timezone.utc).strftime("%d/%m/%Y"),
        "published": True,
    },
    {
        "id": 6,
        "title": "Internacionalizando uma app com o Flash",
        "date": datetime.now(timezone.utc).strftime("%d/%m/%Y"),
        "published": True,
    },
]


class Post(BaseModel):
    id: int
    title: str
    date: datetime = datetime.now(timezone.utc)
    published: bool = False


@app.get("/posts")
def read_posts(
    response: Response,
    page: int = 1,
    per_page: int = 5,
    ads_id: Annotated[str | None, Cookie()] = None,
    user_agent: Annotated[str | None, Header()] = None,
):
    print(f"Cookie: {ads_id}")
    print(f"User Agent: {user_agent}")

    response.set_cookie(key="user", value="maria@vaicomoutras.com")
    if per_page > len(fake_db):
        return fake_db

    return fake_db[:per_page]


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post.id = len(fake_db) + 1
    fake_db.append(post.model_dump())
    return post


@app.get("/posts/{id_post}")
def read_post(id_post: int):
    return next(filter(lambda post: post["id"] == id_post, fake_db), None)
