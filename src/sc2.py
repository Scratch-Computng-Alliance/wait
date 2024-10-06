def scenario():
    print("Your boss said you needed to code something that defines a list and sorts it what do you do?")
    print("1. make it yourself")
    print("2. find the answer on stack overflow")

    answer = input("choice:")
  
    if answer == "1":
      print("you take the time to build it and come out with the best possible code:")
      print("random_numbers = [1, 4, 3, 2]")
      print("sorted_numbers = sorted(random_numbers)")
      print("print(sorted_numbers)")
    else:
      print("you get it from stack overflow and make this:")
      print("random_numbers = [1, 4, 3, 2]")
      print("sorted_numbers = sorted(random_numbers)")
      print("print(sorted_numbers)")
      print("but then you get fired from your job. GET OUT!")
