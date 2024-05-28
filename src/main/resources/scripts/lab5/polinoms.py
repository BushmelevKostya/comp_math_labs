import re
from collections import defaultdict


def parse_polynomial(poly_str):
    poly_str = poly_str.replace(" ", "").replace("(", "").replace(")", "")

    terms = re.findall(r'([+-]?[^-+]+)', poly_str)

    coefficients = defaultdict(int)

    for term in terms:
        if 'x' in term:
            if '^' in term:
                coeff, exp = term.split('x^')
                exp = int(exp)
            else:
                coeff = term.split('x')[0]
                exp = 1
        else:
            coeff = term
            exp = 0

        if coeff in ['', '+']:
            coeff = 1
        elif coeff == '-':
            coeff = -1
        else:
            coeff = float(coeff)

        coefficients[exp] += coeff

    max_degree = max(coefficients.keys()) if coefficients else 0
    poly_list = [0] * (max_degree + 1)
    for degree, coeff in coefficients.items():
        poly_list[degree] = coeff

    return poly_list


def multiply_polynomials(poly1, poly2):
    degree1 = len(poly1)
    degree2 = len(poly2)

    result_degree = degree1 + degree2 - 1
    result = [0] * result_degree

    for i in range(degree1):
        for j in range(degree2):
            result[i + j] += poly1[i] * poly2[j]

    return result


def plus_polynomials(poly1, poly2):
    degree1 = len(poly1)
    degree2 = len(poly2)

    result_degree = max(degree1, degree2)
    result = [0] * result_degree

    for i in range(result_degree):
        try:
            result[i] += poly1[i] + poly2[i]
        except IndexError:
            result[i] += poly1[i] if degree1 > degree2 else poly2[i]
    return result


def polynomial_to_string(poly):
    terms = []
    for exponent, coeff in reversed(list(enumerate(poly))):
        if coeff == 0:
            continue
        if exponent == 0:
            terms.append(f"{coeff}")
        elif exponent == 1:
            terms.append(f"{coeff}x")
        else:
            terms.append(f"{coeff}x^{exponent}")

    result = ' + '.join(terms)
    result = result.replace('+ -', '- ')
    return result


def multiply_polynomial_strings(poly_str1, poly_str2):
    poly1 = parse_polynomial(poly_str1)
    poly2 = parse_polynomial(poly_str2)
    result_poly = multiply_polynomials(poly1, poly2)
    return polynomial_to_string(result_poly)


def plus_polynomial_strings(poly_str1, poly_str2):
    poly1 = parse_polynomial(poly_str1)
    poly2 = parse_polynomial(poly_str2)
    result_poly = plus_polynomials(poly1, poly2)
    result_poly = [round(p, 3) for p in result_poly]
    return polynomial_to_string(result_poly)
