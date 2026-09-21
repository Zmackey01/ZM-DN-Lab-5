def roman_to_decimal(string):
  """
  string -> string
  
  takes in a string as a Roman numeral and returns the whole number it corresponds to.

  >>> roman_to_decimal("XIX")
  19
  >>> roman_to_decimal("MCMX")
  1910
  >>> roman_to_decimal("III")
  3
  """
  values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000}
  total = 0
  for i in range(len(string)):
    if i + 1 < len(string) and values[string[i]] < values[string[i+1]]:
      total -= values[string[i]]
    else:
      total += values[string[i]]
  return total