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

def calc_mean(total, num_items):
        x = total/num_items
        format_mean = round(x,1)
        mean = format_temperature(format_mean)
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
        #gather number of days, and dates
        num_items = num_items + 1

        date_input = (weather["Date"])
        date = convert_date(date_input)
        #calculate minimum 
        min_temp_f = (weather["Temperature"]["Minimum"]["Value"])
        min_temp_c = convert_f_to_c(min_temp_f)
        #adds values to preform calc
        min_mean_calc = min_mean_calc + min_temp_c
        #returns calculated & formatted mean
        low_mean = calc_mean(min_mean_calc, num_items)

        #determines lowest temp & day
        if min_temp_c < lowest_temp:
            lowest_temp = min_temp_c
            low_day = (date)
            low_day_temp = format_temperature(min_temp_c)


        #calculate minimum 
        max_temp_f = (weather["Temperature"]["Maximum"]["Value"])
        max_temp_c = convert_f_to_c(max_temp_f)
        #adds values to preform calc
        max_mean_calc = max_mean_calc + max_temp_c
        #returns calculated & formatted mean

        high_mean = calc_mean(max_mean_calc, num_items)
        #determines lowest temp & day
        if max_temp_c > highest_temp:
            highest_temp = max_temp_c
            high_day = (date)
            high_day_temp = format_temperature(max_temp_c)


    output_string = f"""{num_items} Day Overview
    The lowest temperature will be {low_day_temp}, and will occur on {low_day}.
    The highest temperature will be {high_day_temp}, and will occur on {high_day}.
    The average low this week is {low_mean}.
    The average high this week is {high_mean}.\n"""
    with open("test.txt", "a") as txt_file: 
        for weather in json_data['DailyForecasts']:
            min_temp_f = (weather["Temperature"]["Minimum"]["Value"])
            min_temp_c = convert_f_to_c(min_temp_f)
            max_temp_f = (weather["Temperature"]["Maximum"]["Value"])
            max_temp_c = convert_f_to_c(max_temp_f)
            date_input = (weather["Date"])
            date = convert_date(date_input)
            long_boy = (weather["Day"]["LongPhrase"])
            rain_chance = (weather["Day"]["RainProbability"])
            long_boy_pm = (weather["Night"]["LongPhrase"])
            rain_chance_pm = (weather["Night"]["RainProbability"])
            max_temp = format_temperature(max_temp_c)
            min_temp = format_temperature(min_temp_c)

            output_string += f"""
-------- {date} --------
Minimum Temperature: {min_temp}
Maximum Temperature: {max_temp}
Daytime: {long_boy}
    Chance of rain:  {rain_chance}%
Nighttime: {long_boy_pm}
    Chance of rain:  {rain_chance_pm}%\n"""




    output_string += "\n"
    return output_string

    with open("test.txt", "w") as txt_file:
        txt_file.write(output_string)


if __name__ == "__main__":
    print(process_weather("data/forecast_10days.json"))
