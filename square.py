
def square(w, h):
  symbols = ["┌", "-", "┐", "|" ,"└" ,"┘"]
  for i in range(h):
    x=""
    for j in range(w):
      if i == 0 and j == 0:
        x= x + symbols[0]
        # print("⌐")
      elif i == 0 and j == w-1:
        x= x + symbols[2]
        # print("¬")
      elif i==h-1 and j==0:
        # print("└")
        x= x + symbols[4]
      elif i ==h-1 and j==w-1:
        # print("┘")
        x= x + symbols[5]
      elif(j == 0 or j ==w-1):
        # print("|")
        x= x + symbols[3]
      elif(i == 0 or i==h-1):
        # print("-")
        x= x +  symbols[1]
      else:
        # Print space
        x= x + " " 

    print(x)
      

  

square(4,4)
square(3,3)
square(2,3)

