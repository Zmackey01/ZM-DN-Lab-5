def bologna_latin(string):
  """
  string -> string

  takes a string and returns a string with the first letter moved to the end of the string together with an "ay".
  
  >>> bologna_latin("programming")
  "rogrammingpay"
  >>> bologna_latin("hello world")
  "ello worldhay"
  >>> bologna_latin("a")
  "aay"
  """
  return string[1:] + string[0] + "ay"


