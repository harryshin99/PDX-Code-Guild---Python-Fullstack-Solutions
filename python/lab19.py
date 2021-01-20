import re
import requests
import math


def get_data(url):
    response = requests.get(url)
    data = response.text
    return data

def get_data_list(url):
    data = get_data(url)
    date_data = re.findall(r'\d+-\w+-\d+\s+\d+', data)

    data_list = []

    for index in range(len(date_data)):
        date_sep_data = date_data[index].split()
        rain_info = {
            'Date': date_sep_data[0],
            'Rainfall': int(date_sep_data[1])
        }
        data_list.append(rain_info)
    return data_list

def get_mean(data_list):
    sum = 0
    for index in range(len(data_list)):
        sum += (data_list[index]['Rainfall'])
    return round(sum/len(data_list), 2)

def get_standard_dev(mean, data_list):
    sum = 0.0
    for index in range(len(data_list)):
        sum += ((data_list[index]['Rainfall']) - mean) ** 2
    sum = sum / len(data_list)
    sum = math.sqrt(sum)
    return round(sum, 2)
    
def get_stand_dev_range(standard_dev, data_list):
    within_range = []
    for index in range(len(data_list)):
        if standard_dev - 1 < data_list[index]['Rainfall'] < standard_dev + 1:
            within_range.append(data_list[index]['Rainfall'])
    return round(((len(within_range) / len(data_list)) * 100), 2)

def get_most_rain(data_list):
    most_rain = 0
    for index in range(len(data_list)):
        if int(data_list[index]['Rainfall']) > most_rain:
            # print(most_rain)
            most_rain = int(data_list[index]['Rainfall'])
            output = f"Date: {data_list[index]['Date']} Rainfall: {data_list[index]['Rainfall']} inches."
    return output

url = 'https://or.water.usgs.gov/non-usgs/bes/glencoe.rain'

data_list = get_data_list(url)

mean = get_mean(data_list)

standard_dev = get_standard_dev(mean, data_list)

stand_dev_range = get_stand_dev_range(standard_dev, data_list)

most_rain = get_most_rain(data_list)

print(f"The average daily rainfall is {mean} inches.")
print(f"The standard deviation is {standard_dev:.2f}.")
print(f"{stand_dev_range}% of the data falls within 1 standard deviation of the mean.")
print(most_rain)