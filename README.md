# 📚 Study Planner App

A simple and efficient web-based study planner built using **Streamlit** and **Python**.  
It helps students manage their tasks, get reminders, and stay on track with their study goals.

🌐 Live Demo

👉 Try the app here:
https://shettynaviya-study-planner-app-main-hbnuxm.streamlit.app/

## 🚀 Features

- ✅ **Task Management** – Add, update, delete, and filter study tasks
- ⏰ **Email Reminders** – Set reminders and receive email notifications
- 📅 **Schedule View** – Visualize your daily/weekly tasks
- 📝 **PDF Export** – Download your plan for offline access
- 📤 **Cross-platform access** – Use from any device with a browser

---

## 🖥️ Tech Stack

- **Frontend/UI**: [Streamlit](https://streamlit.io/)
- **Backend**: Python
- **Database**: CSV or in-memory (can be extended to SQLite/MySQL)
- **Email Services**: `smtplib`, `email.message`
- **PDF Export**: `reportlab`, `fpdf`, or `pdfkit`

---

## 🧪 How to Run Locally

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repo:**
   ```bash
   git clone https://github.com/shettynaviya/Study-Planner-App.git
   cd Study-Planner-App
Install dependencies:


pip install -r requirements.txt
Run the app:


streamlit run app.py
✉️ Email Reminder Setup
To enable email reminders:

Configure your email credentials in a .env file or inside the script:


EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
Use App Password if using Gmail with 2FA
How to get one →

📦 Folder Structure
bash
Copy
Edit
Study-Planner-App/
│
├── app.py                # Main Streamlit application
├── tasks.csv             # Task storage (if applicable)
├── utils/                # Helper functions
├── templates/            # Email or UI templates
├── assets/               # Icons, images, or static files
└── requirements.txt      # Python dependencies
💡 Future Enhancements
✅ Google Calendar Sync

✅ Pomodoro Timer

✅ Task Priority and Categories

✅ Analytics Dashboard

✅ Login & User Profiles

🤝 Contributing
Contributions are welcome!
Feel free to open issues or submit PRs for bug fixes, improvements, or new features.

📜 License
This project is open-source under the MIT License.

🙋‍♀️ Author
Built with ❤️ by shettynaviya

yaml
Copy
Edit

---

### ✅ What to Do Next:

1. Create a new file in your repo:  
   👉 `Study-Planner-App/README.md`

2. Paste the content above into it

3. Commit and push:
```bash
git add README.md
git commit -m "Add initial README"
git push origin main
