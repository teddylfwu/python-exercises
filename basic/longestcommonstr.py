def Commonsubstring(s,t):
  i = 0
  j = 0
  str_com = ""
  while i < len(s) and j < len(t):
    if len(s) > len(t):
    #move letter in s to match letter in t
      if s[i] == t[j]:
        str_com = str_com + s[i]
        i += 1
        j += 1
      else:
        i += 1
    else: #always try to match longer one to the shorter one
    #move letter in t to match letter in s
      if s[i] == t[j]:
        str_com = str_com + s[i]
        i += 1
        j += 1
      else:
        j += 1

  return str_com

def longestCommonsubstring(strs):
  if len(strs) == 1:
    return strs[0]
  str_com = Commonsubstring(strs[0], strs[1])
  if str_com == "":
    return ""
  i = 2
  while i < len(strs):
    str_com = Commonsubstring(str_com, strs[i])
    i += 1
    if str_com == "":
      return ""
  return str_com

def main():
  s = ["flight"]
  s  = longestCommonsubstring(s)
  print("longest common substring = %s" % s)
  s = ["reflower","flow","flight"]
  s  = longestCommonsubstring(s)
  print("longest common substring = %s" % s)
  s = ["flow","flight","reflower"]
  s  = longestCommonsubstring(s)
  print("longest common substring = %s" % s)
  s = ["flower","flow","flight"]
  s  = longestCommonsubstring(s)
  print("longest common substring = %s" % s)

if __name__ == '__main__':
  main()
