def countdown(start):
  # This is the outer enclosing function
  def display():
    # This is the nested function
    n = start
    while n > 0:
      n-=1
      print(f"n = {n}")
  return display

counter1 = countdown(2)
counter1()
del countdown # the ref to method is deleted 
counter1() # yet the state is maintained 
