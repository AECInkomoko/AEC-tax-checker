# import the logging library
import logging
from .models import TaxBracket

class TaxCalculator:

  def computeFederalTax (income):
    print("entered computeFederalTax")

    try:
      test = int(income)
    except ValueError:
      return 0

    # if income == "":
    #   return 0

    if int(income) == 0 :
      return 0

    fedTaxAmount = 0
    prevRangeMax = 0

    for e in TaxBracket.objects.all().filter(taxType="Federal") :
      rowTaxAmount = 0
      if int(income) < e.rangeMax : #last income row
        #print("last income row")
        taxableIncome = int(income) - prevRangeMax
        rowTaxAmount = taxableIncome * e.rangeRate
        fedTaxAmount = fedTaxAmount + rowTaxAmount
        break;
      elif (e.rangeMax ==0) :
        #print("last range row")
        taxableIncome = int(income) - prevRangeMax
      else : # all other rows
        #print("middle rows")
        taxableIncome = e.rangeMax - prevRangeMax
      prevRangeMax = e.rangeMax
      rowTaxAmount = taxableIncome * e.rangeRate
      fedTaxAmount = fedTaxAmount + rowTaxAmount
      # print("ID: " + str(e.id) + " RangeMax: " + str(e.rangeMax) + " RangeRate: " + str(e.rangeRate) +
      # " TaxableIncome = " + str(taxableIncome) + " Federal Tax = " + str(fedTaxAmount))

    percentage = fedTaxAmount / int(income) * 100
    print("Federal Percentage: " + str(percentage))

    return fedTaxAmount;


  def computeStateTax (income, userState):
    print("entered computeStateTax")

    try:
      test = int(income)
    except ValueError:
      return 0

    # if income == "":
    #   return 0

    if int(income) == 0 :
      return 0

    stateTaxAmount = 0
    prevRangeMax = 0

    for e in TaxBracket.objects.all().filter(taxType="State", state=userState) :
      rowTaxAmount = 0
      if int(income) < e.rangeMax : #last income row
        #print("last income row")
        taxableIncome = int(income) - prevRangeMax
        rowTaxAmount = taxableIncome * e.rangeRate
        stateTaxAmount = stateTaxAmount + rowTaxAmount
        break;
      elif (e.rangeMax ==0) :
        #print("last range row")
        taxableIncome = int(income) - prevRangeMax
      else : # all other rows
        #print("middle rows")
        taxableIncome = e.rangeMax - prevRangeMax
      prevRangeMax = e.rangeMax
      rowTaxAmount = taxableIncome * e.rangeRate
      stateTaxAmount = stateTaxAmount + rowTaxAmount
      # print("ID: " + str(e.id) + " RangeMax: " + str(e.rangeMax) + " RangeRate: " + str(e.rangeRate) +
      #  " TaxableIncome = " + str(taxableIncome) + " State Tax = " + str(stateTaxAmount))

    percentage = stateTaxAmount / int(income) * 100
    print("State Tax Percentage: " + str(percentage))

    return stateTaxAmount;

  def getFederalStandardDeduction () :
    standardDeduction = 25100
    return standardDeduction

  def getStateStandardDeduction () :
    standardDeduction = 9202
    return standardDeduction
