import streamlit as st
from database import get_connection
import pandas as pd

def calendar_view(user):
    st.header("📆 Calendar View")

    # Fetch data
    with get_connection() as conn:
        plans = conn.execute("SELECT title, reminder FROM study_plans WHERE user_id = ?", (user["id"],)).fetchall()
        tasks = conn.execute("SELECT title, reminder FROM tasks WHERE user_id = ?", (user["id"],)).fetchall()

    # Convert to DataFrames only if data is not empty
    df_plans = pd.DataFrame(plans, columns=["title", "reminder"]) if plans else pd.DataFrame(columns=["title", "reminder"])
    df_tasks = pd.DataFrame(tasks, columns=["title", "reminder"]) if tasks else pd.DataFrame(columns=["title", "reminder"])

    # Add a type column for distinction
    if not df_plans.empty:
        df_plans["Type"] = "Study Plan"
    if not df_tasks.empty:
        df_tasks["Type"] = "Task"

    # Concatenate and handle empty case
    df = pd.concat([df_plans, df_tasks], ignore_index=True)

    if df.empty:
        st.info("No tasks or study plans found with reminders.")
        return

    # Convert and sort by reminder date
    df['reminder'] = pd.to_datetime(df['reminder'], errors='coerce')
    df.dropna(subset=['reminder'], inplace=True)  # drop rows where reminder is null/invalid

    if df.empty:
        st.info("No valid reminder dates found.")
        return

    # Show the calendar data
    st.dataframe(df.sort_values(by="reminder"))
