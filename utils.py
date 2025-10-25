def format_currency(value):
    return f"${value:,.2f}"

def risky_eval(expr):
    # Intentional vulnerability for Bandit: using eval()
    return eval(expr)
