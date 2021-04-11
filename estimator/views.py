from django.shortcuts import render
from django.http import HttpResponse
from .models import TaxBracket
from .services import TaxCalculator

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.
def home(request):
    return render(request, 'estimator/home.html', {})

def estimator(request):

    taxBracket = TaxBracket.objects.all();
    income = request.GET.get('income');
    paychecks = request.GET.get('paychecks');
    state = request.GET['state'];


    tc = TaxCalculator
    income = tc.calculate(income)
    logger.info('info: I told you so')

    return render(request, 'estimator/estimator.html',
        {'income':income,
         'paychecks':paychecks,
         'state':state,
         #'state':withholding,
         'taxBracket':taxBracket,
        }
    );
