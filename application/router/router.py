from fastapi import APIRouter
from application.config.db import engine
from application.model.post import posts
from application.schema.post_schema import PostSchema

post = APIRouter()

@post.get('/')
def root():
    return { "message": "hello world"}

@post.get('/api/v1/post')
async def get_posts():
    with engine.connect() as conn:
        result = conn.execute(posts.select()).fetchall()
        return result

@post.get('/api/v1/post/{post_id}', response_model=PostSchema)
def get_post(post_id: str):
    with engine.connect() as conn:
        result = conn.execute(posts.select().where(posts.c.id == post_id)).first()
        return result
        

@post.post('/api/v1/post')
def create_post(data_post: PostSchema):
    with engine.connect() as conn:
        new_post = data_post.dict()
        result = conn.execute(posts.insert().values(new_post))
        return get_post(result.lastrowid)

@post.put('/api/v1/post/{post_id}')
def update_post(post_id: str, data_post: PostSchema):
    with engine.connect() as conn:
        conn.execute(posts.update().values(name = data_post.name, description = data_post.description, latitude= data_post.latitude, longitude= data_post.longitude).where(posts.c.id == post_id))
        return get_post(post_id)


@post.delete('/api/v1/post/{post_id}')
def delete_post(post_id: str):
    with engine.connect() as conn:
        conn.execute(posts.delete().where(posts.c.id == post_id))
        return post_id