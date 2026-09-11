import streamlit as st
from chatbot import chatbot_response
from utils import download_nltk_data
# ---------------------------------------
# NLTK SETUP
# ---------------------------------------
download_nltk_data()
# ---------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------

st.set_page_config(
    page_title="Bhavya's Professional Assistant",
    page_icon="👩‍💻",
    layout="centered"
)

# ---------------------------------------
# CUSTOM CSS
# ---------------------------------------

st.markdown(
    """
    <style>

    .stApp {
        background-color: #0e1117;
    }

    .title {
        text-align: center;
        font-size: 40px;
        font-weight: 800;
        color: white;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: white;
        font-size: 16px;
        margin-bottom: 25px;
    }
    .stChatMessage p {
    color: white !important;
}

    .section-title {
        color: white;
        font-size: 14px;
        font-weight: 600;
        margin-top: 15px;
        margin-bottom: 8px;
    }

    .profile-card {
        padding: 18px;
        border-radius: 12px;
        background-color: #161b22;
        margin-bottom: 20px;
        color:white !important;
    }

    .stButton > button {
        border-radius: 20px;
        padding: 5px 12px;
        font-size: 13px;
        min-height: 34px;
       
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------
# HEADER
# ---------------------------------------

st.markdown(
    '<div class="title">👩‍💻 Bhavya\'s Professional Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
    Ask me about Bhavya's education, skills, projects,
    Java experience, DSA, AI/ML and career interests.
    </div>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------
# PROFILE SUMMARY
# ---------------------------------------

st.markdown(
    """
    <div class="profile-card">
    <b>👋 Welcome!</b><br><br>
    I'm a Personal Professional FAQ Assistant.
    Ask me questions about Bhavya's technical background,
    projects, education and career interests.
    </div>
    """,
    unsafe_allow_html=True
)
# ---------------------------------------
# CHAT HISTORY
# ---------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

# ---------------------------------------
# SUGGESTED QUESTIONS
# ---------------------------------------
st.markdown(
    '<div class="section-title">Try asking</div>',
    unsafe_allow_html=True
)

suggestions = [
    "Who is Bhavya?",
    "What are her technical skills?",
    "Tell me about her projects.",
    "Education details",
    "How many DSA problems has she solved?",
    "Tell me about her API Rate Limiter."
]
cols = st.columns(2)
for i, suggestion in enumerate(suggestions):

    with cols[i % 2]:

        if st.button(
            suggestion,
            key=f"suggestion_{i}"
        ):

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": suggestion
                }
            )

            response = chatbot_response(suggestion)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": response
                }
            )

            st.rerun()


# ---------------------------------------
# CHAT INPUT
# ---------------------------------------

user_input = st.chat_input(
    "Ask about Bhavya..."
)


if user_input:

    # Add user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )


    # Generate response
    response = chatbot_response(user_input)


    # Add chatbot response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )


    # Refresh page
    st.rerun()