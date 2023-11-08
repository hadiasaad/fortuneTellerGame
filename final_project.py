color = input("choose a color - red, blue, yellow or green: ")

if color == "red":
  number = input("Choose a number - 1, 2, 3, 4: ")
elif color == "blue":
  number = input("choose a number - 3, 4, 5, 6: ");
elif color == "yellow":
  number = input("choose a number - 5, 6, 7, 8: ");
elif color == "blue":
  number = input("choose a number - 7, 8, 1, 2: ");

if number == "1":
    print("Would you rather have a - 1. pause button or 2. rewind button")
elif number == "2":
    print("Would you rather be able to - 1. talk to all animals or 2. speak all foreign laguages")
elif number == "3":
    print("Would you rather eat - 1. the same thing for every meal for a year or 2. whatever you wanted, but only once every three days ")
elif number == "4":
    print("Would you rather lose - 1. your sight or 2. your memory ")
elif number == "5":
    print("Would you rather be - 1. forced to live the same day over and over again for a full year or 2. take three years of the end of your life ")
elif number == "6":
    print("Would you rather have - 1. unlimited battery life on all of your devices or 2. free WiFi wherever you go")
elif number == "7":
    print("Would you rather - 1. travel the world for free for a year or 2. have $50,000 to spend however you please")
elif number == "8":
    print("Would you rather be - 1. alone all your life or 2. surrounded by really annoying people")
    
rather = input("1 or 2: ")
if rather == "1": 
  print("What a great choice!");
elif rather == "2":
  print("Amazing Choice!");