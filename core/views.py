from django.shortcuts import redirect

def home(request):
    """Redirect to React frontend"""
    return redirect('http://localhost:3000') 