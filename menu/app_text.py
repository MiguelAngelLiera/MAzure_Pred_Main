"""
This file is all of the markdown used throughout the app.
"""

intro = """    
## Problem Statement

In a real-world production environment, it's crucial to know when one of our assets, in this case machines, 
is prone to failure. In this regard, we have several tools to develop an effective solution: various measurements, 
failure logs, and error records. Additionally, we possess diverse data analysis and ML tools. 
Throughout this project, the implementation of an LSTM network to predict the estimated time until a machine experiences a failure will be demonstrated.
"""

app_overview = """
    ## 📑 App Overview

    This project is aimed at creating an analysis and design for an ML solution for predicting the remaining time until a machine has a failure. Use the sidebar to navigate between the following sections:

    ### 📊 Page 1: **Exploratory Data Analysis and Feature Engineering Analysis**
    - Summary statistics
    - Visualizations of key features

     ---

    ### 📈 Page 2: **Model**
    - LSTM-nn architecture to predict time series.

    ---

    ### ⚙️ Page 3: **Production Demo**
    Interactive Production Dashboard Example
    - Select day and hour and a number of machine to get a prediction.

    ---

    ### 🔮 Page 4: **Future Work**
    Some ideas for future development.

    """

eda_intro = r"""## Exploratory Data Analysis 🔎

We'll be working with the **Microsoft Azure Predictive Maintenance dataset** using a computed feature **seconds_to_fail** to get a prediction.
To get done with it, and demonstrate the practical utility of LSTM neural network model at time-series for predictive maintenance, we'll create a model that takes the last five
time values in order to interpolate the 6th data point.
The available data includes:

1. **Telemetry data**: Hourly readings of Voltage, Rotation, Pressure, and Vibration
2. **Errors**: Timestamped logs of error codes (types 1–5)
3. **Maintenance records**: Logs of component replacements (components 1–4), regardless of failure
4. **Failure records**: Logs of component replacements **due to failure**
5. **Machine metadata**: Machine age and model type

> **Note**: For the analisis of all features, all data has been merge into one table to see hourly machine performance.
---
"""

hours_to_fail = """### Hours to fail 

One of the most important pieces of data is how much time remains before a machine experiences a failure. 
Based on this, we will try to analyze which characteristics of each record are useful for generating a time-based prediction. """

heat_text = """
## Correlation Analysis Summary (Heatmap Interpretation)

This correlation heatmap displays the **Pearson correlation matrix** between various machine features, including `age`, `datetime`, `volt`, `rotate`, `pressure`, `vibration`, `errors`, `failures`, `maint`, and the target variable, `seconds_to_fail`. Pearson correlation values range from -1 (perfect negative correlation) to 1 (perfect positive correlation), with 0 indicating no linear correlation.

### Key Observations Regarding `seconds_to_fail` (Time Remaining Until Failure):

* **Weak Negative Correlations with `age` (-0.19) and `datetime` (-0.17):** As the machine `age` or the `datetime` progresses, the `seconds_to_fail` tends to decrease. This is logical: older machines or those further along in their operational timeline are naturally closer to experiencing a failure. The weak strength suggests these factors alone are not dominant predictors.
* **Weak to Moderate Negative Correlations with `errors` (-0.20) and `failures` (-0.22):** These are among the strongest (in absolute terms) linear correlations with our target variable. A higher count of `errors` and the occurrence of `failures` are associated with a reduced `seconds_to_fail`. This aligns with intuition, as errors often precede, and failures directly consume, remaining operational time.
* **Correlation with `maint` (-0.01):** Maintenance (`maint`) shows virtually no linear correlation with `seconds_to_fail`. This could indicate that the recorded maintenance is primarily reactive (post-failure) rather than preventive, or that the current maintenance strategy/data doesn't linearly influence the time until the next failure.
* **Sensor Readings (`volt`, `rotate`, `pressure`, `vibration`) exhibit very low correlations:** These critical sensor characteristics show near-zero linear correlations with `seconds_to_fail`, `errors`, and `failures`.

### Project Implications:

While `failures`, `errors`, `age`, and `datetime` appear to be the most linearly correlated features with `seconds_to_fail`, their correlations are only weak to moderate. The low linear correlation of sensor readings necessitates a deeper investigation into non-linear relationships or advanced feature engineering to fully leverage their potential for accurate time-to-failure prediction.
"""

final_eda_text = """
Due to time and implementation constraints, an LSTM-based neural network was chosen to predict the remaining time before a new failure. This was done by selecting the last five `seconds_to_fail` values to predict the next one. The following section will detail the architecture and some of the experimental results.
"""

model_selection_text = """
As we discussed in the previous session, we will feed the model with the last five time values to predict the next one. In this regard, we have the following network architecture.

## Model creation

### Keras Sequential LSTM Model Description

This is a **Sequential Keras model** designed for **time series prediction** (predicting a single value, the seconds to fail metric). It leverages a **stacked Long Short-Term Memory (LSTM)** architecture, which is highly effective for learning patterns and dependencies in sequential data.

---

## Model Architecture Breakdown

### 1. `Sequential` Model

The model is constructed using Keras's `Sequential` API, meaning that layers are added one after another in a linear stack. This approach provides a straightforward and common method for building neural networks.

### 2. Stacked LSTM Layers

* **First LSTM Layer:**
    * `LSTM(15, activation='tanh', return_sequences=True, input_shape=(5,1))`
    * This is the initial LSTM layer, featuring **15 memory units (neurons)**.
    * It employs the **hyperbolic tangent (`tanh`) activation function**.

* **Second LSTM Layer:**
    * `LSTM(10, activation='tanh')`
    * This is the second LSTM layer, which receives the sequential output from the first LSTM layer as its input. It comprises **10 memory units**.
    * It also utilizes the `tanh` activation function.

### 3. `Dropout` Layer

* `Dropout(0.2)`
* This layer serves as a **regularization technique**.

### 4. `Dense` Output Layer

* `Dense(1)`
* This is a standard **fully connected layer** containing **1 neuron**. This single neuron typically generates the ultimate predicted value.
"""

future_text = """
One of the project's details that immediately stands out is why some other features weren't chosen to feed the model. This is precisely the future work.
It's possible to add feature engineering for continuous values such as voltage or pressure to obtain better correlations for prediction. Furthermore, 
it's feasible to implement a classification model not only to get the remaining time before a failure, 
but also to identify which components will be the next most likely to fail. There's significant room for data treatment and analysis, 
so it's undeniable that this project still has valuable work left to be done.
"""

model_final_text = """
The model was trained for 3 epochs with 70 machines for training (the approach chosen was to use each machine as a batch). Under these parameters, an MSE of 0.000017 was obtained for the normalized data. Below is an example of the prediction for machine number 99.
"""
