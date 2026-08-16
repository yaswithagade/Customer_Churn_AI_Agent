import streamlit as st
import pandas as pd
import joblib

# ---------------------------------------------------
# Load model
# ---------------------------------------------------

model = joblib.load("churn_model.pkl")

# ---------------------------------------------------
# Page configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

st.sidebar.title("📌 About This Project")

st.sidebar.info(
    """
    Final Year Mini Project

    AI-Powered Customer Churn Prediction System

    Machine Learning Model:
    Logistic Regression
    """
)

# ---------------------------------------------------
# Title
# ---------------------------------------------------

st.title("📊 AI-Powered Customer Churn Prediction System")

# ---------------------------------------------------
# Banner image
# ---------------------------------------------------

st.image(
    "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9",
    use_container_width=True
)

# ---------------------------------------------------
# Description
# ---------------------------------------------------

st.info(
    """
    This application predicts whether a telecom customer is likely to leave the company based on customer demographics, services, and billing information.
    """
)

# ---------------------------------------------------
# Input section
# ---------------------------------------------------

col1, col2 = st.columns(2)

# Left column

with col1:

    st.subheader("👤 Customer Information")

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    senior = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    tenure = st.slider(
        "Tenure (Months)",
        0,
        72,
        12
    )

    partner = st.checkbox("Partner")

    dependents = st.checkbox("Dependents")

    monthly = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        max_value=200.0,
        value=50.0
    )

    total = st.number_input(
        "Total Charges",
        min_value=0.0,
        max_value=10000.0,
        value=1000.0
    )

# Right column

with col2:

    st.subheader("📞 Service Information")

    phone = st.checkbox("Phone Service")

    multiple = st.selectbox(
        "Multiple Lines",
        ["No", "Yes", "No phone service"]
    )

    internet = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    security = st.selectbox(
        "Online Security",
        ["No", "Yes", "No internet service"]
    )

    backup = st.selectbox(
        "Online Backup",
        ["No", "Yes", "No internet service"]
    )

    device = st.selectbox(
        "Device Protection",
        ["No", "Yes", "No internet service"]
    )

    support = st.selectbox(
        "Tech Support",
        ["No", "Yes", "No internet service"]
    )

    tv = st.selectbox(
        "Streaming TV",
        ["No", "Yes", "No internet service"]
    )

    movies = st.selectbox(
        "Streaming Movies",
        ["No", "Yes", "No internet service"]
    )

    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

    paperless = st.checkbox(
        "Paperless Billing"
    )

    payment = st.selectbox(
        "Payment Method",
        [
            "Bank transfer",
            "Credit card (automatic)",
            "Electronic check",
            "Mailed check"
        ]
    )

# ---------------------------------------------------
# Prediction
# ---------------------------------------------------

if st.button("🔍 Predict"):

    data = {

        "gender": 1 if gender == "Male" else 0,
        "SeniorCitizen": senior,
        "tenure": tenure,
        "MonthlyCharges": monthly,
        "TotalCharges": total,
        "Partner_Yes": int(partner),
        "Dependents_Yes": int(dependents),
        "PhoneService_Yes": int(phone),
        "MultipleLines_No phone service": int(
            multiple == "No phone service"
        ),
        "MultipleLines_Yes": int(
            multiple == "Yes"
        ),
        "InternetService_Fiber optic": int(
            internet == "Fiber optic"
        ),
        "InternetService_No": int(
            internet == "No"
        ),
        "OnlineSecurity_No internet service": int(
            security == "No internet service"
        ),
        "OnlineSecurity_Yes": int(
            security == "Yes"
        ),
        "OnlineBackup_No internet service": int(
            backup == "No internet service"
        ),
        "OnlineBackup_Yes": int(
            backup == "Yes"
        ),
        "DeviceProtection_No internet service": int(
            device == "No internet service"
        ),
        "DeviceProtection_Yes": int(
            device == "Yes"
        ),
        "TechSupport_No internet service": int(
            support == "No internet service"
        ),
        "TechSupport_Yes": int(
            support == "Yes"
        ),
        "StreamingTV_No internet service": int(
            tv == "No internet service"
        ),
        "StreamingTV_Yes": int(
            tv == "Yes"
        ),
        "StreamingMovies_No internet service": int(
            movies == "No internet service"
        ),
        "StreamingMovies_Yes": int(
            movies == "Yes"
        ),
        "Contract_One year": int(
            contract == "One year"
        ),
        "Contract_Two year": int(
            contract == "Two year"
        ),
        "PaperlessBilling_Yes": int(
            paperless
        ),
        "PaymentMethod_Credit card (automatic)": int(
            payment == "Credit card (automatic)"
        ),
        "PaymentMethod_Electronic check": int(
            payment == "Electronic check"
        ),
        "PaymentMethod_Mailed check": int(
            payment == "Mailed check"
        )
    }

    df = pd.DataFrame([data])

    prediction = model.predict(df)

    st.markdown("---")

    if prediction[0] == 1:

        st.error("⚠️ Customer is likely to churn.")

    else:

        st.success("✅ Customer is likely to stay.")

# ---------------------------------------------------
# Footer
# ---------------------------------------------------

st.markdown("---")

st.subheader("🛠️ Technologies Used")

st.write("• Python")
st.write("• Streamlit")
st.write("• Pandas")
st.write("• Scikit-learn")
st.write("• Machine Learning")
st.write("• Logistic Regression")