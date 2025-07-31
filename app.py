import streamlit as st
from menu.demo import demo
from menu.eda import eda
from menu.lstm import lstm
from menu.future import future
from menu.app_text import app_overview


def main():
    st.set_page_config(
        page_title="Predictive Maintenance Model Homepage",
        layout="centered",
        initial_sidebar_state="auto",
    )
    st.title("Azure Machine Predictive Maintenaince")
    st.divider()

    choice = st.sidebar.selectbox("Menu", ['Proyect presentation', 'EDA and Feature Engineering', 'Model', 'Demo', 'Future Work'])
    if choice == "Proyect presentation":
        presentation()
    elif choice == "EDA and Feature Engineering":
        eda()
    elif choice == "Model":
        lstm()
    elif choice == "Demo":
        demo()
    elif choice == "Future Work":
        future()


def presentation():
    st.markdown(app_overview)
    st.image('images/pred_maint.png')


if __name__ == '__main__':
    main()
