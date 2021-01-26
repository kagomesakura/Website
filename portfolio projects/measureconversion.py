def units_variations(units):
    if units in ['m', 'meter', 'meters']:
        return 'm'
    elif units in ['yd', 'yard', 'yards']:
        return 'yd'
    elif units in ['in', 'inch', 'inches']:
        return 'in'
    elif units in ['mi', 'mile', 'miles']:
        return 'mi'
    elif units in ['ft', 'feet']:
        return 'ft'
    elif units in ['km', 'kilometer', 'kilometers']:
        return 'km'

def meters_to(distance, units):
    if units == 'm':
        return distance
    elif units == 'mi':
        return distance * 1609.34
    elif units == 'ft':
        return distance * 0.3048
    elif units == 'km':
        return distance * 1000
    elif units == 'yd':
        return distance * 0.9144
    elif units == 'in':
        return distance * 0.0254

def meters_from(distance, units):
    if units == 'm':
        return distance
    elif units == 'mi':
        return distance / 1609.34
    elif units == 'ft':
        return distance / 0.3048
    elif units == 'km':
        return distance / 1000
    elif units == 'yd':
        return distance / 0.9144
    elif units == 'in':
        return distance / 0.0254

def main():
    distance = float(input('Please type in a distance...'))
    units_in = input('What units are you converting from? ')
    units_out = input('What units are you converting to? ')

    units_in = units_variations(units_in)
    units_out = units_variations(units_out)
    distance_in_m = meters_to(distance, units_in)
    distance_out_m = meters_from(distance_in_m, units_out)

    output = f'{distance} {units_in} is {distance_out_m} {units_out}'
    print(output)
main()


# 1 yard is 0.9144 m
# 1 inch is 0.0254 m

#def yard_in(distance, units)
