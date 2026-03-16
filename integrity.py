data = input("Enter data packet: ")

if data == data[::-1]:
  print("Data integrity verified (Palindrome)")
else:
  print("Data may be corrupted")
