from django.shortcuts import render

def Index(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')

def Score_board(request):
    return render(request, 'score.html')