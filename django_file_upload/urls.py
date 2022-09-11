from django.contrib import admin
from django.urls import path, include
from file_upload.views import home, signup, upload

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup", signup, name="signup"),
    path("upload", upload, name="upload"),
]
