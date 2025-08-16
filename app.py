import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Load Data from CSV ---
providers_data = pd.read_csv("providers_data.csv")
receivers_data = pd.read_csv("receivers_data.csv")
food_listings_data = pd.read_csv("food_listings_data.csv")
claims_data = pd.read_csv("claims_data.csv")

# Sidebar Menu
st.sidebar.title("📊 Food Wastage Management")
menu = ["Providers", "Receivers", "Food Listings", "Claims", "Analysis"]
choice = st.sidebar.radio("Select Page:", menu)

if choice == "Providers":
    st.subheader("Providers Data")
    st.dataframe(providers_data)

elif choice == "Receivers":
    st.subheader("Receivers Data")
    st.dataframe(receivers_data)

elif choice == "Food Listings":
    st.subheader("Food Listings Data")
    st.dataframe(food_listings_data)

elif choice == "Claims":
    st.subheader("Claims Data")
    st.dataframe(claims_data)

elif choice == "Analysis":
    st.subheader("📊 Analysis Dashboard")

    # KPIs
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Providers", len(providers_data))
    col2.metric("Receivers", len(receivers_data))
    col3.metric("Food Listings", len(food_listings_data))
    col4.metric("Expired Food", len(food_listings_data[food_listings_data["Expiry_Date"] < pd.Timestamp.today().strftime("%Y-%m-%d")]))
    col5.metric("Claims", len(claims_data))

    st.markdown("---")

    # Providers by City
    st.markdown("### 🏙️ Providers by City")
    df1 = providers_data.groupby("City").size().reset_index(name="total_providers")
    st.dataframe(df1)
    fig1, ax1 = plt.subplots()
    ax1.bar(df1["City"], df1["total_providers"], color="skyblue")
    st.pyplot(fig1)

    # Receivers by City
    st.markdown("### 🏙️ Receivers by City")
    df2 = receivers_data.groupby("City").size().reset_index(name="total_receivers")
    st.dataframe(df2)
    fig2, ax2 = plt.subplots()
    ax2.bar(df2["City"], df2["total_receivers"], color="orange")
    st.pyplot(fig2)

    # Claims by Status
    st.markdown("### ✅ Claims by Status")
    df3 = claims_data.groupby("Status").size().reset_index(name="total_claims")
    st.dataframe(df3)
    fig3, ax3 = plt.subplots()
    ax3.pie(df3["total_claims"], labels=df3["Status"], autopct="%1.1f%%")
    st.pyplot(fig3)

    # Food Listings by Meal Type
    st.markdown("### 🍛 Food Listings by Meal Type")
    df4 = food_listings_data.groupby("Meal_Type").size().reset_index(name="total_meals")
    st.dataframe(df4)
    fig4, ax4 = plt.subplots()
    ax4.bar(df4["Meal_Type"], df4["total_meals"], color="green")
    st.pyplot(fig4)

    # Top 5 Providers by Quantity
    st.markdown("### 🏆 Top 5 Providers by Quantity Donated")
    df5 = food_listings_data.groupby("Provider_ID")["Quantity"].sum().reset_index().sort_values(by="Quantity", ascending=False).head(5)
    st.dataframe(df5)
    fig5, ax5 = plt.subplots()
    ax5.bar(df5["Provider_ID"], df5["Quantity"], color="purple")
    st.pyplot(fig5)
