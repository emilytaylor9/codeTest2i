#Please state any assumptions you’ve made

#multiples of A until X
def multiples(a,b):
    for x in range(b+1):
        if x % a == 0 and x != 0:    #added != 0 to stop 0 from printing
            print(x)

#user can change mutiples(a) up to any number(b) below
#this example will print multiples of 5 up until 50

multiples(5,50)


#then in multiples of A + 1 until 2X,
def multiple2(a,b):
      b=b*2 
      x=0
      if x <= b:
            a=a+1
            x+=1
            for y in range(b+1):
                  if y <= b and y % a == 0:
                        print(y)
            
#same as above, user can change multiples(a) up to any number (b)
#this example will print out the multiples of (2+1) until (2x10) is reached 

multiple2(2,10)

#then multiples of A + 2 until 3X
def multiple3(a,b):
      b=b*3
      x=0
      if x <= b:
            a=a+2
            x+=1
            for y in range(b+1):
                  if y <= b and y % a == 0:
                        print(y)

#this example will print out multiples of (2+2) until (3x10) is reached

multiple3(2,10)

