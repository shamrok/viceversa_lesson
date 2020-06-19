from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
    
def reverse(request):
    user_text = request.GET['usertext']
    words = user_text.split()
    numbers_of_words = len(words)
    reversed_text = user_text[::-1]
    return render(request, 'reverse.html', {'usertext':user_text, 'reversedtext':reversed_text, 'numbers_of_words':numbers_of_words})