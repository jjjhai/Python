# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 13:55:55 2018

@author: Administrator
"""

"""
如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。如果异常的类型和except之后的名称相符，那么对应的except子句将被执行。最后执行try语句之后的代码
如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中
最多只有一个except子句会被执行
一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组
最后一个except子句可以忽略异常的名称，它将被当作通配符使用。可以使用这种方法打印一个错误信息，然后再次把异常抛出
try except 语句还有一个可选的else子句，如果使用这个子句，那么必须放在所有的except子句之后。这个子句将在try子句没有发生任何异常的时候执行
不管try子句里面有没有发生异常，finally子句都会执行
如果一个异常在try子句里（或者在except和else子句里）被抛出，而又没有任何的except把它截住，那么这个异常会在finally子句执行后再次被抛出
"""

"""
使用raise语句抛出一个指定的异常
raise唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是Exception的子类）
"""


import sys
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

# 自定义异常
class InputError(Error):
    """Exception raised for errors in the input.
    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
        
        
try:
    print('code start running...')
    raise InputError('input()', 'input error')
    # ValueError
    int('a')
    # TypeError
    s = 1 + 'a'
    dit = {'name': 'john'}
    # KeyError
    print(dit['1'])
except InputError as ex:
    print("InputError:", ex.message)
except TypeError as ex:
    print('TypeError:', ex.args)
    pass
except (KeyError, IndexError) as ex:
    """支持同时处理多个异常, 用括号放到元组里"""
    print(sys.exc_info())
except:
    """捕获其他未指定的异常"""
    print("Unexpected error:", sys.exc_info()[0])
    # raise 用于抛出异常
    raise RuntimeError('RuntimeError')
else:
    """当无任何异常时, 会执行 else 子句"""
    print('"else" 子句...')
finally:
    """无论有无异常, 均会执行 finally"""
    print('finally, ending')
    
# sys.exc_info() 取得异常信息