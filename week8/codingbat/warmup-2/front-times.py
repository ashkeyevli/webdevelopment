def front_times(str, n):
  s = str[0:3]
  str=str[0:3]
  if n==0:
    return ""
  for i  in range(n-1):
    str+=s
  return str
