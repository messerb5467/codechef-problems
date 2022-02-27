def get_ints_from_string(string, sep=" "):
  return list(map(lambda x: int(x), string.strip().split(" ")))