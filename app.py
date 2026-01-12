import streamlit as st
import pickle
import pandas as pd

# Title of the page
st.set_page_config(
    page_title="Mall Customer Segmentation", page_icon="📊", layout="centered"
)

# Load the pre-trained K-Means model
kmeans = pickle.load(open("./model/kmeans.pkl", "rb"))
# dbscan = pickle.load(open("./model/dbscan.pkl", "rb"))

cluster_descriptions = {
    0: "Cluster 0: Customers with low annual income and low annual spend",
    1: "Cluster 1: Customers with high annual income and high annual spend",
    2: "Cluster 2: Customers with low annual income and high annual spend",
    3: "Cluster 3: Customers high annual income but low annual spend ",
}

# Streamlit app
st.title("Mall Customer Segmentation")
st.write("Predict the customer segment based on user input")

# User input
age = st.slider("Enter the age", 18, 70, 25)
annual_income = st.slider("Enter Annual Income in k$", 1, 200, 50)
spending_score = st.slider("Spending Score", 0, 100, 50)

# Predict cluster
if st.button("Predict Cluster"):
    user_data = pd.DataFrame(
        # user_data_scaled = dbscan.transform(user_data)
        [[age, annual_income, spending_score]],
        columns=["Age", "Annual Income (k$)", "Spending Score (1-100)"],
    )
    predicted_cluster = kmeans.predict(user_data)[0]

    # Display prediction
    st.subheader(f"The customer belongs to Cluster-{predicted_cluster}")
    st.write(
        cluster_descriptions.get(predicted_cluster, "Cluster description not available")
    )
