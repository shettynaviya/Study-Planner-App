import streamlit as st
import pandas as pd
import plotly.express as px
from database import get_connection

def analytics_page(user):
    st.header("📊 Analytics and Reports")

    with get_connection() as conn:
        plans = conn.execute("SELECT id, user_id, title, description, reminder FROM study_plans WHERE user_id = ?", (user["id"],)).fetchall()
        tasks = conn.execute("SELECT id, user_id, title, description, status, reminder FROM tasks WHERE user_id = ?", (user["id"],)).fetchall()

    df_plans = pd.DataFrame(plans, columns=["id", "user_id", "title", "description", "reminder"])
    df_tasks = pd.DataFrame(tasks, columns=["id", "user_id", "title", "description", "status", "reminder"])

    # Convert reminder columns to datetime safely
    if not df_plans.empty:
        df_plans["reminder"] = pd.to_datetime(df_plans["reminder"], errors='coerce')
    if not df_tasks.empty:
        df_tasks["reminder"] = pd.to_datetime(df_tasks["reminder"], errors='coerce')

    # Study Plan Stats
    st.subheader("📘 Study Plan Stats")
    if not df_plans.empty:
        st.dataframe(df_plans)
        df_plans["Day"] = df_plans["reminder"].dt.date
        fig = px.histogram(df_plans, x="Day", title="Study Plan Reminder Dates")
        st.plotly_chart(fig)
    else:
        st.info("No Study Plans Available")

    # Task Stats
    st.subheader("📝 Task Stats")
    if not df_tasks.empty:
        st.dataframe(df_tasks)

        # Pie chart of task status
        st.subheader("✅ Task Completion Breakdown")
        status_counts = df_tasks["status"].value_counts().reset_index()
        status_counts.columns = ["status", "count"]
        pie = px.pie(status_counts, values="count", names="status", title="Task Status Distribution")
        st.plotly_chart(pie)

        # Task reminders over time
        st.subheader("📅 Task Reminder Timeline")
        df_tasks["Day"] = df_tasks["reminder"].dt.date
        task_day_count = df_tasks.groupby("Day").size().reset_index(name="Task Count")
        line = px.line(task_day_count, x="Day", y="Task Count", markers=True, title="Tasks Scheduled Over Time")
        st.plotly_chart(line)
    else:
        st.info("No Tasks Available")
