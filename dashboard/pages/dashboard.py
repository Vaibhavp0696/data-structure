import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

st.title("Dashboard")

df = sns.load_dataset("titanic")
st.dataframe(df)

#Gender Filter
gender = st.sidebar.multiselect('Gender',
                                options= df['sex'].unique(),
                                default= df['sex'].unique())

#class filter
pclass = st.sidebar.multiselect('Class',
                                options= df['pclass'].unique(),
                                default= df['pclass'].unique())
#age filter
min_age, max_age = st.sidebar.slider('Age',
                        min_value= int(df['age'].min()),
                        max_value= int(df['age'].max()),
                        value= (int(df['age'].min()), int(df['age'].max())))

filtered_data = df[
    (df['sex'].isin(gender)) &
    (df['pclass'].isin(pclass)) &
    (df['age'] >= min_age) &
    (df['age'] <= max_age)
    ]

#histogram of age distribution
st.subheader("Age Distribution")
fig = px.histogram(filtered_datadashboard, x="age", nbins=20, title="Age Distribution")
st.plotly_chart(fig)

#pie chart of survuval rate by gender

fig = px.pie(df, names='sex',values='survived',title='survival rate by gender',
             color_discrete_sequence=['pink', 'blue'],hole=0.5)
st.plotly_chart(fig)

#passenger count by class

fig = px.bar(df, x='pclass', y='survived', title='Passenger count by class',
             color="class",text_auto=True)
st.plotly_chart(fig)

#survival rate by age

fig = px.line(df.groupby('age')['survived'].mean().reset_index(), x='age',
              y='survived',title='Survival rate by age',markers=True)
st.plotly_chart(fig)