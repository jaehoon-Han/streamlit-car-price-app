import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def run_eda() :
    st.subheader('데이터 분석')

    df = pd.read_csv('data/Car_Purchasing_Data.csv',encoding='ISO-8859-1')

    # 라디오버튼을 이용해서, 데이터프레임과, 통계치를 선택해서
    # 보여줄 수 있도록 만든다.
    radio_menu = ['데이터 프레임', '통계치']
    selected = st.radio('선택하세요', radio_menu )

    if selected == radio_menu[0] :
        st.dataframe( df )
    elif selected == radio_menu[1] :
        st.dataframe(df.describe())
    
    ## 컬럼명을 보여주고, 컬럼을 선택하면,
    ## 해당 컬럼의 최대값 데이터와, 최소값 데이터를 보여준다
        
        col_list = df.columns[4 : ]

        selected_col = st.selectbox('최대 최소 원하는 컬럼 선택', col_list )

        df_max = df.loc[df['selected_col'] == df['selected_col'].max(), ]
        df_min = df.loc[df['selected_col'] == df['selected_col'].min(), ]
        #st.text('{}컬럼의 최대값에 해당하는 데이터입니다.)
        st.dataframe(df_max)
        st.dataframe(df_min)
        
        #유저가 선택한 컬럼들만, pairplot 그리고
        # 그 아래, 상관계수를 보여준다.

        selected_list = st.multiselect('컬럼들 선택', col_list)
        # print(selected_list)

        if len(selected_list != 0) :
            fig1 = sns.pairplot(data = df[selected_list])
            st.pyplot(fig1)
        
            st.text('선택하신 컬럼끼리의 상관계수 입니다.')
            st.dataframe(df[selected_list].corr())


            fig2 = plt.figure()
            sns.heatmap(data = df[selected_list].corr(), annot=True, vmin= -1, vmax = 1, cmap='coolwarm', linewidths=0.5)
            st.pyplot(fig2)

            # 고객 이름 컬럼을 검색할 수 있도록 만듭니다.
            # he 라고 넣으면, he 가 이름에 들어있는 고객들의 데이터를
            # 가져옵니다.

            # 1. 유저한테 검색어를 입력받는다.
            word = st.text_input('이름을 검색할 단어를 입력하세요.')

            # 2. 검색어를 고객이름 컬럼에 들어있는 데이터 가져온다
            result = df.loc[ df['Customer Name'].str.contains(word)]

            # 3. 화면에 보여준다.
            st.dataframe(result)


