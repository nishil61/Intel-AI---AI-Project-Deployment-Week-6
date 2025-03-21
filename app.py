import streamlit as st
import numpy as np

# App Title
st.markdown("📦 **Delivery Time Prediction App**")

# UI Layout
st.markdown("### 🛍️ Select Product Category")
product_category = st.selectbox("", ["Electronics", "Clothing", "Home & Kitchen", "Books", "Other"])

st.markdown("### 📍 Select Customer Location")
customer_location = st.selectbox("", ["Urban", "Suburban", "Rural"])

st.markdown("### 🚚 Select Shipping Method")
shipping_method = st.selectbox("", ["Standard", "Express", "Same-Day"])

st.markdown("### ⚡ Select Shipping Priority")
shipping_priority = st.selectbox("", ["Normal", "High", "Urgent"])

st.markdown("### 🌤️ Select Weather Condition")
weather = st.selectbox("", ["Sunny", "Rainy", "Snowy", "Stormy"])

# Additional Inputs for Accuracy
st.markdown("### ⚖️ Enter Package Weight (kg)")
weight = st.number_input("Weight", min_value=0.1, max_value=100.0, step=0.1)

st.markdown("### 📏 Select Package Size")
package_size = st.selectbox("", ["Small", "Medium", "Large"])

st.markdown("### 📍 Enter Distance to Destination (km)")
distance = st.number_input("Distance (km)", min_value=1, max_value=5000, step=1)

st.markdown("### 🏢 Is the Product Available in a Nearby Warehouse?")
warehouse_available = st.radio("", ["Yes", "No"])

st.markdown("### 🏠 Select Delivery Type")
delivery_type = st.selectbox("", ["Residential", "Business"])

# Predict Button
if st.button("🚀 Predict Delivery Time"):
    # Base delivery times
    if shipping_method == "Standard":
        base_time = np.random.randint(3, 7)  # 3-7 days
    elif shipping_method == "Express":
        base_time = np.random.randint(2, 4)  # 2-4 days
    elif shipping_method == "Same-Day":
        base_time = 1  # Always 1 day
    
    # Adjustments
    if customer_location == "Rural":
        base_time += 2  # Rural areas take longer
    
    if weather in ["Rainy", "Snowy", "Stormy"]:
        base_time += 1  # Bad weather causes delays
    
    if weight > 10:
        base_time += 1  # Heavy packages take longer
    
    if distance > 1000:
        base_time += 2  # Long distances take longer
    
    if package_size == "Large":
        base_time += 1  # Large packages require extra handling
    
    if warehouse_available == "Yes":
        base_time -= 1  # Nearby warehouses reduce time
    
    if delivery_type == "Business":
        base_time -= 1  # Business addresses are usually faster
    
    # Ensure 'Urgent' never exceeds 2 days
    if shipping_priority == "Urgent":
        base_time = min(base_time, 2)
    
    # Final correction to avoid 0-day delivery
    base_time = max(1, base_time)
    
    st.success(f"📦 Estimated Delivery Time: **{base_time} days**")
