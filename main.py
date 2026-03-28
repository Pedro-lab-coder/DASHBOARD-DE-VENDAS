import streamlit as st
import pandas as pd

tabela = pd.read_excel("Tabela.xlsx")

st.title("Dashboard de Vendas")

# filtro de lojas
Location = st.multiselect(
    "Selecione as Lojas (Store)",
    tabela["Location"].unique()
)

if Location:
    tabela = tabela[tabela["Location"].isin(Location)]

# métricas
st.metric("Faturamento total", f"R$ {tabela['TotalPrice'].sum():,.2f}")
st.metric("Ticket médio", f"R$ {tabela['TotalPrice'].mean():,.2f}")

# gráfico por loja
faturamento_loja = tabela.groupby("Location")["TotalPrice"].sum()
st.bar_chart(faturamento_loja)

# gráfico por produto
faturamento_produto = tabela.groupby("Product")["TotalPrice"].sum()
st.bar_chart(faturamento_produto)