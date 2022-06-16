def CommonPrefix(s,t):
  i = 0
  str_com = ""
  if len(s) < len(t):
    length = len(s)
  else:
    length = len(t)
  while i < length:
    if s[i] == t[i]:
      str_com = str_com + s[i]
      i += 1
    else:
      break
  return str_com

def longestCommonPrefix(strs):
  if len(strs) == 1:
    return strs[0]
  str_com = CommonPrefix(strs[0], strs[1])
  if str_com == "":
    return ""
  i = 2
  while i < len(strs):
    if str_com == "":
      return ""
    str_com = CommonPrefix(str_com, strs[i])
    i += 1
  return str_com

def main():
  s = ["flight"]
  s  = longestCommonPrefix(s)
  print("longest common prefix = %s" % s)
  s = ["reflower","flow","flight"]
  s  = longestCommonPrefix(s)
  print("longest common prefix = %s" % s)
  s = ["flow","flight","reflower"]
  s  = longestCommonPrefix(s)
  print("longest common prefix = %s" % s)
  s = ["flower","flow","flight"]
  s  = longestCommonPrefix(s)
  print("longest common Prefix = %s" % s)

if __name__ == '__main__':
  main()
