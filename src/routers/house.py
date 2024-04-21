# router: 길을 터주는 애

from fastapi import APIRouter
from pydantic import BaseModel
from src.services.house import run_model

# 길을 붙여주는 애를 house_router랑 router 변수에 담을거다.
house_router = router = APIRouter()

# /house/prcie/predict 로 Get 요청이 들어오면 실행
# main.py에서 include_router를 통해 house_router를 포함시키면
# /house/prcie/predict로 요청이 들어오면 이 함수를 실행한다.
# 왜냐하면 main.py 에서 house라는 prefix를 붙여서 price/predict로 요청이 들어오기 때문이다.
@router.get('/price/predict')
async def get_prediction_of_house_price(criminal: float, room: float):
    price = run_model(criminal, room)
    return price

# 더 만들고 싶다면 @router.get('/price/what')

# 모든 @는 if문으로 보면 된다.