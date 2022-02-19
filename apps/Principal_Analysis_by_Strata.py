import pandas as pd
import matplotlib.pyplot as plt
import functools
import numpy as np
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit

#st.set_page_config(page_title="Pricipal Analysis of Unemployment in Malaysia by Strata", page_icon=":bar_chart:", layout="wide")

directory_strata = 'D:/Data Science Projects/Malaysia Statistics/Excel Files/03.Principal statistics of labour force by strata.xlsx'

df_malaysia_u = pd.read_excel(directory_strata, sheet_name = 0)
df_malaysia_r = pd.read_excel(directory_strata, sheet_name = 1)
df_johor_u = pd.read_excel(directory_strata, sheet_name = 2)
df_johor_r = pd.read_excel(directory_strata, sheet_name = 3)
df_kedah_u = pd.read_excel(directory_strata, sheet_name = 4)
df_kedah_r = pd.read_excel(directory_strata, sheet_name = 5)
df_kelantan_u = pd.read_excel(directory_strata, sheet_name = 6)
df_kelantan_r = pd.read_excel(directory_strata, sheet_name = 7)
df_melaka_u = pd.read_excel(directory_strata, sheet_name = 8)
df_melaka_r = pd.read_excel(directory_strata, sheet_name = 9)
df_nsembilan_u = pd.read_excel(directory_strata, sheet_name = 10)
df_nsembilan_r = pd.read_excel(directory_strata, sheet_name = 11)
df_pahang_u = pd.read_excel(directory_strata, sheet_name = 12)
df_pahang_r = pd.read_excel(directory_strata, sheet_name = 13)
df_ppinang_u = pd.read_excel(directory_strata, sheet_name = 14)
df_ppinang_r = pd.read_excel(directory_strata, sheet_name = 15)
df_perak_u = pd.read_excel(directory_strata, sheet_name = 16)
df_perak_r = pd.read_excel(directory_strata, sheet_name = 17)
df_perlis_u = pd.read_excel(directory_strata, sheet_name = 18)
df_perlis_r = pd.read_excel(directory_strata, sheet_name = 19)
df_selangor_u = pd.read_excel(directory_strata, sheet_name = 20)
df_selangor_r = pd.read_excel(directory_strata, sheet_name = 21)
df_terangganu_u = pd.read_excel(directory_strata, sheet_name = 22)
df_terangganu_r = pd.read_excel(directory_strata, sheet_name = 23)
df_sabah_u = pd.read_excel(directory_strata, sheet_name = 24)
df_sabah_r = pd.read_excel(directory_strata, sheet_name = 25)
df_sarawak_u = pd.read_excel(directory_strata, sheet_name = 26)
df_sarawak_r = pd.read_excel(directory_strata, sheet_name = 27)
df_kl_u = pd.read_excel(directory_strata, sheet_name = 28)
df_labuan_u = pd.read_excel(directory_strata, sheet_name = 29)
df_labuan_r = pd.read_excel(directory_strata, sheet_name = 30)
df_putrajaya_u = pd.read_excel(directory_strata, sheet_name = 31)

df_malaysia_unemployed = pd.merge(df_malaysia_u[['Year','Unemployed']], df_malaysia_r[['Year','Unemployed']], how="outer", on='Year')
df_malaysia_unemployed.columns = ['Year','Urban','Rural']

df_johor_unemployed = pd.merge(df_johor_u[['Year','Unemployed']], df_johor_r[['Year','Unemployed']], how="outer", on='Year')
df_johor_unemployed.columns = ['Year','Urban','Rural']

df_kedah_unemployed = pd.merge(df_kedah_u[['Year','Unemployed']], df_kedah_r[['Year','Unemployed']], how="outer", on='Year')
df_kedah_unemployed.columns = ['Year','Urban','Rural']

df_kelantan_unemployed = pd.merge(df_kelantan_u[['Year','Unemployed']], df_kelantan_r[['Year','Unemployed']], how="outer", on='Year')
df_kelantan_unemployed.columns = ['Year','Urban','Rural']

df_melaka_unemployed = pd.merge(df_melaka_u[['Year','Unemployed']], df_melaka_r[['Year','Unemployed']], how="outer", on='Year')
df_melaka_unemployed.columns = ['Year','Urban','Rural']

df_nsembilan_unemployed = pd.merge(df_nsembilan_u[['Year','Unemployed']], df_nsembilan_r[['Year','Unemployed']], how="outer", on='Year')
df_nsembilan_unemployed.columns = ['Year','Urban','Rural']

df_pahang_unemployed = pd.merge(df_pahang_u[['Year','Unemployed']], df_pahang_r[['Year','Unemployed']], how="outer", on='Year')
df_pahang_unemployed.columns = ['Year','Urban','Rural']

df_ppinang_unemployed = pd.merge(df_ppinang_u[['Year','Unemployed']], df_ppinang_r[['Year','Unemployed']], how="outer", on='Year')
df_ppinang_unemployed.columns = ['Year','Urban','Rural']

