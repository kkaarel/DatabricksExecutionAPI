
import streamlit as st 
from databricks import sql
import os


st.set_page_config(layout="wide")


connection = sql.connect(
                        server_hostname = st.secrets["workspace"],
                        http_path = st.secrets["http_path"],
                        access_token = st.secrets["pat"])

cursor = connection.cursor()


st.header("Query you data from Databricks")
query = st.text_input("Enter SQL query here:")
if st.button("Execute"):
    cursor.execute(query)
    st.header("Results")
    st.dataframe(cursor.fetchall(), width=False)



cursor.close()
connection.close()