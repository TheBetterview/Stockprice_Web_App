import yfinance as yf
import streamlit as st
import pandas as pd


# Page title

st.write(""" 
# Simple stock price web app

Shown are the stock closing price and volume of Meta, Amazon, Apple, Netflix, Google and Microsoft companies


""")

# define the ticker symbols

tickerSymbolF = 'META'
tickerSymbolA = 'AMZN'
tickerSymbolAA = 'AAPL'
tickerSymbolN = 'NFLX'
tickerSymbolG = 'GOOG'
tickerSymbolM = 'MSFT'

# Get Data on this tickers

tickerdataF = yf.Ticker(tickerSymbolF)
tickerdataA = yf.Ticker(tickerSymbolA)
tickerdataAA = yf.Ticker(tickerSymbolAA)
tickerdataN = yf.Ticker(tickerSymbolN)
tickerdataG = yf.Ticker(tickerSymbolG)
tickerdataM = yf.Ticker(tickerSymbolM)


# Get the historical proces for this ticker
tickerDFF = tickerdataF.history(period ='1d', start='2005-01-01', end = '2022-09-30')
tickerDFA = tickerdataA.history(period ='1d', start='2005-01-01', end = '2022-09-30')
tickerDFAA = tickerdataAA.history(period ='1d', start='2005-01-01', end = '2022-09-30')
tickerDFN = tickerdataN.history(period ='1d', start='2005-01-01', end = '2022-09-30')
tickerDFG = tickerdataG.history(period ='1d', start='2005-01-01', end = '2022-09-30')
tickerDFM = tickerdataM.history(period ='1d', start='2005-01-01', end = '2022-09-30')


# Open High low close volumen dividens stock splits of META

st.write(""" 
## META """)

st.write(""" 
### Closing Price """)

st.line_chart(tickerDFF.Close)

st.write(""" 
### Volume """)

st.line_chart(tickerDFF.Volume)

# Open High low close volumen dividens stock splits of Amazon

st.write(""" 
## AMAZON """)

st.write(""" 
### Closing Price """)

st.line_chart(tickerDFA.Close)

st.write(""" 
### Volume """)

st.line_chart(tickerDFA.Volume)

# Open High low close volumen dividens stock splits of Apple

st.write(""" 
## APPLE """)

st.write(""" 
### Closing Price """)

st.line_chart(tickerDFAA.Close)

st.write(""" 
### Volume """)

st.line_chart(tickerDFAA.Volume)


# Open High low close volumen dividens stock splits of Netflix

st.write(""" 
## NETFLIX """)

st.write(""" 
### Closing Price """)

st.line_chart(tickerDFN.Close)

st.write(""" 
### Volume """)

st.line_chart(tickerDFN.Volume)


# Open High low close volumen dividens stock splits of Google 

st.write(""" 
## GOOGLE """)

st.write(""" 
### Closing Price """)

st.line_chart(tickerDFG.Close)

st.write(""" 
### Volume """)

st.line_chart(tickerDFG.Volume)

# Open High low close volumen dividens stock splits of Microsoft

st.write(""" 
## Microsoft """)

st.write(""" 
### Closing Price """)

st.line_chart(tickerDFM.Close)

st.write(""" 
### Volume """)

st.line_chart(tickerDFM.Volume)

