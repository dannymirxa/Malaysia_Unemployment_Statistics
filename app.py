import streamlit as st
from multiapp import MultiApp
from apps import main, Principal_Analysis, Principal_Analysis_by_Sex, Principal_Analysis_by_Strata, Unemployed_Analysis

app = MultiApp()

# st.title("Unemployment Statistics of Malaysia 2020")

st.set_page_config(layout="wide")

st.markdown("""
<style>
.big-font {
    font-size:50px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Unemployment Statistics of Malaysia 2020</p>', unsafe_allow_html=True)

# Add all your application here
app.add_app("Main Page", main.app)
app.add_app("Principal Analysis", Principal_Analysis.app)
app.add_app("Principal Analysis by Sex", Principal_Analysis_by_Sex.app)
app.add_app("Principal_Analysis by Strata", Principal_Analysis_by_Strata.app)
app.add_app("Unemployed Analysis", Unemployed_Analysis.app)
# The main app
app.run()
