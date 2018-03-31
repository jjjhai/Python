# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 16:47:29 2018

@author: Administrator
"""

def short(word="yes"):
    return word.capitalize()+"!"
print(short())

scream = short

del short

try:
    print(short())
except NameError as e:
    print(e)
    
def talk():
    
    def whisper(word="yes"):
        return word.lower()+"..."
    
    print(whisper())

talk()

def decorator(pre=""):
    
    def Fun(F):
        
        def new_Fun(a, b):
            print("new_Fun")
            F(a, b)
            
        return new_Fun
    
    return Fun


@decorator("pre")
def Test(a, b):
    print(a+b)
    
Test(1,2)


    

    

