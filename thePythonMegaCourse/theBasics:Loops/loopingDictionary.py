#contacts = { "John Smith": "+37682929928", "Marry Simpons": "+423998200919" }
#
#for key, value in contacts.items():
#  print(f"{key} {value}")

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for value in phone_numbers.values():
  print(value.replace("+", "00"))

for key in phone_numbers.keys():
  print(key.replace("S", "BALI"))