import streamlit as st
import slutils

config = slutils.load_config()

st.set_page_config(
    page_title="Information",
    page_icon=":material/info:",
    layout="wide",
)

st.markdown("# :material/info: Information")

st.write("This is the information page")

st.write(config["app"]["title"])

# Accessing a specific key within the nested table
st.write("---")
st.subheader("Accessing 'sales_data'")
sales_data_endpoint = st.secrets["api"]["endpoints"]["sales_data"]
st.code(f"st.secrets['api']['endpoints']['sales_data'] -> '{sales_data_endpoint}'")