# fastapi 라이브러리에서 FastAPI를 불러온다.
from fastapi import FastAPI
from src.routers.house import house_router

# FastAPI 함수를 실행시키면, Fastapi 서버가 열리는데,
# 그 서버를 app이라는 변수에 담겠다. 
app = FastAPI() # app 변수에 fastapi 서버가 담김

# @ 데코레이터라고 부른다. 꾸며주는 아이.
# 함수나 클래스, 변수 등을 꾸며주는 역할
# 클라이언트가 get이라는 api를 요청하면 root라는 함수를 실행하겠다.
#http://127.0.0.1:8000 이게 지금 naver.com이게 나중에 도메인을 사서 이름을 바꿀 수 있음
#
@app.get("/")
async def root():
    return {"message": "Hello World"}

# get(리소스 요청) post(데이터에 맞는 생성 요청) 
# put(수정 요청) delete(삭제 요청)
# request : 요청, response : 응답
# request get : 데이터를 가져오는 요청
# request post : 데이터를 생성하는 요청
# request put : 데이터를 수정하는 요청
# 서버는 서비스를 제공하는 컴퓨터, 컴퓨터를 사용하는 사람은 클라이언트
# 클라이언트가 http request get 이라는 서비스를 요청함

# http://127.0.0.1:8000/user
# = naver.com/user
# async: 비동기 함수
@app.get("/user")
async def getUser():
    return {"name": "jiyul", "age": 25}



# 함수를 생성하고 app.get()을 통해서 바로 실행시키는 역할을 해줌

# @app.get(url)을 하지않으면
# def get(url);
#     something()
#     getUser()
#     somthing()

# HTTP 5개
# GET(read), POST(create)
# PUT(update), PATCH(update), 
# DELETE(delete)

# prefix: /house 라는 경로를 타면 house_router로 가게끔 길을 붙여준다.
# 요즘 추세는 리소스 추세로 이름을 짓는다. 
app.include_router(house_router, prefix="/house") # house_router를 포함시킨다.