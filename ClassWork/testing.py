# variables total = 0 print("Welcome to the pizza shop") selection = input("Would you like to make an order?"'y or n').lower() while selection == "y": print("Cheese pizza,  Seafood Pizza,  Ham Pizza, Beef pizza, Vegetarian pizza") selection = input("Cheese pizza,  Seafood Pizza, Ham Pizza, Beef pizza, Vegetarian pizza" 'c,s,h,b or v') if selection == "c": print("cheese pizza ==$10") total = total + 10 elif selection == 's': print("seafood pizza == $20") total = total + 20 elif selection == "h": print("ham pizza ==  $12") total = total + 12 elif selection == "b": print("beef pizza ==  $12") total = total + 12 elif selection == "v": print("vegetarian pizza ==$8") total = total + 8 selection = input("Would you like to make an another order?y/n").lower() print(total) payment = int(input("How much would you like to pay?")) change = payment - total print('your change is', change) print("enjoy your pizza") 