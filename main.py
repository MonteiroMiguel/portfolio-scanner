import streamlit as st 
from application.src.domain import get_page_content, get_portfolio, show_portfolio

st.title('Portfolio Scanner')
with st.form('Search'):
    address = st.text_input('Endereço da carteira').replace(' ', '')
    search = st.form_submit_button('Buscar')
    if search:
        soup = get_page_content(address)
        try:
            df_table = get_portfolio(soup)
            show_portfolio(df_table)
        except ValueError:
            st.write("Essa carteira não existe ou nunca realizou uma transação")


    
        
        
       