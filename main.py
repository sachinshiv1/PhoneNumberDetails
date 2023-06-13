import phonenumbers
    # phonenumbers module have many functions to get details
from phonenumbers import timezone, geocoder, carrier

number = input("Enter your Number with Country code\n")
    # Take Number from the user in String form

phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")

print("Phone Number = ", phone)
print("Time-Zone = ", time)
print("Carrier = ", car)
print("Region = ", reg)
