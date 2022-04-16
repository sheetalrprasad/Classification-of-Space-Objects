import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Page setup
st.set_page_config(page_title="Sky Objects", page_icon=":bar_chart:", layout="wide")

skyObj = pd.read_csv('data/Skyserver_SQL4_7_2022 12_58_52 AM.csv',skiprows=1 )

if __name__ == '__main__':
    st.write(skyObj.corr())
    data = skyObj[['u','g','r','i','z','modelFlux_u','modelFlux_g','modelFlux_r','modelFlux_i','modelFlux_z','redshift','plate','fiberid','class']]

    fig, ax = plt.subplots(figsize=(20,10))  
    sns.heatmap(data.corr(), cmap="YlGnBu", linewidths=0.1, annot=True, ax=ax)
    st.write(fig)

    targetCount = data['class'].value_counts()
    st.write(f'Class 0: {targetCount[0]}')
    st.write(f'Class 1: {targetCount[1]}')
    st.write(f'Class 2: {targetCount[2]}')
    st.write(f'Percentage of Majority Class: {round(targetCount[0] / sum(targetCount), 4)*100}')
    st.write(f'Percentage of Minority Class: {round(targetCount[2] / sum(targetCount), 4)*100}')

    fig2, ax = plt.subplots(figsize=(20,10))  
    targetCount.plot(kind='bar', title='Class Count', rot=0)
    st.write(fig2)