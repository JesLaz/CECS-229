#!/usr/bin/env python
# coding: utf-8

# ## CECS 229 Coded HW #3
# 
# #### Due Date: Tuesday 3/14 @ 11:59 PM
# 
# #### Submission Instructions:
# 
# Attach your coded solution to the programming tasks below. When you are finished...
# 
# 1. Rename this file so that your actual name replaces "YOUR NAME" in the current notebook name, and submit it to the dropbox by **Tuesday 4/14 @ 11:59 PM**. For example, I would submit to the dropbox a file called  `CECS 229 Coded HW#3 - KATHERINE VARELA.ipynb`
# 2. Submit your code only to CodePost as `hw3.py` by **Tuesday 4/14 @ 11:59 PM**
# 
# ### Programming Tasks
# 1. Implement the missing functions of the class `Vec` below. 
# 
#     * `__abs__(self)` to define the `abs()` method.  The call `abs(v)` for a vector $v = [v_1, v_2, ..., v_n]$ should return the Euclidean norm of the vector, i.e. result of $\sqrt{v_1^2 + v_2^2 + \cdots +v_n^2}$
#     
#     e.g `abs(Vec([-3, 0.5, 1.7]))` returns `3.4842502780368694`

# In[8]:


class Vec:
    def __init__(self, contents = []):
        """constructor defaults to empty vector
           accepts list of elements to initialize a vector object with the 
           given list
        """
        self.elements = contents
        return
    
    def __abs__(self):
        """Overloads the built-in function abs(v)
            returns the Euclidean norm of vector v
        """
        pass
        
    def __add__(self, other):
        """Overloads the + operation to support Vec + Vec
         raises ValueError if vectors are not same length
        """
        pass
    
    
    def __mul__(self, other):
        """Overloads the * operator to support 
            - Vec * Vec (dot product) raises ValueError if vectors are not same length in the case of dot product
            - Vec * float (component-wise product)
            - Vec * int (component-wise product)
            
        """
        if type(other) == Vec: #define dot product
            #FIXME: IMPLEMENT
            pass
        elif type(other) == float or type(other) == int: #scalar-vector multiplication
            #FIXME: IMPLEMENT
            pass
            
    
    def __rmul__(self, other):
        """Overloads the * operation to support 
            - float * Vec
            - int * Vec
        """
        pass
    
    def __str__(self):
        """returns string representation of this Vec object"""
        return str(self.elements) # does NOT need further implementation
    
    def __sub__(self, other):
        pass


# In[12]:


"""----------------------TESTER CELL----------------------"""
import math
u = Vec([1, 2, 3])
w = Vec([0, 1, -1])
v = Vec([0, -3])
print("u = ", u)
print("w = ", w)
print("Euclidean norm of u:", abs(u))
print("Expected:", math.sqrt(sum([ui**2 for ui in u.elements])))
print("Euclidean norm of u:", abs(v))
print("Expected: 3")
print("\nu left scalar multiplication by 2:", 2*u)
print("Expected: [2, 4, 6]")
print("\nw right scalar multiplication by -1:", w * -1.2)
print("Expected: [0, -1, 1]")
print("\nVector addition:", u + w)
print("Expected: [1, 3, 2]")
print("\nVector addition:", u - w)
print("Expected: [1, 1, 4]")
print("\nDot product:", w*u)
print("Expected: -1")


try:
    print("\nDot product:", v*u)
    print("If this line prints, you forgot to raise a ValueError for taking the dot product of vectors of different lengths")
except:
    print("If this line prints, the line passed the test.")

