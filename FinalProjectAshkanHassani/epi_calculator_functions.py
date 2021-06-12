
#            Disease (+) | Disease (-)
#             _________________________
# Exposed (+)|----A-------|----B------| 
#            |________________________|
# Exposed (-)|----C-------|----D------| 
#            |________________________|            




def cohort(a, b, c, d, disease = "DISEASE", exposure = "EXPOSURE"):
    
   """perform risk ratio calcualtion
    
    Parameters
    ----------
 a,b,c,d : integer 
 inputs from the 2x2 table
 Exposure : string
     optional, lets you assign the exposure
 Disease : string
     optional, lets you assign the disease name
    Returns
    -------
    prints : string
        The interpetation  of the calculation. 
    """    

   if a or b or c or d == 0:
        a += 0.5
        b += 0.5
        c += 0.5
        d += 0.5    
        # Adds 0.5 to all inputs in case of 0 as per CDC guidelines 

   incidence_exposed = a/(a+b)
   incidence_unexposed = c/(c+d)
   #incidence_population = (a + c)/(a + b + c + d)
   riskratio = incidence_exposed/ incidence_unexposed
    
   print ("RR: People with " + exposure + " are " + str(round(riskratio, 2)) + " times more likely to get " + disease + " than people with low " + exposure + ".")
       
def case_control (a, b, c, d, disease = "DISEASE", exposure = "EXPOSURE"):
    
   """perform odds ratio calcualtion amd returns meaning
    
    Parameters
    ----------
 a,b,c,d : integer 
 inputs from the 2x2 table
 Exposure : string
     optional, lets you assign the exposure
 Disease : string
     optional, lets you assign the disease name
    Returns
    -------
    prints : string
        The interpetation  of the calculation. 
    """  
    
   if a or b or c or d == 0:
       a += 0.5
       b += 0.5
       c += 0.5
       d += 0.5    
    
    #  proportion of cases who were exposed compared to the proportion of noncases who were not exposed
  
   odds_ratio = (a * d)/(c * b)
    
   print(" OR: The odds of " + disease + " among those exposed to " + exposure + " is " + str(round(odds_ratio, 2) * 100) + " percent less than among those without the exposure")

def cross_sectional(a, b, c, d, disease = "DISEASE", exposure = "EXPOSURE"):

    if a or b or c or d == 0:
      a += 0.5
      b += 0.5
      c += 0.5
      d += 0.5    
    prevalence_ratio = (a / a + b) / (c / c + d) 
    # Prevalance of Disease in exposed/ Prevalence of Disease in unexposed
    prevalence_odds_ratio =  (a/b)/(c/d)
    # Prevalence of Odds of disease in exposed/ Prevalence of odds of disease in not exposed
    print (" PR: The prevalence odds of " + disease + " increase " + str(round(prevalence_ratio, 2)) + " fold among those with " + exposure + ".")  
    print (" POR: People with higher " + exposure + " are " + str(round(prevalence_odds_ratio, 2)) + " time(s) more likely to get  " + disease + "  than those with lower " + exposure + ".")

    """perform prevalence ration AND prevalence odds ratio calcualtion and returns meaning
    
    Parameters
    ----------
 a,b,c,d : integer 
 inputs from the 2x2 table
 Exposure : string
     optional, lets you assign the exposure
 Disease : string
     optional, lets you assign the disease name
    Returns
    -------
    prints : string
        The interpetation  of the calculation. 
    """  


#GUI notes that I used: https://www.geeksforgeeks.org/python-gui-tkinter/




#Expansion can include:
    # Including confidence intervals 
        # https://select-statistics.co.uk/calculators/confidence-interval-calculator-odds-ratio/
        # https://www.geeksforgeeks.org/log-functions-python/
           #ci1 = math.log(odds_ratio) 
           #ci2 = math.log(odds_ratio)
    # measures of validity
    # Sensitivity = TP/ TP + FN
    # Specificiy = TN/ TN + FP
    # PPV = TP/(TP+FP) #PPV: for those who test positive for the test how likely do they actually have the disease.
    # NPV = TN/ (TN/+FN) #Negative Predictive value: what is the probability among patients who test negative to actually not have the disease 
