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

    # Get the input parameters
    filerType = request.GET.get('filerType');
    income = request.GET.get('income');
    state = request.GET['state'];

    # Compute Federal Tax stuff
    tc = TaxCalculator
    fedStandardDeduction = tc.getFederalStandardDeduction()
    taxableIncome = int(income) - int(fedStandardDeduction)
    fedTaxAmount = tc.computeFederalTax(taxableIncome, filerType)

    # Compute State Tax stuff
    stateStandardDeduction = tc.getStateStandardDeduction()
    taxableIncome = int(income) - int(stateStandardDeduction)
    stateTaxAmount = tc.computeStateTax(taxableIncome, filerType, state)

    print ("Federal Tax = " + str(fedTaxAmount))
    print ("Federal Standard Deduction = " + str(fedStandardDeduction))

    print ("State Tax = " + str(stateTaxAmount))
    print ("State Standard Deduction = " + str(stateStandardDeduction))

    # Compute Total Tax stuff
    totalTaxAmount = fedTaxAmount + stateTaxAmount
    paystubAmount = round(totalTaxAmount / 26)

    fedTaxBracket = tc.getFederalTaxBracket(taxableIncome, filerType)
    stateTaxBracket = tc.getStateTaxBracket(taxableIncome, filerType, state)

    return render(request, 'estimator/estimator.html',
        {
          'income':income,
          'state':state,
          'fedTaxAmount':fedTaxAmount,
          'stateTaxAmount':stateTaxAmount,
          'fedStandardDeduction':fedStandardDeduction,
          'stateStandardDeduction':stateStandardDeduction,
          'totalTaxAmount':totalTaxAmount,
          'paystubAmount':paystubAmount,
          'fedTaxBracket':fedTaxBracket,
          'stateTaxBracket':stateTaxBracket,
        }
    );
