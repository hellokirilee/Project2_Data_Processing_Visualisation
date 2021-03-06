import json
import plotly.express as px
import plotly.io as pio
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

forecast = []

def process_weather(forecast_file):
    with open(forecast_file) as json_file:
        json_data = json.load(json_file)
    for weather in json_data['DailyForecasts']:
        date_input = (weather["Date"])
        date = convert_date(date_input)
        max_temp_f = (weather["Temperature"]["Maximum"]["Value"])
        max_temp_c = convert_f_to_c(max_temp_f)
        min_temp_f = (weather["Temperature"]["Minimum"]["Value"])
        min_temp_c = convert_f_to_c(min_temp_f)
        real_feel = (weather["RealFeelTemperature"]["Minimum"]["Value"])
        rfmin = convert_f_to_c(real_feel)
        real_feel_shade = (weather["RealFeelTemperatureShade"]["Minimum"]["Value"])
        rfminshade = convert_f_to_c(real_feel_shade)
       
        days = {'Date': date, 'Maximum': max_temp_c, 'Minimum': min_temp_c, 'Minimum Real Feel':rfmin, 'Minimum Real Feel Shade':rfminshade}

        forecast.append (days)

process_weather('data/forecast_5days_b.json')

fig1 = px.line(
    forecast,  
    x= "Date",
    y= ["Minimum", "Maximum"],
    title="Forecast",
    labels={
    "date": "Date"})

fig1.update_layout(
    template = "plotly_dark",
    yaxis_title = "Temperature (C)",
    legend_title = "Temperature",

)

fig1.update_traces(mode="lines+markers")

fig1.show()
#minrf & minrfshade actually have same values - may look like one line in graph
fig2 = px.line(
    forecast,
    x= "Date",
    y= ["Minimum", "Minimum Real Feel", "Minimum Real Feel Shade"],
    title="Forecast",
    labels={
    "date": "Date"})

fig2.update_layout(
    template = "plotly_dark",
    yaxis_title = "Temperature (C)",
    legend_title = "Temperature",

)

fig2.update_traces(mode="lines+markers")

fig2.show()