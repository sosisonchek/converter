
units_temp = [
    {'type': 'temp', 'alias': 'c', 'fullname': ' celcius', 'factor': 1, 'offset': 0},
    {'type': 'temp', 'alias': 'f', 'fullname': ' fahrenheit', 'factor': 1.8, 'offset': 32},
    {'type': 'temp', 'alias': 'k', 'fullname': ' kelvin', 'factor': 1, 'offset': 273.15}

]
units_distance = [
    {'type': 'distance','alias': 'km', 'fullname': ' kilometres', 'factor': 0.001},
    {'type': 'distance','alias': 'm', 'fullname': ' metres', 'factor': 1},
    {'type': 'distance', 'alias': 'mi', 'fullname': ' miles', 'factor': 0.000621371192},
    {'type': 'distance', 'alias': 'in', 'fullname': ' inches', 'factor': 39.3700787},
    {'type': 'distance', 'alias': 'ft', 'fullname': ' feet', 'factor': 3.2808399},
    {'type': 'distance', 'alias': 'yd', 'fullname': ' yards', 'factor': 1.0936133}
]
units_weight = [
    {'type': 'weight', 'alias': 'kg', 'fullname': ' kilograms', 'factor': 1},
    {'type': 'weight', 'alias': 'lb', 'fullname': ' pounds', 'factor': 2.20462262},
    {'type': 'weight', 'alias': 'oz', 'fullname': ' ounces', 'factor': 35.2739619}
]
units = units_temp + units_distance + units_weight

def convertion(n: str, measurement: str):
    n: int = int(n) # 😍
    measurement = measurement.lower()
    result = []
    for unit in units:
        if unit['alias'] == measurement:
            source = unit
    for unit in units:
        if unit['type'] == source['type']:
            if unit['alias'] == measurement:
                final_n = n
            elif unit['type'] == 'temp':
                # базовое значение - градусы цельсия
                base = (n - source['offset']) / source['factor']
                final_n = base * unit['factor'] + unit['offset']

            else: final_n = (n / source['factor']) * unit['factor']
            result.append(str(round(final_n, 3)) + unit['fullname'])
    return result

def user_input():
    user = input()
    num, string = '', ''

    for i in user:
        if i.isdigit(): num += i
        else: string += i
    return num,string
print("example: 10 kg")

while True:
    try:
        result = convertion(*user_input())
        print('convertion results:')
        for r in result:
            print(r)
    except (TypeError, IndexError, UnboundLocalError): print('wrong input!!!')