import pandas as pd
import matplotlib.pyplot as plt
import functools
import numpy as np
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit

labour_force_age = 'D:/Data Science Projects/Malaysia Statistics/04.Labour force by age group.xlsx'
labour_force_ethnic = 'D:/Data Science Projects/Malaysia Statistics/05.Labour force by ethnic group.xlsx'
labour_force_edu = 'D:/Data Science Projects/Malaysia Statistics/06.Labour force by educational attainment.xlsx'
labour_force_cert = 'D:/Data Science Projects/Malaysia Statistics/07.Labour force by highest certificate obtained.xls'
labour_force_marital = 'D:/Data Science Projects/Malaysia Statistics/08.Labour force by marital status.xls'
employed_age = 'D:/Data Science Projects/Malaysia Statistics/09.Employed persons by age group.xls'
employed_ethnic = 'D:/Data Science Projects/Malaysia Statistics/10.Employed persons by ethnic group.xls'
employed_edu = 'D:/Data Science Projects/Malaysia Statistics/14.Employed persons by educational attainment.xls'
employed_cert = 'D:/Data Science Projects/Malaysia Statistics/15.Employed persons by highest certificate obtained.xls'
employed_marital = 'D:/Data Science Projects/Malaysia Statistics/16.Employed persons by marital status.xls'

df_labour_force_age = pd.read_excel(labour_force_age, sheet_name = 0)
df_labour_force_ethnic = pd.read_excel(labour_force_ethnic, sheet_name = 0)
df_labour_force_edu = pd.read_excel(labour_force_edu, sheet_name = 0)
df_labour_force_cert = pd.read_excel(labour_force_cert, sheet_name = 0)
df_labour_force_marital = pd.read_excel(labour_force_marital, sheet_name = 0)
df_employed_age = pd.read_excel(employed_age, sheet_name = 0)
df_employed_ethnic = pd.read_excel(employed_ethnic, sheet_name = 0)
df_employed_edu = pd.read_excel(employed_edu, sheet_name = 0)
df_employed_cert = pd.read_excel(employed_cert, sheet_name = 0)
df_employed_marital = pd.read_excel(employed_marital, sheet_name = 0)

df_labour_force_ethnic.rename(columns={'Total.1': 'Total citizens'}, inplace = True)
df_employed_ethnic.rename(columns={'Total.1': 'Total citizens'}, inplace= True)
df_labour_force_cert.replace('-',np.NaN, regex=True, inplace= True)
df_employed_cert.replace('-',np.NaN, regex=True, inplace= True)

df_unemployed_age = df_labour_force_age.set_index('Year').subtract(df_employed_age.set_index('Year'), fill_value=0)
df_unemployed_ethnic = df_labour_force_ethnic.set_index('Year').subtract(df_employed_ethnic.set_index('Year'), fill_value=0)
df_unemployed_edu = df_labour_force_edu.set_index('Year').subtract(df_employed_edu.set_index('Year'), fill_value=0)
df_unemployed_cert = df_labour_force_cert.set_index('Year').subtract(df_employed_cert.set_index('Year'), fill_value=0)
df_unemployed_marital = df_labour_force_marital.set_index('Year').subtract(df_employed_marital.set_index('Year'), fill_value=0)

total_unemployment_breakdown_by_age_range = px.pie(pd.melt(df_unemployed_age.iloc[-1:, 1:11]),
                                        title='Total Unemployment Breakdown by Age Range 2020',
                                        values='value',
                                        names='variable'
                                        )

st.plotly_chart(total_unemployment_breakdown_by_age_range)

total_unemployment_by_age_range = px.bar(pd.melt(df_unemployed_age.iloc[-1:,1:]),
                                        title='Total of Unemployment by Age Range in 2020',
                                        y='value',
                                        x='variable',
                                        labels={'value' : 'Total of Unemployment (thousands)', 'variable' : 'Age Range'}, 
                                        color='variable',
                                        text_auto=True, width=1000
                                        )

st.plotly_chart(total_unemployment_by_age_range)

total_unemployment_breakdown_by_ethnics = px.pie(pd.melt(df_unemployed_ethnic.iloc[-1:,2:7]),
                                        title='Total Unemployment Breakdown by Ethnics 2020',
                                        values='value',
                                        names='variable'
                                        )

st.plotly_chart(total_unemployment_breakdown_by_ethnics)

total_unemployment_by_ethnics = px.bar(pd.melt(df_unemployed_ethnic.iloc[-1:,2:6]),
                                        title='Total of Unemployment by Ethnics in 2020',
                                        y='value',
                                        x='variable',
                                        labels={'value' : 'Total of Unemployment (thousands)', 'variable' : 'Ethnics'}, 
                                        color='variable',
                                        text_auto=True, width=1000
                                        )

st.plotly_chart(total_unemployment_by_ethnics)

total_unemployment_breakdown_by_education = px.pie(pd.melt(df_unemployed_edu.iloc[-1:,1:5]),
                                        title='Total Unemployment Breakdown by Education 2020',
                                        values='value',
                                        names='variable'
                                        )

st.plotly_chart(total_unemployment_breakdown_by_education)

total_unemployment_by_education = px.bar(pd.melt(df_unemployed_edu.iloc[-1:,1:5]),
                                        title='Total of Unemployment by Education in 2020',
                                        y='value',
                                        x='variable',
                                        labels={'value' : 'Total of Unemployment (thousands)', 'variable' : 'Education'}, 
                                        color='variable',
                                        text_auto=True, width=1000
                                        )

st.plotly_chart(total_unemployment_by_education)

df_unemployed_cert.iloc[-1:,1:]

total_unemployment_breakdown_by_certification = px.pie(pd.melt(df_unemployed_cert.iloc[-1:,1:]),
                                        title='Total Unemployment Breakdown by Certification 2020',
                                        values='value',
                                        names='variable'
                                        )

st.plotly_chart(total_unemployment_breakdown_by_certification)

total_unemployment_by_certification = px.bar(pd.melt(df_unemployed_cert.loc[2020:, df_unemployed_cert.columns != 'Total']),
                                        title='Total of Unemployment by Certification in 2020',
                                        y='value',
                                        x='variable',
                                        labels={'value' : 'Total of Unemployment (thousands)', 'variable' : 'Certification'}, 
                                        color='variable',
                                        text_auto=True, width=1000
                                        )

st.plotly_chart(total_unemployment_by_certification)