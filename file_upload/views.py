from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# from django.core.files.storage import FileSystemStorage

import json
from .models import JsonData


def home(request):
    json_data = JsonData.objects.filter(user=request.user.id)
    return render(request, "home.html", context={"json_data": json_data})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


def upload(request):
    context = {}
    if request.method == "POST":
        uploaded_file = request.FILES["document"]

        if uploaded_file.content_type != "application/json":
            json_data = JsonData.objects.filter(user=request.user.id)
            return render(
                request,
                "home.html",
                context={
                    "wrong_content_type": "wrong_content_type",
                    "json_data": json_data,
                },
            )
        jdata = uploaded_file.read()
        json_data = json.loads(jdata)
        for d in json_data:
            userId = d.pop("userId")
            user_obj = User.objects.filter(id=userId)
            if user_obj:
                d.update({"user_id": user_obj[0].id})
                JsonData.objects.update_or_create(**d)
        return redirect("home")

    return render(request, "upload.html", context)
