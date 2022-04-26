capacity = float(input("Please enter your car's fuel capacity : "))
distance = float(input("Please enter how many you go to distance with your car? : "))

kilometers_one_kilometer = float(1)
kilometers_hundert_kilometers = float(100)
gasoline_amount = float(20)

using_gasoline_one_kilometer = capacity/distance * kilometers_one_kilometer
using_gasoline_hundert_kilometers = capacity/distance * kilometers_hundert_kilometers
total_amount_one_kilometer = float(using_gasoline_one_kilometer * gasoline_amount)
total_amount_hunder_kilometers = float(using_gasoline_hundert_kilometers * gasoline_amount)

print("Using gasoline in 1 kilometer : ",using_gasoline_one_kilometer,"L")
print("Using gasoline in 100 kilometers : ",using_gasoline_hundert_kilometers,"L")
print("Total amount for 1 kilometer : ",total_amount_one_kilometer,"₺")
print("Total amount for 100 kilometers : ",total_amount_hunder_kilometers,"₺")
