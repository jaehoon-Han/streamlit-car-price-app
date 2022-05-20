import streamlit as st
import joblib
def run_ml() :
    st.subheader('자동차 구매 가능 금액 예측')

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

if __name__ == '__main__' :
    run_ml()