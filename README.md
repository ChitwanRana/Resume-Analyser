# Resume Evaluator

A visually appealing web application to analyze and score resumes, recommend courses, and provide feedback for career improvement.

## Features
- Upload your resume and get a detailed evaluation
- See your resume score visualized with a circular progress indicator
- Get feedback on missing skills and strengths
- Receive recommended courses and resources to improve your profile
- Beautiful, modern UI with Bootstrap 5 and Font Awesome

## Technologies Used
- Python 3.12
- Django 5.2.6
- Bootstrap 5
- Font Awesome
- Google Fonts (Poppins)

## Folder Structure
```
resume_evaluator/
├── career_model.pkl
├── db.sqlite3
├── manage.py
├── README.md
├── requirements.txt
├── train_model.py
├── vectorizer.pkl
├── CV_app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   ├── views.py
│   └── migrations/
│       ├── __init__.py
│       └── 0001_initial.py
├── media/
│   └── resumes/
├── myenv/
│   └── ...
├── resume_evaluator/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __pycache__/
└── templates/
    ├── home.html
    └── result.html
```

## Setup Instructions
1. **Clone the repository**
   ```sh
   git clone <repo-url>
   cd Resume-Analyser
   ```
2. **Create and activate a virtual environment**
   ```sh
   python -m venv myenv
   myenv\Scripts\activate
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Apply migrations**
   ```sh
   python manage.py migrate
   ```
5. **Run the development server**
   ```sh
   python manage.py runserver
   ```
6. **Open in browser**
   Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage
- Upload your resume on the home page
- View your evaluation results, score, missing skills, and recommended courses
- Click "Analyze Another Resume" to upload a new file

## Customization
- Modify `result.html` in the `templates/` folder for UI changes
- Update scoring logic in `CV_app/utils.py` and `CV_app/views.py`


## Author
Chitwan Rana
Aditi Mishra 
Ashish Yadav
