import json

# Load JSON data from file
in_file = open('C:\\Users\\lenovo\\Downloads\\Python-task.json', 'r')

jd = json.loads(in_file.read())

# Extract the list of shown prices
shown_price = list(jd.get('assignment_results', [{}])[0].get('shown_price', {}).values())


def cheapest(shown_price):
    """Finds the lowest price without using the min() function."""
    for i in range(len(shown_price)):
        for j in range(len(shown_price)):
            if shown_price[i] > shown_price[j]:
                shown_price[i], shown_price[j] = shown_price[j], shown_price[i]
    return shown_price[0]


cheapest_shown_price = cheapest(shown_price)


def cheap_rooms(room_type, Number_of_Guests, cheapest_shown_price):
    """Finds the room type and number of guests for the cheapest price."""
    for room, price in room_type.items():
        if price == cheapest_shown_price:
            return room, Number_of_Guests


room_type = jd.get('assignment_results', [{}])[0].get('shown_price', {})
Number_of_Guests = jd.get('assignment_results', [{}])[0].get('number_of_guests', '')
cheap_room_with_no_of_guest = cheap_rooms(room_type, Number_of_Guests, cheapest_shown_price)

# Calculate total taxes
taxes = jd.get('assignment_results', [{}])[0].get('ext_data', {}).get('taxes', '')
total_tax = 0
for tax in eval(taxes).values():
    total_tax += float(tax)


def total_room_price(net_price, total_tax):
    """Calculates the total price including net price and taxes."""
    rooms_with_tax = {}
    for room_type, price in net_price.items():
        rooms_with_tax.update({room_type: (float(price) + total_tax)})
    return rooms_with_tax


net_price = jd.get('assignment_results', [{}])[0].get('net_price', {})
total_price = total_room_price(net_price, total_tax)


# Prepare output
output = {'cheapest_(lowest)_shown_price': cheapest_shown_price,
          'room_type_with_number_of_guest': cheap_room_with_no_of_guest,
          'total_price_(Net_price_+_taxes)': total_price
          }
for key, value in output.items():
    print(f"{key}: {value}")
