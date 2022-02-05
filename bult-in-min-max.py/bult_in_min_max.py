def maximum(value1, value2, value3):
    """Return the maximum of three values."""
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value

MaximumValue = maximum(12,27,36)
print('Maximum Value is: ',MaximumValue)

def minimum(value1, value2, value3):
    """Return the minimum of three values."""
    min_value = value1
    if value2 < min_value:
        min_value = value2
    if value3 < min_value:
        min_value = value2
    return min_value

MinimumValue = minimum (15, 9, 27)
print('Minimum Value is: ',MinimumValue)