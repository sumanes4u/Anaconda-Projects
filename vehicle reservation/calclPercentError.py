##def f(expected, actual):
##    diff = abs(expected - actual)
##    percent_err = ((expected - (expected - diff)) / expected) * 100
##    return percent_err

def f(expected, actual):
    percent_err = ((abs(expected - actual) - 86400) / expected) * 100
    return percent_err
   
    
