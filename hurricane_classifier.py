speed_of_hurricane = int(input("what is the speed of the huricane? \n > "))




if 0 <= speed_of_hurricane < 75:
    print("Tropical storm")
elif 75 <= speed_of_hurricane < 96:
    print("Category 1")
elif 96 <= speed_of_hurricane < 111:
    print("Category 2")
elif 111 <= speed_of_hurricane < 130:
    print("Category 3")
elif 130 <= speed_of_hurricane < 157:
    print("Category 4")
else:
    print("Category 5")