from preProcessing import preProcessing
from normalize import normalize
from decomposition import decomposition
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import streamlit as st,requests


st.sidebar.title("Ce formulaire prédit le diabète")

datatest = pd.read_csv('test.csv')

for i in datatest.columns[1:]:
    st.sidebar.selectbox(i,list(set(datatest[i].values)),key=i)

if st.sidebar.button('button'):
        data = requests.get("http://mallocpaul.pythonanywhere.com/modelApi", params=st.session_state).json()
        #data = requests.get("http://localhost:5000/modelApi", params=st.session_state).json()
        output_query = data
        st.sidebar.header("Query Response")
        st.sidebar.write( output_query)


st.title("Analyse de Données")
pr = preProcessing()
n = normalize()
d = decomposition()

pr.load()
st.write(pr.headDF())
st.write(pr.shapeDF())
st.write(pr.infoDF())
st.write(pr.describeDF())

fig, ax = plt.subplots(nrows=4,ncols=2,figsize = (50,50))
for i,ax in enumerate(ax.flatten()):
    ax.set_title(pr.df.columns[i])
    ax.hist(pr.df[pr.df.columns[i]],20)
st.pyplot(fig)

st.bar_chart(pr.getLabelSeries())
st.write(pr.corrDF())

pca = d.Pca(pr.getDataWithoutLabels())
st.scatter_chart(pd.DataFrame(pca,columns=["x","y"]))




