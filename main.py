from unittest.util import _MAX_LENGTH
from typing import Union
from fastapi import FastAPI, Path, Query, Form, File, UploadFile
from pydantic import BaseModel

app=FastAPI()

# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: str):
#     return {"item_id": item_id, "q": q}

@app.get("/profile/")
async def read_profile(id:int):
    return {
        "id": id,
        "f_name": "Gunjon",
        "l_name": "Roy",
        "phone": "01533702981",
        "image": "https://scontent.fdac22-1.fna.fbcdn.net/v/t39.30808-6/397462269_6721358314624591_7332706261685508404_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=efb6e6&_nc_eui2=AeE0hRoDNol-pj_1eF-j45V9pUM_HKQgBJqlQz8cpCAEmkyK7FQbA30acb_emQwMhsuvC0vLaoLVnJ6ZdKZzgeaz&_nc_ohc=qP9KnjDJmc8AX_hwwUW&_nc_ht=scontent.fdac22-1.fna&oh=00_AfC7UbD-2hM2cGLnbbGAUXZnNAUcZtxB0hPd1XxMro0mdg&oe=6575D20F",
        "email": "gunjon.cse@gmail.com",
        "password": "$2y$10$cVcyDP9btDKfY646Eu0h5OAf/snjgAezrzt1llm2OFngRUZKgmUjy",
        "status": "approved",
        "remember_token": "MGuiJJoXYrdvQHVEA3FJijpbOYIB3KQwJk6Hzh8UnxaT8qhHawezg67YFmer",
        "is_phone_verified": "1",
        "created_at": "2023-04-30T03:35:30.000000Z",
        "updated_at": "2023-08-22T09:46:49.000000Z",
        "bank_name": "Islami Bank Ltd",
        "branch": "Abdullapur",
        "account_no": "133445235233",
        "holder_name": "GUNJON ROY",
        "auth_token": "I3MvpNj0gfkdzNBbsH1Zzi0rSguCOsaTJ3g3AjpuBWu49OphMhw716krSfqKKkpcgCcoc06IwWFgi299",
        "sales_commission_percentage": 12.6,
        "gst": 2,
        "cm_firebase_token": None,
        "pos_status": "0"
    }

@app.get("/item/{item}")
def path_func(item:int):
    var_name={"path_variable": item}
    return var_name

profile_data={
            "user_name": "userName",
            "f_name": "Gunjon",
            "l_name": "Roy",
            "phone": "01533702981",
            "image": "https://scontent.fdac22-1.fna.fbcdn.net/v/t39.30808-6/397462269_6721358314624591_7332706261685508404_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=efb6e6&_nc_eui2=AeE0hRoDNol-pj_1eF-j45V9pUM_HKQgBJqlQz8cpCAEmkyK7FQbA30acb_emQwMhsuvC0vLaoLVnJ6ZdKZzgeaz&_nc_ohc=qP9KnjDJmc8AX_hwwUW&_nc_ht=scontent.fdac22-1.fna&oh=00_AfC7UbD-2hM2cGLnbbGAUXZnNAUcZtxB0hPd1XxMro0mdg&oe=6575D20F",
            "email": "gunjon.cse@gmail.com",
            "password": "$2y$10$cVcyDP9btDKfY646Eu0h5OAf/snjgAezrzt1llm2OFngRUZKgmUjy",
            "status": "approved",
            "remember_token": "MGuiJJoXYrdvQHVEA3FJijpbOYIB3KQwJk6Hzh8UnxaT8qhHawezg67YFmer",
            "is_phone_verified": "1",
            "created_at": "2023-04-30T03:35:30.000000Z",
            "updated_at": "2023-08-22T09:46:49.000000Z",
            "bank_name": "Islami Bank Ltd",
            "branch": "Abdullapur",
            "account_no": "133445235233",
            "holder_name": "GUNJON ROY",
            "auth_token": "I3MvpNj0gfkdzNBbsH1Zzi0rSguCOsaTJ3g3AjpuBWu49OphMhw716krSfqKKkpcgCcoc06IwWFgi299",
            "sales_commission_percentage": 12.6,
            "gst": 2,
            "cm_firebase_token": None,
            "pos_status": "0"
        }
@app.get("/login/")
async def login_func(userName:str,password):
    if(userName=="gunjonroy" and password=="123456"):
        return {
            "status":200,
            "message":"Successfuly logged in",
            "data":profile_data
        }
    else:
        errorList=[]
        if(userName!="gunjonroy"):
            errorList.append(
                    {
                        "message": "user_name",
                        "error": "User Name is not currect"
                    }
                )
        if(password!="123456"):
            errorList.append(
                    {
                        "message": "password",
                        "error": "password is not currect"
                    }
                )
        return {
            "status": 401,
            "message": "Unauthorised.",
            "errors": errorList
        }
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id":item_id}


# Query Parameters¶
# Query Parameters¶
# Query Parameters¶
# Query Parameters¶

product_items_db=[
    {
        "id":123,
        "product_name":"product name 1",
        "product_price":343,
        "product_selling_price":400
    },
    {
        "id":124,
        "product_name":"product name 2",
        "product_price":400,
        "product_selling_price":450
    },
    {
        "id":125,
        "product_name":"product name 3",
        "product_price":370,
        "product_selling_price":500
    },
    {
        "id":126,
        "product_name":"product name 1",
        "product_price":120,
        "product_selling_price":200
    },
    {
        "id":123,
        "product_name":"product name 1",
        "product_price":343,
        "product_selling_price":400
    },
    {
        "id":124,
        "product_name":"product name 2",
        "product_price":400,
        "product_selling_price":450
    },
    {
        "id":125,
        "product_name":"product name 3",
        "product_price":370,
        "product_selling_price":500
    },
    {
        "id":126,
        "product_name":"product name 1",
        "product_price":120,
        "product_selling_price":200
    },
     {
        "id":123,
        "product_name":"product name 1",
        "product_price":343,
        "product_selling_price":400
    },
    {
        "id":124,
        "product_name":"product name 2",
        "product_price":400,
        "product_selling_price":450
    },
    {
        "id":125,
        "product_name":"product name 3",
        "product_price":370,
        "product_selling_price":500
    },
    {
        "id":126,
        "product_name":"product name 1",
        "product_price":120,
        "product_selling_price":200
    },
    {
        "id":123,
        "product_name":"product name 1",
        "product_price":343,
        "product_selling_price":400
    },
    {
        "id":124,
        "product_name":"product name 2",
        "product_price":400,
        "product_selling_price":450
    },
    {
        "id":125,
        "product_name":"product name 3",
        "product_price":370,
        "product_selling_price":500
    },
    {
        "id":126,
        "product_name":"product name 1",
        "product_price":120,
        "product_selling_price":200
    }
]

# Request Body¶ 
# Request Body¶
# Request Body¶
# Request Body¶
# Request Body¶
# Request Body¶
# Request Body¶

class Product(BaseModel):
    productName: str
    description: str | None = None
    price: float
    tax:float | None=None

@app.post("/products/")
async def create_product(product:Product):
    product_items_db.append(product)
    return product_items_db


@app.post("/form/data/")
async def form_data(username:str=Form(),password =Form()):
    return {"username":username,"password":password}

@app.post("/file/uploadfile")
async def file_bytes_len(file: bytes = File()):
    return ({"file": len(file)})

@app.post("/upload/file")
async def file_upload(file:UploadFile):
    return ({"file":file})
