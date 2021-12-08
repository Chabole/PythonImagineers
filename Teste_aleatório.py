# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 20:40:07 2021

@author: Arthur Chabole
==========================

"""

def FibonacciChecker(num):
    
  Fn=[]
  Fn[0]=1
  Fn[1]=1
  i=2
  
  while Fn<=num:
    Fn[i]=Fn[i-1]+Fn[i-2]
    i+=1
    
  if Fn[i]==num:  
    return 'yes'
  else:
    return 'no'

 
  

# num = int(input("Digite um número: "))
# a = FibonacciChecker(num) 

n = FibonacciChecker(5)
#%%

def fibonacci_iter(n):
    lista = []
    a=1
    b=1
    if n==1:
        lista.append(int(0))
    elif n==2:
        lista.append(int(0), int(1))
    else:
        lista.append(int(0))
        lista.append(int(a))
        lista.append(int(b))
        for i in range(n-3):
            total = a + b
            b=a
            a= total
            print(total)
            
            
            
r = fibonacci_iter(5)        
            
            
            
            
            
            
            
            
            