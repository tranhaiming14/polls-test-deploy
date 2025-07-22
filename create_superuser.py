# create_superuser.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username=os.environ["DJANGO_ADMIN_USER"]).exists():
    User.objects.create_superuser(
        os.environ["DJANGO_ADMIN_USER"],
        os.environ["DJANGO_ADMIN_EMAIL"],
        os.environ["DJANGO_ADMIN_PASSWORD"]
    )
    print("✅ Superuser created.")
else:
    print("Superuser already exists.")
