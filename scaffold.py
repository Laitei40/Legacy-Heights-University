# 🔧 Django Project Scaffolding Bot Script
# This bot creates the folder structure, files, and base content for your project.
# Run this script in your terminal after navigating to your desired directory.

import os
import subprocess

# ✅ Basic Setup
PROJECT_NAME = "final_project"
APPS = [
    "core", "accounts", "activities", "contact",
    "students", "staff", "programs"
]
TEMPLATES = {
    "accounts": "account.html",
    "activities": "activity.html",
    "contact": "contact.html",
    "students": "marksheet.html",
    "staff": "staff.html",
    "programs": "program.html",
    "core": ["home.html", "base.html"]
}

# ✅ Commands
print("📦 Creating Django Project...")
subprocess.run(["django-admin", "startproject", PROJECT_NAME])

# 🌱 Move into project directory
os.chdir(PROJECT_NAME)

print("📁 Creating Apps...")
for app in APPS:
    subprocess.run(["python3", "manage.py", "startapp", app])

print("🗃 Creating Template Structure...")
for app, template in TEMPLATES.items():
    if isinstance(template, list):
        for tpl in template:
            path = os.path.join(app, "templates", app)
            os.makedirs(path, exist_ok=True)
            with open(os.path.join(path, tpl), "w") as f:
                f.write(f"<!-- {tpl} -->\n<h1>{tpl[:-5].capitalize()}</h1>")
    else:
        path = os.path.join(app, "templates", app)
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, template), "w") as f:
            f.write(f"<!-- {template} -->\n<h1>{template[:-5].capitalize()}</h1>")

print("🧾 Creating urls.py for each app...")
for app in APPS:
    url_file = os.path.join(app, "urls.py")
    with open(url_file, "w") as f:
        f.write(f"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='{app}_index'),
]
""")
    view_file = os.path.join(app, "views.py")
    with open(view_file, "a") as f:
        f.write(f"""
from django.shortcuts import render

def index(request):
    return render(request, '{app}/{TEMPLATES[app] if isinstance(TEMPLATES[app], str) else TEMPLATES[app][0]}')
""")

print("🧱 Updating main urls.py...")
main_urls = os.path.join(PROJECT_NAME, "urls.py")
with open(main_urls, "r") as f:
    content = f.read()

# Inject imports and urlpatterns
import_line = "from django.urls import path, include\n"
app_paths = "\n".join([f"    path('{app}/', include('{app}.urls'))," for app in APPS])

new_content = content.replace(
    "from django.urls import path",
    import_line
).replace(
    "urlpatterns = [",
    f"urlpatterns = [\n{app_paths}"
)

with open(main_urls, "w") as f:
    f.write(new_content)

print("✅ All Done Laitei! Your Django structure is ready!")
print("👉 Next Steps:\n- Define your models in each app\n- Run migrations\n- Start the server")
