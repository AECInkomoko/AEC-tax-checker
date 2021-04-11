from django.shortcuts import render
from django.http import HttpResponse
from .services import TaxCalculator

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.
def home(request):
    return render(request, 'estimator/home.html', {})

def estimator(request):
    print ("reached estimator")
    income = request.GET.get('income');
    print ("1 retrieved " + str(income))
    numPayChecks = request.GET.get('numPayChecks');
    print ("2 retrieved " + str(numPayChecks))
    state = request.GET['state'];
    print ("3 retrieved ")

    tc = TaxCalculator
    withholdAmount = tc.calculateWithholdAmount(income, numPayChecks, state)

    print (withholdAmount)

    # return render(request, 'estimator/estimator.html',
    # {
    #     'withholdAmount':withholdAmount,
    # }

    return render(request, 'estimator/estimator.html',
        {'income':income,
         'paychecks':numPayChecks,
         'state':state,
         'withholdAmount':withholdAmount,
        }
    );
