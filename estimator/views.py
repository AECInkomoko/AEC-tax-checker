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

    try:
      test = int(income)
    except ValueError:
      income = 0
      return render(request, 'estimator/estimator.html')

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
    print ("totalTaxAmount " + str(totalTaxAmount))
    print ("income " + income)
    effectiveRate = round(100*int(totalTaxAmount)/int(income))
    print("effectiveRate " + str(effectiveRate))
    withholdAmount = round(totalTaxAmount/12)

    # Compute Fed Tax stuff
    fedEffectiveRate = round(100*fedTaxAmount/int(income))
    fedWithholdAmount = round(fedTaxAmount/12)

    # Compute State Tax stuff
    stateEffectiveRate = round(100*stateTaxAmount/int(income))
    stateWithholdAmount = round(stateTaxAmount/12)

    fedTaxBracket = tc.getFederalTaxBracket(taxableIncome, filerType)
    stateTaxBracket = tc.getStateTaxBracket(taxableIncome, filerType, state)

    return render(request, 'estimator/estimator.html',
        {
          'income':income,
          'totalTaxAmount':totalTaxAmount,
          'effectiveRate':effectiveRate,
          'withholdAmount':withholdAmount,
          'fedStandardDeduction':fedStandardDeduction,
          'fedTaxAmount':fedTaxAmount,
          'fedEffectiveRate':fedEffectiveRate,
          'fedWithholdAmount':fedWithholdAmount,
          'state':state,
          'stateStandardDeduction':stateStandardDeduction,
          'stateTaxAmount':stateTaxAmount,
          'stateEffectiveRate':stateEffectiveRate,
          'stateWithholdAmount':stateWithholdAmount,
          'fedTaxBracket':fedTaxBracket,
          'stateTaxBracket':stateTaxBracket,
        }
    );
