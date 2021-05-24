# this is for Dict
def display_all(this_dict):
    for name, val in this_dict.items():
        print('%s %s' % (val, 'is the capital of'), name)


def get_capital_city(province_name, this_dict):
    capital = this_dict[province_name]
    return capital


def add_element(province_name, capital_city, this_dict):
    this_dict[province_name] = capital_city


def remove_item(province_name, this_dict):
    del this_dict[province_name]


# read thoroughly
def get_total_population(the_dict):
    sum = 0
    for key in the_dict:
        sum += the_dict[key]["population"]
    return sum


# read thoroughly
def get_another_capital_city(province, this_dict):
    if province == '':
        return ''
    return this_dict[province]['capital'].capitalize()


# read thoroughly
def get_largest_city(province_name, this_dict):
    if province_name == '':
        return ''
    return this_dict[province_name]['largest'].capitalize()


# read thoroughly
def get_smallest_province(this_dict):
    a = min(this_dict)
    for i in this_dict:
        if this_dict[i]['population'] == a:
            return i.capitalize()


# read thoroughly
def get_largest_province(this_dict):
    a = max(this_dict)
    for i in this_dict:
        if this_dict[i]['population'] == a:
            return i.capitalize()


# read thoroughly
def get_province_description(province_name, this_dict):
    print(
        f"{province_name.capitalize()} has a population of {this_dict[province_name]['population']} whose capital is {this_dict[province_name]['capital']} and largest city is {this_dict[province_name]['largest']}.")
