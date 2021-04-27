# import the logging library
import logging
from .models import TaxBracket
from .models import StateDeduction

class TaxCalculator:

  # BEGINNING OF THE METHOD COMPUTEFEDERALTAX
  def computeFederalTax (income, userFilerType):
    print("entered computeFederalTax: " + str(income) + " " + userFilerType)

    # try:
    #   test = income
    # except ValueError:
    #   return 0
    #
    # if income == 0 :
    #   return 0

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

    stateTaxAmount = 0
    prevRangeMax = 0

    if userFilerType == "Head" :
      userFilerType="Joint"

    stateTaxBracket = TaxBracket.objects.all().filter(taxType="State", filerType=userFilerType, state=userState)

    for e in stateTaxBracket :
      print("Range Max " + str(e.rangeMax))
      rowTaxAmount = 0
      if income < e.rangeMax : #last income row
        #print("last income row")
        taxableIncome = income - prevRangeMax
        rowTaxAmount = taxableIncome * e.rangeRate
        stateTaxAmount = stateTaxAmount + rowTaxAmount
        break;
      elif (e.rangeMax == 0) :
        #print("last range row")
        taxableIncome = income - prevRangeMax
      else : # all other rows
        #print("middle rows")
        taxableIncome = e.rangeMax - prevRangeMax
      prevRangeMax = e.rangeMax
      rowTaxAmount = taxableIncome * e.rangeRate
      stateTaxAmount = stateTaxAmount + rowTaxAmount
      # print("ID: " + str(e.id) + " RangeMax: " + str(e.rangeMax) + " RangeRate: " + str(e.rangeRate) +
      #    " TaxableIncome = " + str(taxableIncome) + " State Tax = " + str(stateTaxAmount))

    percentage = (stateTaxAmount / income) * 100
    print("State Tax Percentage: " + str(percentage))

    return stateTaxAmount;

  # BEGINNING OF THE METHOD getFederalStandardDeduction
  def getFederalStandardDeduction () :
    standardDeduction = 25100
    return standardDeduction

  # BEGINNING OF THE METHOD getStateStandardDeduction
  def getStateStandardDeduction (userFilerType, userState) :

    if userFilerType == "Head" :
      userFilerType="Joint"

    stateDeduction = StateDeduction.objects.all().filter(state=userState)
    for e in stateDeduction :
      if userFilerType == "Single" :
        standardDeduction = e.singleAmount
      else :
        standardDeduction = e.coupleAmount
    return standardDeduction

  def getFederalTaxBracket (userFilerType):
    fedTaxBracket = TaxBracket.objects.all().filter(taxType="Federal", filerType=userFilerType)
    for n in range(len(fedTaxBracket)):
      fedTaxBracket[n].rangeRate = round(100 * fedTaxBracket[n].rangeRate, 2)

    return fedTaxBracket

  def getStateTaxBracket (userFilerType, userState):
    if userFilerType == "Head" :
      userFilerType="Joint"

    stateTaxBracket = TaxBracket.objects.all().filter(taxType="State", filerType=userFilerType, state=userState)

    # if len(stateTaxBracket) == 0:
    #   print("List is empty")

    for n in range(len(stateTaxBracket)):
      stateTaxBracket[n].rangeRate = round(100 * stateTaxBracket[n].rangeRate, 2)

    return stateTaxBracket
