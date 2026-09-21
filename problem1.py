def ugly_number(n):
  """
  number -> Boolean
  
  takes n and returns True if it has a prime factor of 2, 3, 5 or none of these at all, returns False if otherwise

  >>> ugly_number(6)
  True
  >>> ugly_numer(1)
  True
  >>> ugly_number(14)
  False
  >>> ugly_number(8)
  True
  """
  if n%2==1:
    return True
  if n%3==1:
    return True
  if n%5==1:
    return True
  else:
   return False
    
  
  