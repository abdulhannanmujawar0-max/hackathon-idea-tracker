import streamlit as st
import requests

# The address of your local FastAPI backend
API_URL = "http://127.0.0.1:8000"

st.title("💡 AI Hackathon Idea Tracker")
st.write("Generate, save, and manage your startup ideas.")

st.divider()

# --- Section 1: Generate Ideas ---
st.subheader("1. Brainstorm with Gemini")
topic = st.text_input("Enter a target industry or topic (e.g., Healthcare, Finance):")

# This creates a clickable button
if st.button("Generate & Save AI Pitch"):
    if topic:
        # Show a loading spinner while waiting for the AI
        with st.spinner("Thinking..."):
            # Send the data to your FastAPI POST route
            response = requests.post(f"{API_URL}/generate", json={"name": topic})
            
            if response.status_code == 200:
                data = response.json()
                st.success("Pitch generated and saved to database!")
                st.info(data["pitch"])
            else:
                st.error("Backend error. Is your FastAPI server running?")
    else:
        st.warning("Please enter a topic first.")

st.divider()

# --- Section 2: View Database ---
st.subheader("2. Your Idea Vault")

# A button to fetch the latest data from the database
if st.button("Load Saved Ideas"):
    response = requests.get(f"{API_URL}/ideas")
    
    if response.status_code == 200:
        data = response.json()
        ideas = data.get("ideas", [])
        
        if len(ideas) == 0:
            st.write("No ideas saved yet.")
        else:
            # Loop through the database rows and display them
            for idea in reversed(ideas): # Show newest first
                st.markdown(f"**ID {idea['id']}**: {idea['title']}")
                st.write("---")
    else:
        st.error("Could not connect to database.")