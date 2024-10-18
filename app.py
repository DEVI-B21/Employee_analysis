import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model_filename = 'employee_performance_model.pkl'

# Set a custom style for the app, including background image and left-aligned input fields
st.markdown(
    """
    <style>
    /* Set background for the main content */
    .stApp {
        background-image: url('https://www.shutterstock.com/image-photo/taregt-customer-concept-performance-appraisal-600nw-2224682725.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }
    /* Style for header with icon and title */
    .header {
        display: flex;
        justify-content: flex-start;
        align-items: center;
        margin-bottom: 20px;
        margin-left: 20px;
    }
    .header img {
        margin-right: 20px;
    }
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #000000;
    }
    /* Left-align input fields */
    .stInput {
        display: flex;
        flex-direction: column;
        margin-left: 20px;
    }
    /* Input labels */
    .input-label {
        font-size: 18px;
        color: #1E90FF;
    }
    /* Button styles */
    .stButton>button {
        background-color: #2E8B57;
        color: white;
        font-size: 18px;
        margin-left: 20px;
    }
    /* Success message styles */
    .stSuccess {
        color: #32CD32;
        font-weight: bold;
        margin-left: 20px;
    }
    /* Style to make input fields bold and larger font size */
    div[data-baseweb="input"] input {
        font-size: 20px !important;  /* Increase font size */
        font-weight: bold !important;  /* Make text bold */
    }
    /* Style for input labels to make them bold */
    .stLabel {
        font-size: 20px !important;
        font-weight: bold;
        color: #1E90FF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Try to load the model and handle any potential loading errors
try:
    model = joblib.load(model_filename)
except FileNotFoundError:
    st.error(f"Model file '{model_filename}' not found. Please ensure the model is saved correctly.")
    st.stop()

# Display an employee icon and the title aligned to the left
st.markdown(
    """
    <div class="header">
        <img src="https://cdn.iconscout.com/icon/premium/png-256-thumb/employee-performance-evaluation-5904760-4958446.png?f=webp&w=256" width="80">
        <div class="title">Employee Performance Prediction</div>
    </div>
    """, 
    unsafe_allow_html=True
)

# Input fields for employee data with unique keys, left-aligned and bold
tasks_completed = st.number_input('Tasks Completed', min_value=0, key='tasks_completed')

task_completion_rate = st.number_input('Task Completion Rate (%)', min_value=0, max_value=100, key='task_completion_rate')

attendance_rate = st.number_input('Attendance Rate (%)', min_value=0, max_value=100, key='attendance_rate')

leaves_taken = st.number_input('Leaves Taken', min_value=0, key='leaves_taken')

training_hours = st.number_input('Training Hours', min_value=0, key='training_hours')

# Validate inputs and predict performance when the user clicks "Predict"
if st.button('Predict Performance'):
    # Check for valid values in all fields except 'Leaves Taken'
    if tasks_completed == 0:
        st.error("Please enter a valid value for Tasks Completed.")
    elif task_completion_rate == 0:
        st.error("Please enter a valid value for Task Completion Rate.")
    elif attendance_rate == 0:
        st.error("Please enter a valid value for Attendance Rate.")
    elif training_hours == 0:
        st.error("Please enter a valid value for Training Hours.")
    else:
        # Create a DataFrame for the input data
        input_data = {
            'Tasks Completed': [tasks_completed],
            'Task Completion Rate (%)': [task_completion_rate],
            'Attendance Rate (%)': [attendance_rate],
            'Leaves Taken': [leaves_taken],  # Can be 0
            'Training Hours': [training_hours]
        }

        input_df = pd.DataFrame(input_data)
        
        # Predict the performance and display the result
        try:
            prediction = model.predict(input_df)
            st.markdown(f'<div class="stSuccess">Predicted Performance Score: {round(prediction[0], 2)}%</div>', unsafe_allow_html=True)
        except AttributeError as e:
            st.error(f"Error in prediction: {e}")
            st.stop()