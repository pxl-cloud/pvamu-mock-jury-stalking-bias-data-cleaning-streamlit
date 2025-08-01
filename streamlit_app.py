import streamlit as st


information = st.Page(
    "case-study/information.py",
    title="Information",
    icon=":material/info:",
    default=True
)
data = st.Page(
    "case-study/data.py",
    title="Data",
    icon=":material/table:"
)
hypothesis_1 = st.Page(
    "experiment/hypothesis-1.py",
    title="Hypothesis 1",
    icon=":material/psychology_alt:"
)
hypothesis_2 = st.Page(
    "experiment/hypothesis-2.py",
    title="Hypothesis 2",
    icon=":material/psychology_alt:"
)
hypothesis_3 = st.Page(
    "experiment/hypothesis-3.py",
    title="Hypothesis 3",
    icon=":material/psychology_alt:"
)
hypothesis_4 = st.Page(
    "experiment/hypothesis-4.py",
    title="Hypothesis 4",
    icon=":material/psychology_alt:"
)

pg = st.navigation(
    {
        "Case Study": [information, data],
        "Experiment": [hypothesis_1, hypothesis_2, hypothesis_3, hypothesis_4],
    }
)


st.set_page_config(initial_sidebar_state="collapsed")  # Or "expanded"

st.markdown(
    """
    <style>
    [data-testid="collapsedControl"] {
        display: none
    }
    </style>
    """,
    unsafe_allow_html=True,
)

pg.run()
