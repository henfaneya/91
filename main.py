file_name = input("What's the file name? ")
name = input("What's your name? ")
street_address = input("What's your address? ")
phone_number = input("What's your number? ")

with open(file_name, 'w') as file:
  file.write(f"{name.title()}, ")
  file.write(f"{street_address.title()}, ")
  file.write(f"{phone_number}")

with open(file_name) as read_file:
  for line in read_file:
    print()
    print(line)