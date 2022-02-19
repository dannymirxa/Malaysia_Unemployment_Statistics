import pandas as pd
import matplotlib.pyplot as plt
import functools
import numpy as np
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit

# st.set_page_config(page_title="Pricipal Analysis of Unemployment in Malaysia by Sex", page_icon=":bar_chart:", layout="wide")

directory_sex = 'D:/Data Science Projects/Malaysia Statistics/Excel Files/02.Principal statistics of labour force by sex.xlsx'

df_malaysia_m = pd.read_excel(directory_sex, sheet_name = 0)
df_malaysia_f = pd.read_excel(directory_sex, sheet_name = 1)
df_johor_m = pd.read_excel(directory_sex, sheet_name = 2)
df_johor_f = pd.read_excel(directory_sex, sheet_name = 3)
df_kedah_m = pd.read_excel(directory_sex, sheet_name = 4)
df_kedah_f = pd.read_excel(directory_sex, sheet_name = 5)
df_kelantan_m = pd.read_excel(directory_sex, sheet_name = 6)
df_kelantan_f = pd.read_excel(directory_sex, sheet_name = 7)
df_melaka_m = pd.read_excel(directory_sex, sheet_name = 8)
df_melaka_f = pd.read_excel(directory_sex, sheet_name = 9)
df_nsembilan_m = pd.read_excel(directory_sex, sheet_name = 10)
df_nsembilan_f = pd.read_excel(directory_sex, sheet_name = 11)
df_pahang_m = pd.read_excel(directory_sex, sheet_name = 12)
df_pahang_f = pd.read_excel(directory_sex, sheet_name = 13)
df_ppinang_m = pd.read_excel(directory_sex, sheet_name = 14)
df_ppinang_f = pd.read_excel(directory_sex, sheet_name = 15)
df_perak_m = pd.read_excel(directory_sex, sheet_name = 16)
df_perak_f = pd.read_excel(directory_sex, sheet_name = 17)
df_perlis_m = pd.read_excel(directory_sex, sheet_name = 18)
df_perlis_f = pd.read_excel(directory_sex, sheet_name = 19)
df_selangor_m = pd.read_excel(directory_sex, sheet_name = 20)
df_selangor_f = pd.read_excel(directory_sex, sheet_name = 21)
df_terangganu_m = pd.read_excel(directory_sex, sheet_name = 22)
df_terangganu_f = pd.read_excel(directory_sex, sheet_name = 23)
df_sabah_m = pd.read_excel(directory_sex, sheet_name = 24)
df_sabah_f = pd.read_excel(directory_sex, sheet_name = 25)
df_sarawak_m = pd.read_excel(directory_sex, sheet_name = 26)
df_sarawak_f = pd.read_excel(directory_sex, sheet_name = 27)
df_kl_m = pd.read_excel(directory_sex, sheet_name = 28)
df_kl_f = pd.read_excel(directory_sex, sheet_name = 29)
df_labuan_m = pd.read_excel(directory_sex, sheet_name = 30)
df_labuan_f = pd.read_excel(directory_sex, sheet_name = 31)
df_putrajaya_m = pd.read_excel(directory_sex, sheet_name = 32)
df_putrajaya_f = pd.read_excel(directory_sex, sheet_name = 33)

df_malaysia_unemployed = pd.merge(df_malaysia_m[['Year','Unemployed']], df_malaysia_f[['Year','Unemployed']], how="outer", on='Year')
df_malaysia_unemployed.columns = ['Year','Male','Female']

df_johor_unemployed = pd.merge(df_johor_m[['Year','Unemployed']], df_johor_f[['Year','Unemployed']], how="outer", on='Year')
df_johor_unemployed.columns = ['Year','Male','Female']

df_kedah_unemployed = pd.merge(df_kedah_m[['Year','Unemployed']], df_kedah_f[['Year','Unemployed']], how="outer", on='Year')
df_kedah_unemployed.columns = ['Year','Male','Female']

df_kelantan_unemployed = pd.merge(df_kelantan_m[['Year','Unemployed']], df_kelantan_f[['Year','Unemployed']], how="outer", on='Year')
df_kelantan_unemployed.columns = ['Year','Male','Female']

