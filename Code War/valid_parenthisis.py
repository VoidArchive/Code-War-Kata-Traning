# Write a function that takes a string of parentheses,
# and determines if the order of the parentheses is valid. 
# The function should return true if the string is valid, and false if it's invalid.

# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true

def valid_parentheses(string):
    open_braket = '('
    close_braket = ')'
    stack = []
    for i in string:
        if i in open_braket:
            stack.append(i)
        elif i in close_braket:
            try:
                stack.pop()
            except:
                return False
    
    if len(stack) == 0:
        return True
    else:
        return False




