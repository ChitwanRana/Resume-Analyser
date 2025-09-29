
<div align="center">
  <img src="https://img.icons8.com/color/96/000000/resume.png" alt="Resume Icon" width="80"/>
  
  # <span style="color:#4299e1">Resume Evaluator</span>
  
  <p>
    <b>🚀 Analyze, Score & Improve Your Resume!</b><br>
    <i>A creative web app to evaluate resumes, visualize your strengths, and recommend courses for career growth.</i>
  </p>
  
  <p>
    <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python"/>
    <img src="https://img.shields.io/badge/Django-5.2.6-success?logo=django"/>
    <img src="https://img.shields.io/badge/Bootstrap-5.3.2-purple?logo=bootstrap"/>
    <img src="https://img.shields.io/badge/Font%20Awesome-6.4.0-orange?logo=fontawesome"/>
  </p>
</div>

---

## ✨ Features

🌟 **Upload & Analyze:** Instantly upload your resume and get a professional evaluation.<br>
🎯 **Score Visualization:** See your resume score in a beautiful circular progress indicator.<br>
🧩 **Skill Insights:** Discover missing skills and strengths for your target career.<br>
📚 **Course Recommendations:** Get curated courses and resources to boost your profile.<br>
🎨 **Modern UI:** Enjoy a sleek, responsive interface powered by Bootstrap 5 & Font Awesome.

---

## 🛠️ Technologies Used

| Technology      | Purpose                |
|-----------------|------------------------|
| Python 3.12     | Backend Logic          |
| Django 5.2.6    | Web Framework          |
| Bootstrap 5     | UI Styling             |
| Font Awesome    | Icons                  |
| Google Fonts    | Typography (Poppins)   |

---

## 📁 Folder Structure

```text
resume_evaluator/
├── career_model.pkl         # ML model for career prediction
├── db.sqlite3               # Database
├── manage.py                # Django management
├── requirements.txt         # Python dependencies
├── train_model.py           # Model training script
├── vectorizer.pkl           # Text vectorizer
├── CV_app/                  # Main Django app
│   ├── forms.py             # Resume upload form
│   ├── models.py            # Database models
│   ├── utils.py             # Scoring logic
│   ├── views.py             # App views
│   └── migrations/          # DB migrations
├── media/                   # Uploaded resumes
├── myenv/                   # Virtual environment
├── resume_evaluator/        # Django project settings
└── templates/               # HTML templates
    ├── home.html            # Upload page
    └── result.html          # Results page
```

---

## 🚦 Quick Start

1. **Clone the repository**
   ```powershell
   git clone <repo-url>
   cd Resume-Analyser
   ```
2. **Create & activate a virtual environment**
   ```powershell
   python -m venv myenv
   myenv\Scripts\activate
   ```
3. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```
4. **Apply migrations**
   ```powershell
   python manage.py migrate
   ```
5. **Run the development server**
   ```powershell
   python manage.py runserver
   ```
6. **Open in browser**
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🎉 Usage

1. **Upload** your resume on the home page.
2. **View** your evaluation: score, missing skills, and recommended courses.
3. **Click** "Analyze Another Resume" to try again!

---

## 🖌️ Customization

- Edit `templates/result.html` for UI changes.
- Update scoring logic in `CV_app/utils.py` and `CV_app/views.py`.

---

## 👨‍💻 Authors

<table>
  <tr>
    <td align="center"><b>Chitwan Rana</b></td>
    <td align="center"><b>Aditi Mishra</b></td>
    <td align="center"><b>Ashish Yadav</b></td>
  </tr>
</table>

---

<div align="center">
  <sub>Made with ❤️ for career growth</sub>
</div>
