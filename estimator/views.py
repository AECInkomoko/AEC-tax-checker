from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'estimator/home.html', {})

def estimator(request):

    income = request.GET.get('income');
    paychecks = request.GET.get('paychecks');
    state = request.GET['state'];
    return render(request, 'estimator/estimator.html',
        {'income':income,
         'paychecks':paychecks,
         'state':state
        }
    );
