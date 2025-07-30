from datetime import date, datetime, timedelta

import pandas as pd
import joblib
import numpy as np
import streamlit as st
from utils.components import render_input_section

import keras

DATA_PATH = 'data/n_telemetry.csv'
MODEL = 'models/LSTM/e3_m70_lstmv3.keras'
reconstructed_model = keras.models.load_model(MODEL)


def demo():
    min_date = date(2015, 1, 1)
    max_date = date(2016, 1, 1)

    st.title("Machine Maintenance prediction")
    st.subheader("Input Parameters")

    selected_date, time,  machine_n = render_input_section(
        min_date=min_date, max_date=max_date
    )


    if selected_date and time and machine_n:
        n_telemetry = pd.read_csv(DATA_PATH)

        n_telemetry['datetime'] = pd.to_datetime(n_telemetry['datetime'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

        date_time = datetime.combine(selected_date, time)

        last_dates = [date_time - timedelta(hours=i) for i in range(1, 6)]

        last_records = n_telemetry[n_telemetry['datetime'].isin(last_dates)]
        if not last_records.empty:

            last_records = last_records[last_records['machineID'] == machine_n]
            last_records = last_records['seconds_to_fail'].to_numpy()
            st.divider()
            y_pred = reconstructed_model.predict(last_records.reshape(1, 5, 1))

            scaler = joblib.load('models/scaler.save')
            temp_array = np.zeros((y_pred.shape[0], scaler.n_features_in_))
            temp_array[:, -1] = y_pred.flatten()

            u_y_pred = scaler.inverse_transform(temp_array)
            seg = int(u_y_pred[-1,-1])
            hours = seg/3600
            days = hours/24
            hours = hours % 24
            seg = seg % 3600

            st.text(f"The machine number {machine_n} will have a failure in {int(days)} days, {int(hours)} hrs and {seg} seg")
        else:
            st.warning(f"⚠️ There's no data from date and hour: {date_time}")
    else:
        st.warning("⚠️ Please select a **Date**, **Hour** and **Number of machine** to begin.")


# if __name__ == "__main__":
#     demo()
