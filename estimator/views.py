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
    if fedTaxAmount < 0 :
      fedTaxAmount = 0

    print ("Federal Tax = " + str(fedTaxAmount))
    print ("Federal Standard Deduction = " + str(fedStandardDeduction))

    # Compute State Tax stuff
    stateStandardDeduction = tc.getStateStandardDeduction(filerType, state)
    taxableIncome = int(income) - int(stateStandardDeduction)
    stateTaxAmount = tc.computeStateTax(taxableIncome, filerType, state)

    if stateTaxAmount < 0 :
      stateTaxAmount = 0

    print ("State Tax = " + str(stateTaxAmount))
    print ("State Standard Deduction = " + str(stateStandardDeduction))

    # Compute Total Tax stuff
    totalTaxAmount = fedTaxAmount + stateTaxAmount
    totalDeduction = fedStandardDeduction + stateStandardDeduction
    print ("totalTaxAmount " + str(totalTaxAmount))
    print ("income " + income)
    effectiveRate = round(100*int(totalTaxAmount)/int(income), 2)
    print("effectiveRate " + str(effectiveRate))
    withholdAmount = round(totalTaxAmount/12, 2)

    # Compute Fed Tax stuff
    fedEffectiveRate = round(100*fedTaxAmount/int(income), 2)
    fedWithholdAmount = round(fedTaxAmount/12, 2)

    # Compute State Tax stuff
    stateEffectiveRate = round(100*stateTaxAmount/int(income), 2)
    stateWithholdAmount = round(stateTaxAmount/12, 2)

    fedTaxBracket = tc.getFederalTaxBracket(filerType)
    stateTaxBracket = tc.getStateTaxBracket(filerType, state)

    return render(request, 'estimator/estimator.html',
        {
          'income':income,
          'state':state,
          'filerType':filerType,
          'totalTaxAmount':totalTaxAmount,
          'effectiveRate':effectiveRate,
          'withholdAmount':withholdAmount,
          'totalDeduction':totalDeduction,
          'fedStandardDeduction':fedStandardDeduction,
          'fedTaxAmount':fedTaxAmount,
          'fedEffectiveRate':fedEffectiveRate,
          'fedWithholdAmount':fedWithholdAmount,
          'stateStandardDeduction':stateStandardDeduction,
          'stateTaxAmount':stateTaxAmount,
          'stateEffectiveRate':stateEffectiveRate,
          'stateWithholdAmount':stateWithholdAmount,
          'fedTaxBracket':fedTaxBracket,
          'stateTaxBracket':stateTaxBracket,
        }
    );
