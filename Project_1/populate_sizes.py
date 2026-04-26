import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_1.settings')
django.setup()

from application.models import Material

materials = Material.objects.all()
for m in materials:
    try:
        if m.file and m.file.storage.exists(m.file.name):
            m.file_size = m.file.size
            m.save()
            print(f"Updated {m.title} with size {m.file_size}")
        else:
            print(f"File for {m.title} not found.")
    except Exception as e:
        print(f"Error processing {m.title}: {e}")
