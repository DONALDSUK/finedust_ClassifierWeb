import joblib
import pandas as pd

# 모델 로드
model = joblib.load('model.pkl')  # 모델을 'model.pkl'에서 로드

# 사용자가 입력한 값 받기
def get_user_input():
    print("대기 오염 물질 농도를 입력해주세요:")

    # 각 변수의 값 입력받기
    pm25 = float(input("초미세먼지 PM2.5 농도 (㎍/m3): "))
    o3 = float(input("오존 O3 농도 (ppm): "))
    no2 = float(input("이산화질소 NO2 농도 (ppm): "))
    co = float(input("일산화탄소 CO 농도 (ppm): "))
    so2 = float(input("아황산가스 SO2 농도 (ppm): "))

    # 입력값을 딕셔너리로 반환
    return {
        '초미세먼지PM2.5 (㎍/m3)': pm25,
        '오존O3 (ppm)': o3,
        '이산화질소NO2 (ppm)': no2,
        '일산화탄소CO (ppm)': co,
        '아황산가스SO2(ppm)': so2
    }

# 모델을 사용하여 예측
def predict_air_quality(input_data):
    # 입력 데이터를 DataFrame으로 변환
    user_df = pd.DataFrame([input_data])

    # 결측값 처리 (평균값으로 대체)
    user_df = user_df.fillna(user_df.mean())

    # 모델을 사용하여 예측
    prediction = model.predict(user_df)

    # 예측 결과 출력
    print(f"\n예측된 대기질 등급: {prediction[0]}")

# 프로그램 실행
user_input = get_user_input()  # 사용자 입력 받기
predict_air_quality(user_input)  # 예측 수행
