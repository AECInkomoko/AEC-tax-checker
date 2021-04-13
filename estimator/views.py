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

    filerType = request.GET.get('filerType');
    income = request.GET.get('income');
    state = request.GET['state'];

    tc = TaxCalculator
    fedTaxAmount = tc.computeFederalTax(income, filerType)
    fedStandardDeduction = tc.getFederalStandardDeduction()
    stateTaxAmount = tc.computeStateTax(income, filerType, state)
    stateStandardDeduction = tc.getStateStandardDeduction()

    print ("Federal Tax = " + str(fedTaxAmount))
    print ("Federal Standard Deduction = " + str(fedStandardDeduction))

    print ("State Tax = " + str(stateTaxAmount))
    print ("State Standard Deduction = " + str(stateStandardDeduction))

    # return render(request, 'estimator/estimator.html',
    # {
    #     'withholdAmount':withholdAmount,
    # }

    return render(request, 'estimator/estimator.html',
        {
          'income':income,
          'state':state,
          'fedTaxAmount':fedTaxAmount,
          'stateTaxAmount':stateTaxAmount,
          'fedStandardDeduction':fedStandardDeduction,
          'stateStandardDeduction':stateStandardDeduction,
        }
    );
