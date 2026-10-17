import streamlit as st
import requests

# Set up the API URL (Make sure this matches your FastAPI backend URL)
API_URL = "https://hackathon-idea-tracker.onrender.com/generate"

# Create the two tabs
tab1, tab2 = st.tabs(["🚀 Pitch Generator", "💾 Export Hub"])

# --- TAB 1: YOUR ORIGINAL APP ---
with tab1:
    st.header("Generate Your Next Big Idea")
    topic = st.text_input("Enter a topic (e.g., Finance, EdTech):")
    
    if st.button("Generate & Save AI Pitch"):
        if topic:
            try:
                # Send the request to your FastAPI backend
                response = requests.post(API_URL, json={"topic": topic})
                
                if response.status_code == 200:
                    st.success("Pitch generated successfully!")
                    st.write(response.json())
                else:
                    st.error("Backend error. Is your FastAPI server running?")
            except Exception as e:
                st.error("Could not connect to the backend.")
        else:
            st.warning("Please enter a topic first.")

# --- TAB 2: THE NEW EXPORT FEATURE ---
with tab2:
    st.header("Download Your Pitches")
    st.write("Ready to export your pitch for the judges?")
    
    # Placeholder text for the download button
    ai_pitch_text = "Here is the brilliant AI startup pitch..."
    
    st.download_button(
        label="Download Pitch as .txt",
        data=ai_pitch_text,
        file_name="hackathon_pitch.txt",
        mime="text/plain"
    )