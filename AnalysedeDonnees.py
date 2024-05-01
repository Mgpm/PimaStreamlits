import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import streamlit as st,requests


st.title("Ce formulaire prédit le diabète")

datatest = pd.read_csv('test.csv')

for i in datatest.columns[1:]:
    st.selectbox(i,list(set(datatest[i].values)),key=i)

if st.button('button'):
        data = requests.get("http://mallocpaul.pythonanywhere.com/modelApi", params=st.session_state).json()
        #data = requests.get("http://localhost:5000/modelApi", params=st.session_state).json()
        output_query = data
        st.header("Query Response")
        st.write( output_query)



