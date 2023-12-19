from django.shortcuts import render

potatoes = [
    {'brand': 'Reser\'s Red Skin Potato Salad', 'description': 'The best there is', 'rating': 5},
    {'brand': 'Lunardi\'s SF Potato Salad', 'description': 'Best store made p.s.', 'rating': 5},
    {'brand': 'Signature Kitchen\'s Classic Potato Salad', 'description': 'Absolute trash', 'rating': 1},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def potatoes_index(request):
    return render(request, 'potatoes/index.html', {
        'potatoes': potatoes
    })