from typing import List
import xgboost as xgb
import pandas as pd

loaded_model = xgb.XGBRegressor()

loaded_model.load_model('src/models/xgb_model.json')

def run_model(crim: float, rm: float) -> float: # return type이 이거다!

    # 미리 준비된 input 데이터(임시). 나중에는 Http Request에 담아서 보낼 것이다.
    dic = {
    "CRIM": [crim],
    "ZN": [18.0],
    "INDUS": [22.37],
    "CHAS": [0],
    "NOX": [0.145],
    "RM": [rm],
    "AGE": [66.7],
    "DIS": [4.291],
    "RAD": [13],
    "TAX": [333.333],
    "PTRATIO": [21.0],
    "B": [197.6],
    "LSTAT": [23.4],
    }
    
    # dictionary 형태를 DataFrame 형태로 변환한다.
    input = pd.DataFrame.from_dict(dic, orient='columns')

    # input 값을 이용해서 예측값을 만들고, z에 대입한다.  
    z = loaded_model.predict(input)

    # 변수 z의 타입이 numpy이기 때문에 list로 바꿔준다.
    result: List[float] = z.tolist()

    return result[0]

# async def로 함수를 실행하면  -> async await로 함수를 실행해야함