import numpy as np

def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    """
    Compute the derivative of the product of two polynomials.
    
    Args:
        f_coeffs: Coefficients of polynomial f, where f_coeffs[i] is the coefficient of x^i
        g_coeffs: Coefficients of polynomial g, where g_coeffs[i] is the coefficient of x^i
    
    Returns:
        Coefficients of (f*g)' as a list of floats rounded to 4 decimal places
    """
    polynomial_mult = []
    derivative = []
    for i in range(len(f_coeffs) + len(g_coeffs) - 1):
        polynomial_mult.append(0)

    for idx_f, f_coeff in enumerate(f_coeffs):
        for idx_g, g_coeff in enumerate(g_coeffs):
            polynomial_mult[idx_f + idx_g] += f_coeff * g_coeff

    for idx, coeff in enumerate(polynomial_mult):
        if len(polynomial_mult) == 1:
            derivative.append(round(idx * coeff, 4))
        elif len(polynomial_mult) > 1:
            if idx == 0:
                continue
            else:
                derivative.append(round(idx * coeff, 4))

    return derivative                

            