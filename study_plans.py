def study_plans_page(user):
    import streamlit as st
    from database import get_connection
    from datetime import datetime

    st.header("\U0001F4DA Study Plans")
    with st.form("study_plan_form"):
        title = st.text_input("Title")
        description = st.text_area("Description")
        reminder = st.date_input("Reminder Date")
        submitted = st.form_submit_button("Add Study Plan")
        if submitted:
            if title.strip():
                with get_connection() as conn:
                    conn.execute("""
                        INSERT INTO study_plans (user_id, title, description, reminder, created_at)
                        VALUES (?, ?, ?, ?, ?)
                    """, (user["id"], title, description, reminder.strftime("%Y-%m-%d"), datetime.now()))
                st.success("Study Plan Added!")
                st.rerun()
            else:
                st.error("Title cannot be empty")

    st.subheader("Your Study Plans")
    with get_connection() as conn:
        plans = conn.execute("SELECT * FROM study_plans WHERE user_id = ?", (user["id"],)).fetchall()

    for plan in plans:
        with st.expander(f"{plan['title']} (\U0001F4C5 {plan['reminder']})"):
            new_title = st.text_input("Edit Title", value=plan['title'], key=f"et_{plan['id']}")
            new_desc = st.text_area("Edit Description", value=plan['description'], key=f"ed_{plan['id']}")
            new_reminder = st.date_input("Edit Reminder", value=datetime.strptime(plan['reminder'], "%Y-%m-%d"), key=f"er_{plan['id']}")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Update", key=f"upd_{plan['id']}"):
                    with get_connection() as conn:
                        conn.execute("""
                            UPDATE study_plans SET title=?, description=?, reminder=? WHERE id=?
                        """, (new_title, new_desc, new_reminder.strftime("%Y-%m-%d"), plan['id']))
                    st.success("Updated successfully.")
                    st.rerun()
            with col2:
                if st.button("Delete", key=f"del_{plan['id']}"):
                    with get_connection() as conn:
                        conn.execute("DELETE FROM study_plans WHERE id=?", (plan['id'],))
                    st.success("Deleted successfully.")
                    st.rerun()
