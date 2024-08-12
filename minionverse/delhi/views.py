from django.shortcuts import render
from .models import Cinema

# Create your views here.
def city(request):
    return render(request, "delhi/city.html")

def cinemas(request):
    _selected_columns = [field.name for field in Cinema._meta.fields]
    _cinemas = Cinema.objects.all()
    if request.method == 'POST':
        _selected_columns = request.POST.getlist('column')
    return render(request, "delhi/cinemas.html", {
            'selected_columns': _selected_columns,
            'cinemas': _cinemas})