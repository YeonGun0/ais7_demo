import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import plotly.express as px

st.set_page_config(
    page_title="Likelion AI School 자동차 연비 App",
    page_icon="🚗",
    layout="wide",
)

st.markdown("# 자동차 연비 🚗")
st.sidebar.markdown("# 자동차 연비 🚗")

url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv'


@st.cache
def load_data(nrows):
    data = pd.read_csv(url, nrows=nrows)
    return data

data_load_state = st.text('Loading data...')
data = load_data(100000000)
data_load_state.text("Done! (using st.cache)")


st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year',
   list(reversed(range(data.model_year.min(),data.model_year.max())))
   )

# Sidebar - origin
sorted_unique_origin = sorted(data.origin.unique())
selected_origin = st.sidebar.multiselect('origin', sorted_unique_origin, sorted_unique_origin)

if selected_year > 0 :
   data = data[data.model_year == selected_year]

if len(selected_origin) > 0:
   data = data[data.origin.isin(selected_origin)]

st.dataframe(data)

st.line_chart(data["mpg"])

st.bar_chart(data["mpg"])

fig, ax = plt.subplots()
sns.barplot(data=data, x="origin", y="mpg").set_title("origin 별 자동차 연비")
st.pyplot(fig)

fig, ax = plt.subplots()
sns.countplot(data=data, x='origin').set_title("지역별 자동차 연비 데이터 수")
st.pyplot(fig)

lm = sns.lmplot(data=data, x='weight', y='horsepower', hue='origin', ci=None)
plt.title("지역별 무게와 마력")
st.pyplot(lm)

pxh = px.histogram(data, x='origin')
st.plotly_chart(pxh)

