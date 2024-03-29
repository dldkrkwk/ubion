import streamlit as st 
import FinanceDataReader as fdr
import datetime

# pip install -U finance-datareader

date = st.date_input(
    '조회 시작일을 선택해 주세요',
    datetime.datetime(2022,1,1)
)

# 삼성전자 : 005930
code = st.text_input(
    '종목코드',
    value='',
    placeholder='종목코드를 입력해주세요'
)

if code and date:
    df = fdr.DataReader(code,date)
    data = df.sort_index(ascending=True).loc[:,'Close']
    st.line_chart(data)