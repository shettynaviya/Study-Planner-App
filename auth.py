import streamlit as st
import hashlib
from database import get_connection

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_user(username, password):
    with get_connection() as conn:
        result = conn.execute(
            "SELECT * FROM users WHERE username = ? AND password_hash = ?", 
            (username, hash_password(password))
        ).fetchone()
        return result

def create_user(username, password):
    with get_connection() as conn:
        try:
            conn.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)", 
                (username, hash_password(password))
            )
            return True
        except:
            return False

def show_login_signup():
    st.title("Login / Sign Up")
    action = st.radio("Select Action", ["Login", "Sign Up"])

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button(action):
        if action == "Login":
            user = verify_user(username, password)
            if user:
                # ✅ Store user data with "name" key
                st.session_state.user = {
                    "name": user["username"],
                    "id": user["id"]
                }
                st.success("Logged in successfully.")
                st.rerun()
            else:
                st.error("Invalid credentials.")
        else:
            success = create_user(username, password)
            if success:
                st.success("Account created. You can log in now.")
            else:
                st.error("Username already taken.")

def get_current_user():
    return st.session_state.get("user", None)