df_perak_unemployed = pd.merge(df_perak_u[['Year','Unemployed']], df_perak_r[['Year','Unemployed']], how="outer", on='Year')
df_perak_unemployed.columns = ['Year','Urban','Rural']

df_perlis_unemployed = pd.merge(df_perlis_u[['Year','Unemployed']], df_perlis_r[['Year','Unemployed']], how="outer", on='Year')
df_perlis_unemployed.columns = ['Year','Urban','Rural']

df_selangor_unemployed = pd.merge(df_selangor_u[['Year','Unemployed']], df_selangor_r[['Year','Unemployed']], how="outer", on='Year')
df_selangor_unemployed.columns = ['Year','Urban','Rural']

df_terangganu_unemployed = pd.merge(df_terangganu_u[['Year','Unemployed']], df_terangganu_r[['Year','Unemployed']], how="outer", on='Year')
df_terangganu_unemployed.columns = ['Year','Urban','Rural']

df_sabah_unemployed = pd.merge(df_sabah_u[['Year','Unemployed']], df_sabah_r[['Year','Unemployed']], how="outer", on='Year')
df_sabah_unemployed.columns = ['Year','Urban','Rural']

df_sarawak_unemployed = pd.merge(df_sarawak_u[['Year','Unemployed']], df_sarawak_r[['Year','Unemployed']], how="outer", on='Year')
df_sarawak_unemployed.columns = ['Year','Urban','Rural']

df_perlis_unemployed = pd.merge(df_perlis_u[['Year','Unemployed']], df_perlis_r[['Year','Unemployed']], how="outer", on='Year')
df_perlis_unemployed.columns = ['Year','Urban','Rural']

df_kl_unemployed = df_kl_u[['Year','Unemployed']]
df_kl_unemployed.columns = ['Year','Urban']

df_labuan_unemployed = pd.merge(df_labuan_u[['Year','Unemployed']], df_labuan_r[['Year','Unemployed']], how="outer", on='Year')
df_labuan_unemployed.columns = ['Year','Urban','Rural']

df_putrajaya_unemployed = df_putrajaya_u[['Year','Unemployed']]
df_putrajaya_unemployed.columns = ['Year','Urban']

df_malaysia_unemployed_2020 = df_malaysia_unemployed[['Year','Urban','Rural']][df_malaysia_unemployed['Year']==2020]

total_unemployment_breakdown_by_strata = px.pie(pd.melt(df_malaysia_unemployed_2020[['Urban', 'Rural']]),
                                        title='Total Unemployment Breakdown by Strata 2020',
                                        values='value',
                                        names='variable',
                                        width=1000
                                        )



df_unemployed_2020 = pd.concat([df_johor_unemployed[df_johor_unemployed['Year']==2020], 
                             df_kedah_unemployed[df_kedah_unemployed['Year']==2020],
                             df_kelantan_unemployed[df_kelantan_unemployed['Year']==2020],
                             df_melaka_unemployed[df_melaka_unemployed['Year']==2020], 
                             df_nsembilan_unemployed[df_nsembilan_unemployed['Year']==2020], 
                             df_pahang_unemployed[df_pahang_unemployed['Year']==2020],
                             df_ppinang_unemployed[df_ppinang_unemployed['Year']==2020],
                             df_perak_unemployed[df_perlis_unemployed['Year']==2020], 
                             df_selangor_unemployed[df_selangor_unemployed['Year']==2020],
                             df_terangganu_unemployed[df_terangganu_unemployed['Year']==2020],
                             df_sabah_unemployed[df_sabah_unemployed['Year']==2020], 
                             df_sarawak_unemployed[df_sarawak_unemployed['Year']==2020],
                             df_kelantan_unemployed[df_kelantan_unemployed['Year']==2020],
                             df_kl_unemployed[df_kl_unemployed['Year']==2020], 
                             df_labuan_unemployed[df_labuan_unemployed['Year']==2020],
                             df_putrajaya_unemployed[df_putrajaya_unemployed['Year']==2020],
                            ], axis=0)

labels = ['Johor',
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
            'Putrajaya']

df_unemployed_2020['States'] = labels

total_unemployment_by_states = px.bar(pd.melt(df_unemployed_2020, id_vars = ['Year', 'States']),
                                        title='Total of Unemployment by Strata and States in 2020',
                                        y='value',
                                        x='States',
                                        labels={'value' : 'Total of Unemployment (thousands)', 'variable' : 'States'}, 
                                        color='variable',
                                        barmode='group',
                                        text_auto=True, width=1000
                                        )



def app():
    st.title('Pricipal Analysis of Unemployment in Malaysia by Strata')

    st.plotly_chart(total_unemployment_breakdown_by_strata)

    st.plotly_chart(total_unemployment_by_states)