import streamlit as st
from database import get_connection
from datetime import datetime

def task_manager_page(user):
    st.header("✅ Task Manager")
    title = st.text_input("Task Title")
    description = st.text_area("Task Description")
    status = st.selectbox("Status", ["Pending", "Running", "Completed"])
    reminder = st.date_input("Reminder Date")

    if st.button("Add Task"):
        with get_connection() as conn:
            conn.execute("INSERT INTO tasks (user_id, title, description, status, reminder, created_at) VALUES (?, ?, ?, ?, ?, ?)",
                         (user["id"], title, description, status, reminder.strftime("%Y-%m-%d"), datetime.now()))
        st.success("Task Added!")
        st.rerun()  # ✅ updated here

    st.subheader("Your Tasks")
    filter_status = st.selectbox("Filter by status", ["All", "Pending", "Running", "Completed"])

    with get_connection() as conn:
        query = "SELECT * FROM tasks WHERE user_id = ?"
        params = [user["id"]]
        if filter_status != "All":
            query += " AND status = ?"
            params.append(filter_status)
        tasks = conn.execute(query, params).fetchall()

    for task in tasks:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(f"**{task['title']}** ({task['status']}) - {task['description']} (📅 {task['reminder']})")
        with col2:
            if st.button("Delete", key=f"del_{task['id']}"):
                with get_connection() as conn:
                    conn.execute("DELETE FROM tasks WHERE id=?", (task['id'],))
                st.success("Task deleted successfully.")
                st.rerun()  # ✅ updated here
