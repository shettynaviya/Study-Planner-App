import streamlit as st
from auth import show_login_signup, get_current_user
from study_plans import study_plans_page
from task_manager import task_manager_page
from analytics import analytics_page
from calendar_view import calendar_view
from pdf_generator import generate_pdf_report

# Set app title and layout
st.set_page_config(page_title="Study Planner", layout="wide")

# 🧑‍🎨 Apply fixed dark theme using custom CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    div[data-testid="stHeader"],
    div[data-testid="stSidebar"] {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    .stTextInput > div > div > input,
    .stTextArea textarea,
    .stSelectbox > div > div {
        background-color: #333333;
        color: #ffffff;
        border: 1px solid #444;
    }
    .stButton > button {
        background-color: #0e76a8;
        color: white;
        border: none;
    }
    .stDataFrame { 
        background-color: #1e1e1e; 
        color: #ffffff; 
    }
    /* Style for big app title */
    .app-title {
        font-size: 50px;
        font-weight: bold;
        color: #ffffff;
        text-align: center;
        margin-top: -30px;
        margin-bottom: 70px;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    # Add a big app title at the top of the page
    st.markdown('<div class="app-title">Study Planner App</div>', unsafe_allow_html=True)

    user = get_current_user()
    if user is None:
        show_login_signup()
    else:
        # ✅ Show user's name at the top of the sidebar
        st.sidebar.markdown(f"""
            <div style='padding: 16px 0 8px 0; font-size: 20px; font-weight: 600; color: white;'>
                👋 Hello, {user.get("name", "User")}!
            </div>
        """, unsafe_allow_html=True)

        st.sidebar.markdown("## Navigation")
        page = st.sidebar.radio("Go to", [
            "Study Plans", 
            "Task Manager", 
            "Calendar", 
            "Analytics", 
            "Download PDF", 
            "Logout"
        ])

        if page == "Study Plans":
            study_plans_page(user)
        elif page == "Task Manager":
            task_manager_page(user)
        elif page == "Calendar":
            calendar_view(user)
        elif page == "Analytics":
            analytics_page(user)
        elif page == "Download PDF":
            generate_pdf_report(user)
        elif page == "Logout":
            st.session_state.user = None
            st.rerun()

if __name__ == "__main__":
    main()
