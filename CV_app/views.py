from django.shortcuts import render
from .forms import ResumeUploadForm
from .models import Resume
from .utils import extract_text, extract_info, predict_career, recommend_skills, calculate_score, recommend_courses

def upload_resume(request):
    if request.method == "POST":
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            resume_obj = form.save(commit=False)
            resume_obj.save()

            text = extract_text(resume_obj.file.path)
            info = extract_info(text)
            career_field = predict_career(text)
            skills_missing = recommend_skills(text, career_field)
            score = calculate_score(text, career_field)
            courses = recommend_courses(skills_missing)

            # Save results in model
            resume_obj.career_field = career_field
            resume_obj.skills_missing = ", ".join(skills_missing)
            resume_obj.resume_score = score
            resume_obj.recommended_courses = "\n".join(courses)
            resume_obj.save()

            return render(request, "result.html", {
                "resume": resume_obj,
                "info": info,
                "courses": courses
            })
    else:
        form = ResumeUploadForm()

    return render(request, "home.html", {"form": form})



def home(request):
    return render(request, "home.html")
