# import the logging library
import logging
from .models import TaxBracket

class TaxCalculator:

  # BEGINNING OF THE METHOD COMPUTEFEDERALTAX
  def computeFederalTax (income, userFilerType):
    print("entered computeFederalTax: " + str(income) + " " + userFilerType)

    try:
      test = income
    except ValueError:
      return 0

    if income == 0 :
      return 0

    fedTaxAmount = 0
    prevRangeMax = 0

    fedTaxBracket = TaxBracket.objects.all().filter(taxType="Federal", filerType=userFilerType)

    for e in fedTaxBracket :
      rowTaxAmount = 0
      if income < e.rangeMax : #last income row
        #print("last income row")
        taxableIncome = income - prevRangeMax
        rowTaxAmount = taxableIncome * e.rangeRate
        fedTaxAmount = fedTaxAmount + rowTaxAmount
        break;
      elif (e.rangeMax ==0) :
        #print("last range row")
        taxableIncome = income - prevRangeMax
      else : # all other rows
        #print("middle rows")
        taxableIncome = e.rangeMax - prevRangeMax
      prevRangeMax = e.rangeMax
      rowTaxAmount = taxableIncome * e.rangeRate
      fedTaxAmount = fedTaxAmount + rowTaxAmount
      # print("ID: " + str(e.id) + " RangeMax: " + str(e.rangeMax) + " RangeRate: " + str(e.rangeRate) +
      #   " TaxableIncome = " + str(taxableIncome) + " Federal Tax = " + str(fedTaxAmount))

    percentage = fedTaxAmount / income * 100
    print("Federal Percentage: " + str(percentage))

    return fedTaxAmount;

  # BEGINNING OF THE METHOD COMPUTESTATETAX
  def computeStateTax (income, userFilerType, userState):
    print("entered computeStateTax: " + str(income) + " " + userFilerType + " " + userState)

    try:
      test = income
    except ValueError:
      return 0

    if income == 0 :
      return 0

    stateTaxAmount = 0
    prevRangeMax = 0

    stateTaxBracket = TaxBracket.objects.all().filter(taxType="State", filerType=userFilerType, state=userState)

    for e in stateTaxBracket :
      rowTaxAmount = 0
      if income < e.rangeMax : #last income row
        # print("last income row")
        taxableIncome = income - prevRangeMax
        rowTaxAmount = taxableIncome * e.rangeRate
        stateTaxAmount = stateTaxAmount + rowTaxAmount
        break;
      elif (e.rangeMax == 0) :
        # print("last range row")
        taxableIncome = income - prevRangeMax
      else : # all other rows
        # print("middle rows")
        taxableIncome = e.rangeMax - prevRangeMax
      prevRangeMax = e.rangeMax
      rowTaxAmount = taxableIncome * e.rangeRate
      stateTaxAmount = stateTaxAmount + rowTaxAmount
      # print("ID: " + str(e.id) + " RangeMax: " + str(e.rangeMax) + " RangeRate: " + str(e.rangeRate) +
      #   " TaxableIncome = " + str(taxableIncome) + " State Tax = " + str(stateTaxAmount))

    percentage = (stateTaxAmount / income) * 100
    print("State Tax Percentage: " + str(percentage))

    return stateTaxAmount;

  # BEGINNING OF THE METHOD getFederalStandardDeduction
  def getFederalStandardDeduction () :
    standardDeduction = 25100
    return standardDeduction

  # BEGINNING OF THE METHOD getStateStandardDeduction
  def getStateStandardDeduction () :
    standardDeduction = 9202
    return standardDeduction

  def getFederalTaxBracket (income, userFilerType):
    fedTaxBracket = TaxBracket.objects.all().filter(taxType="Federal", filerType=userFilerType)
    return fedTaxBracket

  def getStateTaxBracket (income, userFilerType, userState):
    stateTaxBracket = TaxBracket.objects.all().filter(taxType="State", filerType=userFilerType, state=userState)
    return stateTaxBracket
