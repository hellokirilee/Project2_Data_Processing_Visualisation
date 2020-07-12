import json 

from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"



def format_temperature(temp):
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return (d.strftime('%A %d %B %Y'))

def convert_f_to_c(temp_in_farenheit):
    a = temp_in_farenheit - 32
    b = a * 5
    c = b/9
    d = round(c,1)
    return(d)
    
def calculate_mean(total, num_items):
        x = total/num_items
        mean = round(x,1)
        return (mean)

def process_weather(forecast_file):
    with open(forecast_file) as json_file:
        json_data = json.load(json_file)
        highest_temp = 0
        lowest_temp = 50
        max_mean_calc = 0
        min_mean_calc = 0
        num_items = 0
        line = []

    for weather in json_data['DailyForecasts']:
        min_temp_f = (weather["Temperature"]["Minimum"]["Value"])
        max_temp_f = (weather["Temperature"]["Maximum"]["Value"])
        num_items = num_items + 1
        max_temp_c = convert_f_to_c(max_temp_f)
        max_mean_calc = max_mean_calc + max_temp_c
        if max_temp_c > highest_temp:
            highest_temp = max_temp_c
        min_temp_c = convert_f_to_c(min_temp_f)
        if min_temp_c < lowest_temp:
            lowest_temp = min_temp_c
        min_mean_calc = min_mean_calc + min_temp_c
        high_mean = calculate_mean(max_mean_calc, num_items)
        low_mean = calculate_mean(min_mean_calc, num_items)
        date_input = (weather["Date"])
        date = convert_date(date_input)
        # min_temp_f = (weather["Temperature"]["Minimum"]["Value"])
        # max_temp_f = (weather["Temperature"]["Maximum"]["Value"])
        long_boy = (weather["Day"]["LongPhrase"])
        rain_chance = (weather["Day"]["RainProbability"])
        long_boy_pm = (weather["Night"]["LongPhrase"])
        rain_chance_pm = (weather["Night"]["RainProbability"])
        num_items = num_items + 1
        max_temp_c = convert_f_to_c(max_temp_f)
        max_mean_calc = max_mean_calc + max_temp_c
        if max_temp_c > highest_temp:
            highest_temp = max_temp_c
        min_temp_c = convert_f_to_c(min_temp_f)
        if min_temp_c < lowest_temp:
            lowest_temp = min_temp_c
        min_mean_calc = min_mean_calc + min_temp_c
        max_temp = format_temperature(max_temp_c)
        min_temp = format_temperature(min_temp_c)
            #print statements
    
                
    # print(f"Number items{num_items}, High Temp {highest_temp}, Low Temp {lowest_temp}, Low mean {low_mean}, high mean {high_mean}")
        print(f"-------- {date} --------\n")
        print (f"Minimum Temperature: {min_temp} \n \nMaximum Temperature: {max_temp}\n")
        print(f"Daytime: {long_boy} \n\n\t Chance of rain: {rain_chance}%\n")
        print(f"Nighttime: {long_boy_pm} \n\n\t Chance of rain: {rain_chance_pm}%\n")
# with open("test.txt", "w") as txt_file:
#     for weather in json_data['DailyForecasts']:
#      txt_file.write(f"Number items{num_items}, High Temp {highest_temp}, Low Temp {lowest_temp}, Low mean {low_mean}, high mean {high_mean}")


    """Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
        """

process_weather('data/forecast_5days_a.json')