df_melaka_unemployed = pd.merge(df_melaka_m[['Year','Unemployed']], df_melaka_f[['Year','Unemployed']], how="outer", on='Year')
df_melaka_unemployed.columns = ['Year','Male','Female']

df_nsembilan_unemployed = pd.merge(df_nsembilan_m[['Year','Unemployed']], df_nsembilan_f[['Year','Unemployed']], how="outer", on='Year')
df_nsembilan_unemployed.columns = ['Year','Male','Female']

df_pahang_unemployed = pd.merge(df_pahang_m[['Year','Unemployed']], df_pahang_f[['Year','Unemployed']], how="outer", on='Year')
df_pahang_unemployed.columns = ['Year','Male','Female']

df_ppinang_unemployed = pd.merge(df_ppinang_m[['Year','Unemployed']], df_ppinang_f[['Year','Unemployed']], how="outer", on='Year')
df_ppinang_unemployed.columns = ['Year','Male','Female']

df_perak_unemployed = pd.merge(df_perak_m[['Year','Unemployed']], df_perak_f[['Year','Unemployed']], how="outer", on='Year')
df_perak_unemployed.columns = ['Year','Male','Female']

df_perlis_unemployed = pd.merge(df_perlis_m[['Year','Unemployed']], df_perlis_f[['Year','Unemployed']], how="outer", on='Year')
df_perlis_unemployed.columns = ['Year','Male','Female']

df_selangor_unemployed = pd.merge(df_selangor_m[['Year','Unemployed']], df_selangor_f[['Year','Unemployed']], how="outer", on='Year')
df_selangor_unemployed.columns = ['Year','Male','Female']

df_terangganu_unemployed = pd.merge(df_terangganu_m[['Year','Unemployed']], df_terangganu_f[['Year','Unemployed']], how="outer", on='Year')
df_terangganu_unemployed.columns = ['Year','Male','Female']

df_sabah_unemployed = pd.merge(df_sabah_m[['Year','Unemployed']], df_sabah_f[['Year','Unemployed']], how="outer", on='Year')
df_sabah_unemployed.columns = ['Year','Male','Female']

df_sarawak_unemployed = pd.merge(df_sarawak_m[['Year','Unemployed']], df_sarawak_f[['Year','Unemployed']], how="outer", on='Year')
df_sarawak_unemployed.columns = ['Year','Male','Female']

df_perlis_unemployed = pd.merge(df_perlis_m[['Year','Unemployed']], df_perlis_f[['Year','Unemployed']], how="outer", on='Year')
df_perlis_unemployed.columns = ['Year','Male','Female']

df_kl_unemployed = pd.merge(df_kl_m[['Year','Unemployed']], df_kl_f[['Year','Unemployed']], how="outer", on='Year')
df_kl_unemployed.columns = ['Year','Male','Female']

df_labuan_unemployed = pd.merge(df_labuan_m[['Year','Unemployed']], df_labuan_f[['Year','Unemployed']], how="outer", on='Year')
df_labuan_unemployed.columns = ['Year','Male','Female']

df_putrajaya_unemployed = pd.merge(df_putrajaya_m[['Year','Unemployed']], df_putrajaya_f[['Year','Unemployed']], how="outer", on='Year')
df_putrajaya_unemployed.columns = ['Year','Male','Female']

df_malaysia_unemployed_2020 = df_malaysia_unemployed[['Year','Male','Female']][df_malaysia_unemployed['Year']==2020]

total_unemployment_breakdown_by_sex = px.pie(pd.melt(df_malaysia_unemployed_2020.iloc[:,1:3]),
                                        title='Total Unemployment Breakdown by Sex 2020',
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

df_unemployed_2020['States'] = ['Johor',
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

total_unemployment_by_states = px.bar(pd.melt(df_unemployed_2020, id_vars = ['Year', 'States']),
                                        title='Total of Unemployment by Genders and States in 2020',
                                        y='value',
                                        x='States',
                                        labels={'value' : 'Total of Unemployment (thousands)', 'variable' : 'States'}, 
                                        color='variable',
                                        barmode='group',
                                        text_auto=True, width=1000
                                        )



def app():
    st.title('Pricipal Analysis of Unemployment in Malaysia by Sex')

    st.plotly_chart(total_unemployment_breakdown_by_sex)

    st.plotly_chart(total_unemployment_by_states)