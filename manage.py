#!/usr/bin/env python
import os
import sys
import django
from django.contrib.auth.models import User

def create_superuser():
    if not User.objects.filter(is_superuser=True).exists():
        print("Création superuser admin/admin")
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.settings")
    django.setup()
    create_superuser()
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
