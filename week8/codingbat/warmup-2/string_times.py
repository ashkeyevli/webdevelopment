def string_times(str, n):
    s=str
    if n==0:
      return ""
    for i in range(n-1):
        str+=s
    return str
