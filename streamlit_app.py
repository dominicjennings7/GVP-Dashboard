import streamlit as st
import pandas as pd

# -----------------------------------------------------------------------------
import streamlit as st

st.set_page_config(
    page_title="GVP Dashboard",       # This shows in browser tab + link preview
    page_icon=":bar_chart:",           # Emoji or URL to an image
    layout="centered",                 # or 'wide'
    initial_sidebar_state="auto",      # 'expanded' or 'collapsed'
)

# Display the logo
st.image("gvp_logo.JPG", width=700)  # Adjust width as necessary

import streamlit as st

st.set_page_config(
    page_title="GVP Dashboard",
    page_icon=":bar_chart:"
)

# Clickable logo (opens in new tab)
st.markdown(
    """
    <a href="https://www.generationalvp.com" target="_blank">
        <img src="gvp_logo.JPG" width="700"/>
    </a>
    """,
    unsafe_allow_html=True
)

st.title("GVP Dashboard")
# -----------------------------------------------------------------------------
# Useful functions

@st.cache_data
def get_gvp_data():
    """Return wealth gap data for GVP Dashboard."""
    data = {
        'Race/Ethnicity': ['White', 'Hispanic', 'Black', 'Other'],
        '2016': [166000, 20700, 16600, 87900],
        '2019': [188200, 36100, 24100, 74500],
    }
    df = pd.DataFrame(data)
    return df

# Load the data
gvp_df = get_gvp_data()

# -----------------------------------------------------------------------------
# Draw the page

# Title at the top
st.title(':bar_chart: GVP Dashboard')

st.markdown("""
Browse U.S. racial wealth gap data from **2016 to 2019**.

Data Source: [Statista Wealth Gap Chart](https://www.statista.com/chart/30223/wealth-gap-us/)
""")

# -----------------------------------------------------------------------------
# Display the data

st.header('Wealth Gap by Race', divider='gray')

# Melt the dataframe so it's easier to plot
melted = gvp_df.melt(id_vars='Race/Ethnicity', var_name='Year', value_name='Median Wealth (USD)')

# Show bar chart
st.bar_chart(
    data=melted,
    x='Race/Ethnicity',
    y='Median Wealth (USD)',
    color='Year',
)

# -----------------------------------------------------------------------------
# Show data table

st.header('Data Table', divider='gray')

st.dataframe(gvp_df, use_container_width=True)

