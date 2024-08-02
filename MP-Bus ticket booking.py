a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def bus():
   while True:
       b = int(input('No. of seats:'))
       if b > 3:
          print('Seats cannot be booked more than 3')
          continue
    
       if len(a) < b:
          print(f'Seats not available more than {len(a)}')
          continue
    
       for i in range(b):
           print(a)
           c = int(input('Seat no.:'))
           if c in a:
              print('Seat booked Successfully')
              a.remove(c)
              
           else:
              print('Error: Seat already booked')
              print(a)
              c = int(input('Seat no.:'))
              print('Seat booked Successfully')
              a.remove(c)
              continue
       if not a:
          print("Seat booking closed")
          break

bus()




