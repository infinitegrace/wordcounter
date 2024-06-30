from django.shortcuts import render

# Create your views here.
def index(request):

    context = {
        'name' : 'John',
        'age': 23,
        'nationality': 'Nigerian'
    }
    return render(request, 'index.html', context)

def counter(request):
    text = request.POST['text']
    Amount_of_words = len(text.split())

    return render(request, 'counter.html', {'amount':Amount_of_words})
   