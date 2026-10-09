import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    g_x = np.polyval(g_coeffs, x)
    h_x = np.polyval(h_coeffs, x)
    
    
    g_diff = np.polynomial.polynomial.polyder(g_coeffs[::-1])
    h_diff = np.polynomial.polynomial.polyder(h_coeffs[::-1])

    g_diff_x = np.polyval(g_diff[::-1], x)
    h_diff_x = np.polyval(h_diff[::-1], x)

    return (g_diff_x * h_x - h_diff_x * g_x) / (h_x ** 2)
    
   

        