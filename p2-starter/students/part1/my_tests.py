test_temp = 100
def convert_f_to_c(temp_in_farenheit):
    a = temp_in_farenheit - 32
    b = a * 5
    c = b/9
    print(c)
    return(c)


    """Converts an temperature from farenheit to celcius
    
    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
d = convert_f_to_c(test_temp)
print(d)


    """Day 1, get temp
        max_mean_calc = max_mean_calc + max_temp_c    
        if max_temp_c > highest_temp
            highest_temp = max_temp_c"""
