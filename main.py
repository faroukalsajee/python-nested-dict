from utilities_dict import get_capital_city, display_all, add_element, remove_item
from utilities_dict import get_total_population, get_province_description, get_largest_province, \
    get_another_capital_city, get_largest_city, get_smallest_province


def main():
    cap_and_prov = {"Alberta": 'Edmonton',
                    'British Columbia': 'Victoria',
                    'Manitoba': 'Winnipeg',
                    'New Brunswick': 'Fredericton',
                    'Newfoundland and Labrador': 'St.Johns',
                    'Northwest Territories': 'Yellowknife',
                    'Nova Scotia': 'Halifax',
                    'Nunavut': 'Iqaluit',
                    'Ontario': 'Toronto',
                    'Prince Edward Island': 'Charlottetown',
                    'Saskatchewan': 'Regina',
                    'Yukon': 'Whitehorse'}

    display_all(cap_and_prov)
    print(get_capital_city('Ontario', cap_and_prov))
    add_element('italy', 'rome', cap_and_prov)
    print(get_capital_city('italy', cap_and_prov))
    remove_item('Manitoba', cap_and_prov)
    print(cap_and_prov)


# nested dict

canada = {
    "alberta": {"capital": "edmonton", "largest": "calgary", "population": 3645257},
    "Manitoba": {"capital": "Quebec City", "largest": "Montreal", "population": 4587435},
    "Ontario": {"capital": "Quebec City", "largest": "Montreal", "population": 8574571},
    "Quebec": {"capital": "Quebec City", "largest": "Montreal", "population": 579635},
    "Saskatchewan": {"capital": "Quebec City", "largest": "Montreal", "population": 123689},
    "Nunavut": {"capital": "Quebec City", "largest": "Montreal", "population": 4933586},
    "Yukon": {"capital": "Quebec City", "largest": "Montreal", "population": 7539814},
}

print(get_total_population(canada))
print(get_another_capital_city('Quebec', canada))
print(get_largest_city('Ontario', canada))
print(get_smallest_province(canada))
print(get_largest_province(canada))
print(get_province_description('alberta', canada))

if __name__ == "__main__":
    main()
