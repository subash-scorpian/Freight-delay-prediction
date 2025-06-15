import streamlit as st
import pandas as pd
import joblib

# Load model and feature columns 
model = joblib.load("freight_delay_model.pkl")
feature_cols = joblib.load("model_features.pkl")

st.title("🚛 Freight Delay Prediction App")
st.markdown("Upload a CSV file with shipment details and predict if shipments will be **Delayed** or **On-Time**.")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    input_df = pd.read_csv(uploaded_file)

    # Preprocess input
    try:
        df_input = input_df.drop(columns=['shipment_id', 'shipment_date'])
    except:
        st.error("Make sure 'shipment_id' and 'shipment_date' are included in the file.")

    df_input_encoded = pd.get_dummies(df_input, drop_first=True)

    # Align columns
    missing_cols = set(feature_cols) - set(df_input_encoded.columns)
    for col in missing_cols:
        df_input_encoded[col] = 0
    df_input_encoded = df_input_encoded[feature_cols]

    # Predict
    predictions = model.predict(df_input_encoded)
    input_df['Predicted Delay'] = predictions
    input_df['Predicted Delay'] = input_df['Predicted Delay'].map({1: 'Delayed', 0: 'On-Time'})

    st.success("✅ Predictions completed!")
    st.dataframe(input_df)

    # Download
    csv = input_df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Results CSV", data=csv, file_name="freight_predictions.csv", mime="text/csv")
