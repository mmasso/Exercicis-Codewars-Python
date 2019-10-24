def weather_info(temperature):
    celsius = convertToCelsius(temperature)
    celsius = float(celsius)
    if celsius < 0:
        celsius = "{} is freezing temperature".format(celsius)
        return celsius
    else:
        celsius = "{} is above freezing temperature".format(celsius)
        return celsius


def convertToCelsius(temperature):
    celsius = (temperature - 32) * 5 / float(9)
    return celsius


print(convertToCelsius(347))

print(weather_info(347))