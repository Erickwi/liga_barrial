# views.py

from django.template import loader
from django.http import HttpResponse

def dashboard_view(request):
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render())
