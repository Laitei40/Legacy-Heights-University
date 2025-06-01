from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse
from core.models import Course

def program_list(request):
    q = request.GET.get('q', '')
    courses = Course.objects.select_related('department').all()
    if q:
        courses = courses.filter(name__icontains=q)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('programs/course_list.html', {
            'courses': courses,
            'request': request
        })
        return JsonResponse({'html': html})

    return render(request, 'programs/program.html', {'courses': courses})