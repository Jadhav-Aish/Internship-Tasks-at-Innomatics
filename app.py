import streamlit as st
import google.generativeai as genai

# Load the API key from the file
with open(r"C:\Users\jadha\Generative AI\GCP\Code Reviewer Key.txt") as f:
    key = f.read().strip()

# Configure your API key
genai.configure(api_key=key)


# Set Streamlit page configuration
st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
        /* Background styling */
.stApp {
     background-color: skyblue; /* Sky blue background */
    color: black; /* Black text for good contrast */

/* Title styling */
.title {
    font-size: 2.5em;
    font-weight: bold;
    color: #ffffff; /* White for contrast against the dark background */
    text-shadow: 2px 2px 5px #000; /* Subtle shadow for depth */
    margin-bottom: 10px;
}

/* Text area styling */
textarea {
    background: rgba(255, 255, 255, 0.8) !important; /* Slightly transparent white */
    border: 1px solid #ddd !important; /* Light gray border */
    color: #000 !important; /* Black text */
    border-radius: 5px !important; /* Rounded corners */
    font-size: 16px !important; /* Standard font size */
}

/* Button styling */
button[kind="primary"] {
    background-color: #28a745 !important; /* Green button */
    color: white !important; /* White text */
    border-radius: 8px !important; /* Rounded corners */
    font-size: 18px !important; /* Slightly larger font */
    padding: 10px 20px !important; /* Padding for size */
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Subtle shadow */
}

/* Subheader styling */
.stMarkdown h2 {
    color: #ffffff; /* White text */
    text-shadow: 1px 1px 2px #000; /* Shadow for readability */
}
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar
st.sidebar.title("AI Code Reviewer Features")
st.sidebar.write("🐛 Potential Bugs")
st.sidebar.write("💡 Suggested Improvements")
st.sidebar.write("✨ Improved Code")

st.sidebar.markdown("---")
st.sidebar.write("📌 **Take the time to review your code for improvements**.")

# Title
st.markdown('<div class="title">AI Code Reviewer 🤖</div>', unsafe_allow_html=True)

# Description
st.write("Welcome to the **AI Code Reviewer**! Paste your Python code below, and let the AI help you identify bugs and provide useful feedback.")

# Input for the human prompt
human_code = st.text_area("📝 Enter Your Code")

# Button to trigger code review
if st.button("Review Code"):
    if human_code:
        # Initialize the generative model
        genai.configure(api_key=key)
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        
        # Send the user code for review
        chatbot = model.start_chat(history=[])
        response = chatbot.send_message(f"Review the following Python code and identify any bugs:\n{human_code}")
        #response = chatbot.send_message(f"Review the following Java code and identify any bugs:\n{human_code}")
        # Display the AI-generated response
        st.subheader("🧐 Code Review")
        st.markdown("**Bug Report:**")
        st.write(response.text)  # Display AI response
    else:
        st.error("❌ Please enter some code before generating the review!")

# Footer
st.markdown("---")

