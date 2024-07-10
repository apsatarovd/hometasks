def calculator(a, operator, b):
    if operator == "+":
       plus = a + b
       result = plus 
    elif operator == "-":
        minus = a - b
        result = minus
    elif operator == "*":
        multi = a * b
        result = multi
    elif operator == "/":
        division = a / b 
        result = division
    else: 
        result = None
        print("не решается")
    
    return result
