import holidayapi

hapi = holidayapi.v1('9a97319d-d5be-4802-99a6-f76df98e1338')

parameters = {
    'country':'IN',
    'year': 2016
}

holidays = hapi.holidays(parameters)
print(holidays)
