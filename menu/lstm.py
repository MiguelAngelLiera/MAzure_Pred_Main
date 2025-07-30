import streamlit as st
from menu.app_text import model_selection_text, model_final_text


def lstm():
    st.markdown(model_selection_text)
    st.image('images/lstmv3.png', caption="LSTM-nn Architecture", use_container_width=True)
    st.markdown(model_final_text)
    st.image('images/pred.png', caption="An example of seconds_to_fail_prediction", use_container_width=True)

# if __name__ == "__main__":
#     feat_eng()
