from flask import Flask, render_template, request
import joblib
import pandas as pd

# Flask 앱 초기화
app = Flask(__name__)

# 모델 로드
model = joblib.load('model.pkl')  # 모델을 'model.pkl'에서 로드

# 홈 페이지 라우트
@app.route('/')
def index():
    return render_template('index.html')  # index.html 페이지를 렌더링

# 예측을 처리하는 라우트
@app.route('/predict', methods=['POST'])
def predict():
    # 사용자가 입력한 값 받기
    pm25 = float(request.form['pm25'])
    o3 = float(request.form['o3'])
    no2 = float(request.form['no2'])
    co = float(request.form['co'])
    so2 = float(request.form['so2'])

    # 입력값을 딕셔너리로 변환
    user_data = {
        '초미세먼지PM2.5 (㎍/m3)': pm25,
        '오존O3 (ppm)': o3,
        '이산화질소NO2 (ppm)': no2,
        '일산화탄소CO (ppm)': co,
        '아황산가스SO2(ppm)': so2
    }

    # 입력 데이터를 DataFrame으로 변환
    user_df = pd.DataFrame([user_data])

    # 결측값 처리 (평균값으로 대체)
    user_df = user_df.fillna(user_df.mean())

    # 모델을 사용하여 예측
    prediction = model.predict(user_df)

    # 예측 결과를 웹 페이지에 전달
    return render_template('result.html', prediction=prediction[0])

# 웹 서버 실행
if __name__ == '__main__':
    app.run()
