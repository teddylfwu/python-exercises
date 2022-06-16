def myAtoi(s: str) -> int:
  s = s.strip()
  digits = "0123456789"
  s = s.strip()
  # after strip, empty string
  if s == '':
    return 0
  # after strip, string len is 1
  if len(s) == 1:
    if s in digits:
      return int(s)
    else:
      return 0
  # after strip, string len is greater than 1
  if s[0] == "-":
    sign = "-"
    s = s[1:]
  elif s[0] == "+":
    sign = "+"
    s = s[1:]
  else:
    sign = "+"
  if s[0] in digits:
    digits_end = 0
  else:
    return 0
  while digits_end < len(s):
    if s[digits_end] in digits:
      digits_end += 1
    else:
      break
    s = sign + s[:digits_end+1]
    s_int = int(s)
    if s_int < -2**31:
      return -2**31
    elif s_int > 2**31 -1:
      return 2**31 -1
    else:
      return s_int

def main():
  s = ""
  value  = myAtoi(s)
  print("value = %d" % value)
  s = "+"
  value  = myAtoi(s)
  print("value = %d" % value)
  s = "words and 987"
  value  = myAtoi(s)
  print("value = %d" % value)
  s = "+42 many more"
  value  = myAtoi(s)
  print("value = %d" % value)
  s = "-42"
  value  = myAtoi(s)
  print("value = %d" % value)

if __name__ == '__main__':
  main()
