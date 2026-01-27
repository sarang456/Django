from django.shortcuts import render
def aboutus(request):
    return render(request, 'aboutus.html')
def contactus(request):
    return render(request, 'contactus.html')
def home(request):
    return render(request, 'home.html')
def movies(request):
    return render(request, 'movies.html')
def news(request):
    return render(request, 'news.html')
def shows(request):
    return render(request, 'shows.html')
def main(request):
    return render(request, 'main.html')