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
  if n<= 0:
    return False
  for factor in [2, 3, 5]:
    while n % factor ==0:
      n=n // factor
  return n == 1
    
  
  