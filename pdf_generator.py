import streamlit as st
from fpdf import FPDF
from database import get_connection
from datetime import datetime

def generate_pdf_report(user):
    st.markdown("## 🧾 Download Your Study Planner Report")
    st.markdown("Export all your study plans and tasks into a **well-formatted PDF report**. Great for tracking your progress or sharing with mentors. 📚")

    with st.spinner("Generating your PDF report..."):
        pdf = FPDF()
        pdf.add_page()

        # Title
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt="Study Planner Report", ln=1, align='C')

        # Generated timestamp
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
        pdf.ln(5)

        with get_connection() as conn:
            plans = conn.execute("SELECT * FROM study_plans WHERE user_id = ?", (user["id"],)).fetchall()
            tasks = conn.execute("SELECT * FROM tasks WHERE user_id = ?", (user["id"],)).fetchall()

        # Study Plans Section
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(200, 10, txt="Study Plans", ln=True)
        pdf.set_font("Arial", size=12)

        if plans:
            for i, p in enumerate(plans, start=1):
                pdf.multi_cell(0, 8, txt=f"{i}. Title: {p['title']}\n   Description: {p['description']}\n   Reminder: {p['reminder']}")
                pdf.ln(2)
        else:
            pdf.cell(0, 10, txt="No study plans available.", ln=True)

        pdf.ln(5)

        # Tasks Section
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(200, 10, txt="Tasks", ln=True)
        pdf.set_font("Arial", size=12)

        if tasks:
            for i, t in enumerate(tasks, start=1):
                pdf.multi_cell(0, 8, txt=f"{i}. Title: {t['title']} ({t['status']})\n   Description: {t['description']}\n   Reminder: {t['reminder']}")
                pdf.ln(2)
        else:
            pdf.cell(0, 10, txt="No tasks available.", ln=True)

        # Output PDF
        pdf.output("study_planner_report.pdf")

    # Streamlit UI - Download & Tips
    st.success("✅ Your PDF report is ready!")
    with open("study_planner_report.pdf", "rb") as f:
        st.download_button(
            label="📥 Download PDF Report",
            data=f,
            file_name="study_planner_report.pdf",
            mime="application/pdf"
        )

    st.markdown("---")
    st.info("💡 Tip: Use this PDF to reflect on your learning progress and share it during mentor sessions or academic reviews.")
