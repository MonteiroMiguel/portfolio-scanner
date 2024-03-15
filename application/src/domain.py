import streamlit as st
from bs4 import BeautifulSoup
import requests
import pandas as pd
from io import StringIO

def get_page_content(address):
    url = f'https://polygonscan.com/address/{address}#multichain-portfolio'
    header = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'}) 
    webpage = requests.get(url, headers=header) 
    soup = BeautifulSoup(webpage.content, "lxml") 
    return soup

def get_portfolio(soup):
    table = soup.find("table", id='js-chain-table')
    df_table = pd.read_html(StringIO(str(table)))[0]
    return df_table

def show_portfolio(df_table):
    if df_table.empty:
        st.write("Essa carteira não existe ou nunca realizou uma transação")
    else:
        st.write(df_table)