# manga 100 ch = 415 mbs

manga = 0

my_quota = 100

used = ((500 + (manga * 415)) / 1024)

remaining_percentage = my_quota - used / my_quota * 100

if remaining_percentage < 0:
  print(remaining_percentage, "Critical: your allowance is done abort immediately")
elif remaining_percentage <= 10:
  print(remaining_percentage, "Critical: you have less than 10% left")
elif remaining_percentage <= 20:
  print(remaining_percentage, "Critical: you have less than 20% left")
elif remaining_percentage <= 25:
  print(remaining_percentage, "warning: you have less than 25% left")
elif remaining_percentage <= 50:
  print(remaining_percentage, "warning: you have less than 50% left")
elif remaining_percentage > 50:
  print(remaining_percentage)
  
  

# print(remaining_percentage)