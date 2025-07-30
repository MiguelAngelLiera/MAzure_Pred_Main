from menu.app_text import eda_intro, hours_to_fail, heat_text, final_eda_text
import streamlit as st


def eda():
    st.markdown(eda_intro)
    st.markdown(hours_to_fail)
    st.markdown(heat_text)
    st.image('images/feat_heat_map.png', caption="Heatmap correlation between features", use_container_width=True)
    st.markdown(final_eda_text)


# if __name__ == "__main__":
#     eda()
