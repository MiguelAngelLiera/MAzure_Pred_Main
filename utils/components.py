from datetime import date, timedelta

import streamlit as st


def render_input_section(min_date: date, max_date: date):
    """
    Render the first section of Maintenance_Prioritization_Dashboard

    Returns:
        tuple: (selected_date, top_n, sort_option)
    """
    col1, col2, col3 = st.columns(3)

    with col1:
        selected_date = st.date_input(
            "Select Date:", value=None, min_value=min_date, max_value=max_date
        )

    with col2:
        time = st.time_input(
            "Select Hour", value=None, step=timedelta(minutes=60)
        )

    with col3:
        top_n = st.number_input("Number of machine:", min_value=1, max_value=20, value=10)

    return selected_date, time, top_n
