import json


def process():
    file = open("weatherData.json", "r+")
    x = file.read()
    file.close()
    y = json.loads(x)
    current_name_list = ["Current temperature", "current pressure", "current humidity: ", "current wind speed: "]
    current_data_list = [y['current']['temp'], y['current']['pressure'], y['current']['humidity'], y['current']['wind_speed']]

    for x in range(4):
        print(current_name_list[x] + ": " + str(current_data_list[x]))

    max_temp_data_list = []
    min_temp_data_list = []
    pop_data_list = []
    humidity_data_list = []
    pressure_data_list = []
    for x in range(8):
        max_temp_data_list.append(int(y['daily'][x]['temp']['max']))
        min_temp_data_list.append(int(y['daily'][x]['temp']['min']))
        pop_data_list.append(int(y['daily'][x]['pop']))
        humidity_data_list.append(y['daily'][x]['humidity'])
        pressure_data_list.append(y['daily'][x]['pressure'])
    print()

    for x in range(8):
        print("max temperature: " + str(max_temp_data_list[x]))
        print("min temperature: " + str(min_temp_data_list[x]))
        print("probability of precipitation: " + str(pop_data_list[x]))
        print("humidity: " + str(humidity_data_list[x]))
        print("pressure: " + str(pressure_data_list[x]))
        print()
    print()


process()
