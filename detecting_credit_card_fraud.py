import streamlit as st
import joblib

# load the model
model = joblib.load('credit_card_model')

def predict_fraud(values):
    prediction = model.predict([values])
    return "Normal Transaction" if prediction == 0 else "Fraud Transaction"

def main():
    st.title("Credit Card Fraud Detection")

    # define the button and its functionality at the top
    predict_button = st.empty()  
    result_placeholder = st.empty()

    inputs = []

    inputs_per_row = 5
    num_rows = 6  

    for row in range(num_rows):
        cols = st.columns(inputs_per_row)
        for i in range(inputs_per_row):
            index = row * inputs_per_row + i
            if index < 29: 
                with cols[i]:
                    value = st.number_input(f'V{index+1}', format="%.2f", key=index+1)
                    inputs.append(value)

    if predict_button.button('Predict'):
        with st.spinner('Predicting...'):
            result = predict_fraud(inputs)
            # display the result 
            result_placeholder.success(f"**Final Prediction from the model: {result}**")

if __name__ == "__main__":
    main()
