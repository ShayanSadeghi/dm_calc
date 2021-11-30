import numpy as np


def readfile(filename):
   new_arr = []

   with open("test.txt", 'r') as file:
      l_count = sum(1 for line in file)
      file.seek(0)

      for i in range(l_count):
         line = file.readline()
         line = line.replace("\n", "").split(',')
         new_arr.append(line)
      
   new_arr = np.array(new_arr, dtype='float')
   return new_arr

def op1(arr):
   col_sum = arr.sum(axis=0)
   divided_by_col_sum = arr/col_sum
   res = divided_by_col_sum
   # print(res)
   return res
   
def op2(arr):
   temp = op1(arr)
   row_mean = temp.mean(axis=1)
   print(row_mean.round(3))

def op3(arr1, arr2):
   prod = np.dot(arr1,arr2)
   print(prod)

def show_memory(arr):
   print(in_memory_files)
   for i in range(len(in_memory_files)):
      print(f'index {i}:')
      print(in_memory_files[i])
      print(10*"-")
      

in_memory_files = []
while True:
   print("1.\tRead file")
   print("2.\tMean operation")
   print("3.\tDot production")
   print("4.\tShow memory")
   print("5.\tClear memory")
   print("6.\tExit")
   print(20*'-')
   s = int(input("Choice: "))
   
   if s == 1:
      filename = input("Enter file name: ")
      in_memory_files.append(readfile(filename))
      print(in_memory_files[-1])
      print(20*"-")

   elif s==2:
      arr_ind = 0
      if len(in_memory_files)>1:
         arr_ind = int(input("Enter index:"))
      
      op2(in_memory_files[arr_ind])
      print(20*"-")
      
   elif s==3:
      arr_ind_0=0
      arr_ind_1=1
      if len(in_memory_files)<2:
         print("Error, please add 2 file at list")
   
      
      if len(in_memory_files)>2:
         arr_ind_0 = int(input("Enter index for first array:"))
         arr_ind_1 = int(input("Enter index for second array:"))
         
      op3(in_memory_files[arr_ind_0], in_memory_files[arr_ind_1])
      print(20*"-")

   elif s==4:
      show_memory(in_memory_files)
      print(20*"-")
   elif s==5:
      in_memory_files = []
   elif s == 6:
      break
   