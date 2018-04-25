import sympy as sp

def convert_ocr_to_string(text):
    text = text.lower()
    text = text.replace('/\\','^')
    text = text.replace('"','^')
    text = text.replace('e^x','exp(x)')
    text = text.replace('e^2x','exp(2*x)')

    text = text.replace('2x','2*x')
    text = text.replace('2c','2*c')
    text = text.replace('2s','2*s')
    text = text.replace('2l','2*l')
    text = text.replace('2e','2*e')
    text = text.replace('2t','2*t')
    text = text.replace('2(','2*(')

    text = text.replace('3x','3*x')
    text = text.replace('3c','3*c')
    text = text.replace('3s','3*s')
    text = text.replace('3l','3*l')
    text = text.replace('3e','3*e')
    text = text.replace('3t','3*t')
    text = text.replace('3(','3*(')

    text = text.replace('4x','4*x')
    text = text.replace('4c','4*c')
    text = text.replace('4s','4*s')
    text = text.replace('4l','4*l')
    text = text.replace('4e','4*e')
    text = text.replace('4t','4*t')
    text = text.replace('4(','4*(')

    text = text.replace('5x','5*x')
    text = text.replace('5c','5*c')
    text = text.replace('5s','5*s')
    text = text.replace('5l','5*l')
    text = text.replace('5e','5*e')
    text = text.replace('5t','5*t')
    text = text.replace('5(','5*(')

    text = text.replace('6x','6*x')
    text = text.replace('6c','6*c')
    text = text.replace('6s','6*s')
    text = text.replace('6l','6*l')
    text = text.replace('6e','6*e')
    text = text.replace('6t','6*t')
    text = text.replace('6(','6*(')

    text = text.replace('7x','7*x')
    text = text.replace('7c','7*c')
    text = text.replace('7s','7*s')
    text = text.replace('7l','7*l')
    text = text.replace('7e','7*e')
    text = text.replace('7t','7*t')
    text = text.replace('7(','7*(')

    text = text.replace('8x','8*x')
    text = text.replace('8c','8*c')
    text = text.replace('8s','8*s')
    text = text.replace('8l','8*l')
    text = text.replace('8e','8*e')
    text = text.replace('8t','8*t')
    text = text.replace('8(','8*(')

    text = text.replace('9x','9*x')
    text = text.replace('9c','9*c')
    text = text.replace('9s','9*s')
    text = text.replace('9l','9*l')
    text = text.replace('9e','9*e')
    text = text.replace('9t','9*t')
    text = text.replace('9(','9*(')

    text = text.replace('sum', '^')

    text = text.replace('le','lo')
    text = text.replace('la','lo')
    text = text.replace('l0','lo')
    text = text.replace('t0','to')
    text = text.replace('tog','log')
    text = text.replace('1og','log')

    text = text.replace('ce','co')
    text = text.replace('ca','co')
    text = text.replace('c0','co')

    text = text.replace('to','ta')
    text = text.replace('te','ta')
    text = text.replace('tah','tan')

    text = text.replace('ih','in')
    text = text.replace('5in', 'sin')
    text = text.replace('gin', 'sin')
    text = text.replace('sln','sin')

    text = text.replace('(e)^(x)','exp(x)')
    text = text.replace('(e)^(2*x)','exp(2*x)')
    text = text.replace('(e)^(3*x)','exp(3*x)')
    text = text.replace('(e)^(4*x)','exp(4*x)')
    text = text.replace('(e)^(5*x)','exp(5*x)')
    text = text.replace('(e)^(6*x)','exp(6*x)')
    text = text.replace('(e)^(7*x)','exp(7*x)')
    text = text.replace('(e)^(8*x)','exp(8*x)')
    text = text.replace('(e)^(9*x)','exp(9*x)')
    text = text.replace('(e)^(-x)','exp(-x)')

    text = text.replace('cx','(x')
    return text

def integrate_from_string(integrable_function):
    f = sp.sympify(integrable_function)
    return sp.integrate(f)

s = 'sin(2x)+t0g(x)'
integrable_function = convert_ocr_to_string(s)
integral = integrate_from_string(integrable_function)
print 'Integral = %s' % integral
