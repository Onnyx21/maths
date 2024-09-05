from arithmetique import pgcd


def get_alpha_and_beta(a: int, b: int, c: int) -> tuple[float, float]:
    if a != 0:
        alpha = -b/(2*a)
        beta = -(b*b-4*a*c)/(4*a)
        return alpha, beta


def get_coefficiants(polynom: str):
    polynom = polynom.replace('x²', 'x^2').replace(' ', '')

    a, b, c = 0, 0, 0

    if 'x^2' in polynom:
        pos_x2 = polynom.index('x^2')
        if pos_x2 == 0 or polynom[pos_x2 - 1] in '+-':
            a = int(polynom[:pos_x2].replace('+', '1').replace('-', '-1') or '1')
        else:
            a = int(polynom[:pos_x2])
        polynom = polynom[pos_x2 + 3:]

    if 'x' in polynom:
        pos_x = polynom.index('x')
        if pos_x == 0 or polynom[pos_x - 1] in '+-':
            b = int(polynom[:pos_x].replace('+', '1').replace('-', '-1') or '1')
        else:
            b = int(polynom[:pos_x])
        polynom = polynom[pos_x + 1:]

    if polynom:
        c = int(polynom)

    return tuple(filter(lambda x: x != 0 or (x == 0 and (a != 0 or b != 0 or c != 0)), [a, b, c]))


def decimal_to_fraction(decimal):
    decimal_str = str(decimal)

    # Trouver la position de la virgule
    if '.' in decimal_str:
        decimals = len(decimal_str.split('.')[1])
    else:
        decimals = 0

    denom = 10 ** decimals

    num = int(decimal * denom)

    gcd = pgcd(num, denom)

    num //= gcd
    denom //= gcd

    return f"{num}/{denom}"


polynom = input('Please enter the polynom: ')
a, b, c = get_coefficiants(polynom)
alpha, beta = get_alpha_and_beta(a, b, c)

if not isinstance(alpha, int):
    alpha = f'({decimal_to_fraction(alpha)})'

if not isinstance(beta, int):
    beta = f'({decimal_to_fraction(beta)})'

if '-' not in str(beta):
    beta = '+' + str(beta)
else:
    beta = beta.replace('-', '')
    beta = '-' + beta

print(f'{a}(x-{alpha}){beta}')

