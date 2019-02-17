def expression(number, operation):
     if not operation:
        return number;
     return operation(number)

def zero(operation):
    return expression(0, operation)

def one(operation):
    return expression(1, operation)

def two(operation):
    return expression(2, operation)

def three(operation):
    return expression(3, operation)

def four(operation):
    return expression(4, operation)

def five(operation):
    return expression(5, operation)

def six(operation):
    return expression(6, operation)

def seven(operation):
    return expression(7, operation)

def eight(operation):
    return expression(8, operation)

def nine(operation):
    return expression(9, operation)

def plus(a):
    return lambda x: x + a()


def minus(a):

  return lambda x:x - a()

def times(a):

    return lambda x: x * a()

