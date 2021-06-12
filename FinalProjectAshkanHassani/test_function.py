import epi_calculator_functions as epi
import epi_calc_GUI as calc


assert epi != None
assert calc != None

x = epi.cohort(1,2,3,4, disease = "Test", exposure = "Sample") != None
assert x != None

y = epi.case_control(1,2,3,4, disease = "Test", exposure = "Sample") != None
assert y != None

z = epi.cross_sectional(1,2,3,4, disease = "Test", exposure = "Sample") != None
assert z != None

print ("Please run epi_calc_GUI to access the Epidemiology Calculator")