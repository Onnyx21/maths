from sympy import symbols, diff, sympify


def parse_expr(expr: str) -> str:
    expr = expr.replace(' ', '')  # Delete spaces
    expr = expr.replace('x', '*x')  # Add '*' before each 'x'

    # Make sure multiplication is not reapeted
    expr = expr.replace('**x', '*x').replace('*+x', '+x').replace('*-x', '-x')

    # If first term is a multiplication, then remove '*'
    if expr.startswith('*x'):
        expr = expr[1:]

    expr = expr.replace('²', '**2')
    expr = expr.replace('/*', '/')
    return expr


def render_expr(expr: str) -> str:
    expr = expr.replace('*', '')
    return expr


def get_derivated(f):

    f = parse_expr(f)
    char_count = 0

    for char in f:
        if char.isalpha() and char_count == 0:
            letter = char
            char_count += 1
        elif char.isalpha():
            print('Invalid expresion')
            quit()

    symbol = symbols(letter)

    expression = sympify(f)
    # Calculate the derivate
    derivated_function = diff(expression, symbol)

    return render_expr(str(derivated_function))


print(parse_expr('1/x'))
function = input('f(x) = ')
print(f'f\'(x) = {get_derivated(function)}')


