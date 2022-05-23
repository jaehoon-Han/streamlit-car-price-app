import streamlit as st
import joblib
import numpy as np
import sklearn as sk

def run_ml() :
    st.subheader('자동차 구매 가능 금액 예측')

    print(sk.__version__)

    # 예측하기 위해선 필요한 파일을 불러와야 한다
    # 이 예에서는 
    # 3개를 불러와야 한다.

    regressor = joblib.load('data/regressor.pkl')
    scaler_X = joblib.load('data/scaler_X.pkl')
    sclaer_y = joblib.load('data/scaler_y.pkl')

    # 성별, 나이, 연봉, 카드빚, 자산을 입력받도록 만드세요.
    word = st.text_input('성별과 나이, 연봉 및 카드빚과 자산을 입력하세요')
    gender = st.radio('성별을 선택하세요',['남','여'])
    if gender == '여자' :
        gender = 0
    else :
        gender = 1
    age = st.number_input('나이 입력', min_value = 1, max_value = 105)
    salary = st.number_input('연봉 입력', min_value = 0, max_value = 105000000)
    debt = st.number_input('빚 입력', min_value = 0, max_value = 105000000)
    worth = st.number_input('자산 입력', min_value = 0, max_value = 10505050)

    if st.button('자동차 구매 금액 예측') :     

        # 1. 신규 고객의 정보를 넘파이 어레이로 만들어준다.
        new_data = np.array([gender, age, salary, debt, worth])

        # 2. 학습할 때 사용한 X 의 피처스케일러를 이용해서, 피처스케일링 한다.
        # 먼저, 데이터를 2차원으로 만들어 준다.
        new_data = new_data.reshape(1,5)
        new_data = scaler_X.transform(new_data)

        # 3. 인공지능에게 예측해달라고 한다.
        y_pred = regressor.predict(new_data)

        # 4. 예측한 값을, 원상복구 시킨다.
        y_pred = sclaer_y.inverse_transform(y_pred)
        y_pred = round(y_pred[0,0])

        st.write(y_pred[0,0])

        st.write( ' 이 사람의 구매 가능 금액은 '+ y_pred[0,0] + '달라 입니다.')





if __name__ == '__main__' :
    run_ml()

