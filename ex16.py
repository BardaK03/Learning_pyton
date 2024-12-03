Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0
choice1 = int(input("""Q1) Do you like Dawn or Dusk? 
  1) Dawn 
  2) Dusk
"""))
if choice1 == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif choice1 == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print("Invalid choice")
choice2 = int(input("""""Q2) When I’m dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold
    """""))
if choice2 == 1:
    Hufflepuff += 1
elif choice2 == 2:
    Slytherin += 1
elif choice2 == 3:
    Ravenclaw += 1
elif choice2 == 4:
    Gryffindor += 1
else:
    print("Invalid choice")
choice3 = int(input("""""Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum
    """""))
if choice3 == 1:
    Slytherin += 4
elif choice3 == 2:
    Hufflepuff += 4
elif choice3 == 3:
    Ravenclaw += 4
elif choice3 == 4:
    Gryffindor += 4
else:
    print("Invalid choice")

if Gryffindor >= Ravenclaw and Gryffindor >= Hufflepuff and Gryffindor >= Slytherin:
  print(' Gryffindor!')
elif Ravenclaw >= Hufflepuff and Ravenclaw >= Slytherin:
  print(' Ravenclaw!')
elif Hufflepuff >= Slytherin:
  print(' Hufflepuff!')
else:
  print(' Slytherin!')




