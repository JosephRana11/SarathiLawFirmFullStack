from django.shortcuts import render

# Create your views here.
def home_view(request):
  if (request.method == 'POST'):
    print('Working')
    return render(request , 'home.html')
  else:
   return render(request , 'home.html')