# fastapi-admin

### 项目默认会安装

- fastapi_pagination
- fastapi
- tortoise-orm

### 目前只支持pydantic-v2

## 简单示例

> main.py

```python
from fastapi import FastAPI,Depends
from tortoise.contrib.fastapi import register_tortoise
from uvicorn import run
from models import User
from fastapi_tortoise_crud.crud import ModelCrud

user = ModelCrud(User,
                 schema_filters=User.schema_filters(include=('username',)),
                 # 除了read接口，其他接口都需要登录
                 # dependencies=[Depends(get_current_user)],
                 # depends_read=False
                 )
app = FastAPI()

app.include_router(user, prefix='/user', tags=['用户管理'])


@app.get("/")
async def root():
    return {"message": "Hello World"}


register_tortoise(
    app,
    db_url="sqlite://:memory:",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

if __name__ == '__main__':
    run("main:app", port=2103, reload=True)
```

> models.py

```python
from fastapi_tortoise_crud.model import BaseModel
from tortoise import fields


class User(BaseModel):
    username = fields.CharField(64)
    password = fields.CharField(32)
    nickname = fields.CharField(32, null=True, default='游客')

```

### 路由
![img.png](img.png)
