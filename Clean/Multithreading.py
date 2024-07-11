import threading
import time

working = True

def task1():
  count1 = 0
  while working:
    count1 += 1
    print("Task 1 count = ", count1)

def task2():
  count2 = 0
  while working:
    count2 += 1
    print("Task 2 count = ", count2)


t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

input("Enter something to stop: ")
working = False

# t1.join()
# t2.join()
# t3.join()