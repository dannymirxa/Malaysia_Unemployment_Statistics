from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt
import functools
import numpy as np
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit

directory = 'D:/Data Science Projects/Malaysia Statistics/Excel Files/01.Principal_Statistics.xlsx'

df_malaysia = pd.read_excel(directory, sheet_name=0)
df_johor = pd.read_excel(directory, sheet_name=1)
df_kedah = pd.read_excel(directory, sheet_name=2)
df_kelantan = pd.read_excel(directory, sheet_name=3)
df_melaka = pd.read_excel(directory, sheet_name=4)
df_nsembilan = pd.read_excel(directory, sheet_name=5)
df_pahang = pd.read_excel(directory, sheet_name=6)
df_ppinang = pd.read_excel(directory, sheet_name=7)
df_perak = pd.read_excel(directory, sheet_name=8)
df_perlis = pd.read_excel(directory, sheet_name=9)
df_selangor = pd.read_excel(directory, sheet_name=10)
df_terangganu = pd.read_excel(directory, sheet_name=11)
df_sabah = pd.read_excel(directory, sheet_name=12)
df_sarawak = pd.read_excel(directory, sheet_name=13)
df_kl = pd.read_excel(directory, sheet_name=14)
df_labuan = pd.read_excel(directory, sheet_name=15)
df_putrajaya = pd.read_excel(directory, sheet_name=16)

#st.set_page_config(page_title="Pricipal Analysis of Unemployment in Malaysia", page_icon=":bar_chart:", layout="wide")

totalunemployment = px.line(df_malaysia[['Year','Unemployed']],
                                        x='Year',
                                        y='Unemployed',
                                        title='Total of Unemployment in Malaysia 1982 to 2020',
                                        labels={'Unemployed' : 'Total of Unemployment (thousands)'},
                                        width=1000
                                        )



unemploymentrate = px.line(df_malaysia[['Year','Unemployment rate']],
                                        x='Year',
                                        y='Unemployment rate',
                                        title='Rate of Unemployment in Malaysia 1982 to 2020',
                                        labels={'Unemployment rate' : 'Unemployment Rate (%)'},
                                        width=1000
                                        )



dfs = [df_johor[['Year', 'Unemployed']],
df_kedah[['Year', 'Unemployed']],
df_kelantan[['Year', 'Unemployed']],
df_melaka[['Year', 'Unemployed']],
df_nsembilan[['Year', 'Unemployed']],
df_pahang[['Year', 'Unemployed']],
df_ppinang[['Year', 'Unemployed']],
df_perak[['Year', 'Unemployed']],
df_perlis[['Year', 'Unemployed']],
df_selangor[['Year', 'Unemployed']],
df_terangganu[['Year', 'Unemployed']],
df_sabah[['Year', 'Unemployed']],
df_sarawak[['Year', 'Unemployed']],
df_kl[['Year', 'Unemployed']],
df_labuan[['Year', 'Unemployed']],
df_putrajaya[['Year', 'Unemployed']]
]

df_unemployed_by_states = functools.reduce(lambda left,right: pd.merge(left, right, on='Year', how='outer',), dfs)
df_unemployed_by_states.columns = ['Year',
'Johor',
'Kedah',
'Kelantan',
'Melaka',
'NSembilan',
'Pahang',
'PPinang',
'Perak',
'Perlis',
'Selangor',
'Terangganu',
'Sabah',
'Sarawak',
'KL',
'Labuan',
'Putrajaya'
]

totalemploymentbystates = px.line(pd.melt(df_unemployed_by_states, id_vars =['Year']),
                                        x='Year',
                                        y='value',
                                        title='Rate of Unemployment in Malaysia 1982 to 2020',
                                        labels={'value' : 'Total of Unemployment (thousands)', 'variable' : 'States'}, 
                                        color='variable',
                                        width=1000
                                        )



total_unemployment_breakdown_by_states = px.pie(pd.melt(df_unemployed_by_states.iloc[-1:,1:]),
                                        title='Total Unemployment Breakdown by States 2020',
                                        values='value',
                                        names='variable',
                                        width=1000
                                        )



total_unemployment_by_states = px.bar(pd.melt(df_unemployed_by_states.iloc[-1:,1:]),
                                        title='Total Unemployment by States 2020',
                                        y='value',
                                        x='variable',
                                        labels={'value' : 'Total of Unemployment (thousands)', 'variable' : 'States'}, 
                                        color='variable',
                                        width=1000
                                        )



dfs_unemployment_rate = [df_johor[['Year', 'Unemployment rate']],
df_kedah[['Year', 'Unemployment rate']],
df_kelantan[['Year', 'Unemployment rate']],
df_melaka[['Year', 'Unemployment rate']],
df_nsembilan[['Year', 'Unemployment rate']],
df_pahang[['Year', 'Unemployment rate']],
df_ppinang[['Year', 'Unemployment rate']],
df_perak[['Year', 'Unemployment rate']],
df_perlis[['Year', 'Unemployment rate']],
df_selangor[['Year', 'Unemployment rate']],
df_terangganu[['Year', 'Unemployment rate']],
df_sabah[['Year', 'Unemployment rate']],
df_sarawak[['Year', 'Unemployment rate']],
df_kl[['Year', 'Unemployment rate']],
df_labuan[['Year', 'Unemployment rate']],
df_putrajaya[['Year', 'Unemployment rate']]
]

df_unemployment_rate_by_states = functools.reduce(lambda left,right: pd.merge(left, right, on='Year', how='outer',), dfs_unemployment_rate)
df_unemployment_rate_by_states.columns = ['Year',
'Johor',
'Kedah',
'Kelantan',
'Melaka',
'NSembilan',
'Pahang',
'PPinang',
'Perak',
'Perlis',
'Selangor',
'Terangganu',
'Sabah',
'Sarawak',
'KL',
'Labuan',
'Putrajaya'
]

rate_unemployment_by_states = px.bar(pd.melt(df_unemployment_rate_by_states.iloc[-1:,1:]),
                                        title='Rate of Unemployment by States 2020',
                                        y='value',
                                        x='variable',
                                        labels={'value' : 'Rate of Unemployment (%)', 'variable' : 'States'}, 
                                        color='variable',
                                        width=1000
                                        )





rate_employment_by_states = px.line(pd.melt(df_unemployment_rate_by_states, id_vars = 'Year'),
                                        x='Year',
                                        y='value',
                                        title='Rate of Unemployment in Malaysia 1982 to 2020 by States',
                                        labels={'value' : 'Rate of Unemployment (%)', 'variable' : 'States'}, 
                                        color='variable',
                                        width=1000
                                        )



def app():
    st.title('Pricipal Analysis of Unemployment in Malaysia')

    st.plotly_chart(totalunemployment)

    st.plotly_chart(unemploymentrate)

    st.plotly_chart(totalemploymentbystates)

    st.plotly_chart(total_unemployment_breakdown_by_states)

    st.plotly_chart(total_unemployment_by_states)

    st.plotly_chart(rate_unemployment_by_states)

    st.plotly_chart(rate_employment_by_states)
