import subprocess

# Run the 'pip list' command and capture its output
result = subprocess.run(['pip', 'list'], stdout=subprocess.PIPE)

# Convert the output from bytes to string
pip_list = result.stdout.decode('utf-8')

# print(pip_list)

arr = pip_list.split("\n")
arr = list(filter(None, arr))

newarr = []

for lib in arr:
  for i in range(len(lib)):
    if lib[i] == " ":
      newarr.append(lib[:i])
      # print(lib[:i])
      break

# for lib in newarr:
#   print(lib)

import os


pipupd = "python.exe -m pip install --upgrade pip"
pyupd = ""
pyupd += f"pip install --upgrade "

for lib in newarr:
  pyupd += lib + " "
  
# print(string)
os.system(pipupd)
os.system(pyupd)







# # for i, lib in enumerate(arr):
# #   if i % 2 == 0:
# #     print(lib)
