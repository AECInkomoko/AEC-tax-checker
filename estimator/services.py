# import the logging library
import logging
from .models import TaxBracket

class TaxCalculator:

  # Get an instance of a logger
  #logger = logging.getLogger(__name__)

  #def __init__(self, name):
#self.name = name    # instance variable unique to each instance
#    logger.error('Something went wrong!')

  def calculateWithholdAmount(income, numPayChecks, state):
    #print ("Parameters Passed: " + income + " " + numPayChecks + " " + state)
    #print ("Parameters Passed: " + income + " " + numPayChecks)

    print("entered calculateWithholdAmount")
    #print("Param 1: " + str(income))
    #print("Param 2: " + str(numPayChecks))
    #print("Param 3: " + state)

    #taxBracket = TaxBracket.objects.all()

    #=IF($C$3>F3, IF (ISBLANK(F3),MAX(0, $C$3-F2), F3-F2), MAX(0,$C$3-F2))

    #for e in TaxBracket.objects.all():
    for e in TaxBracket.objects.all().filter(taxType="Federal"):
      print("Tax Type: " + e.taxType + " RangeMax: " + str(e.rangeMax))

    for e in TaxBracket.objects.all().filter(taxType="State"):
      print("Tax Type: " + e.taxType + " RangeMax: " + str(e.rangeMax))

    #income = income
    #paychecks = numPayChecks
    #state = state

    witholdAmount = 400
    #(income * .4)/numPayChecks

    return witholdAmount;
