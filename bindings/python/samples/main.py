def list_of_values(min_value, max_value):
    """Create a list of five values between current_priceand y"""
    step = (min_value - max_value) / 5
    return list(range(round(min_value), round(max_value), abs(round(step))))


if __name__ == '__main__':
    list_of_values(100.73, 176.65)
