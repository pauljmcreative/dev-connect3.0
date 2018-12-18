from django import template
from django.contrib.auth.models import User

register = template.Library()

@register.inclusion_tag('partials/student_directory.html')
def student_directory():
    students = User.objects.all()
    return {'students': students}
