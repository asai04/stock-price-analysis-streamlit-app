#Stock Price Analysis Tutorial to Build App

import yfinance as yf
import streamlit as st

st.write()

tS = 'GOOGL'
tD = yf.Ticker(tS)

tDf = tD.history(period='1d', start='2015-5-31', end='2020-5-31')

st.write()
st.line_chart(tDf.Close)
st.write()
st.line_chart(tDf.Volume)

#In cmd, use python -m streamlit run app