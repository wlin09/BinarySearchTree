# Application of binary search tree in main section of file.
class Fraction:

  def __init__(self, numerator, denominator):
    if denominator == 0:
      raise ZeroDivisionError # Raising an exception from a constructor shouldn't cause a problem here for Python.
    self.__n = numerator
    self.__d = denominator
    self.__reduce()

  @staticmethod
  def gcd(n, d):
    while d != 0:
      t = d
      d = n % d
      n = t
    return n

  def __reduce(self):
    if self.__n < 0 and self.__d < 0:
      self.__n = self.__n * -1
      self.__d = self.__d * -1
    divisor = Fraction.gcd(self.__n, self.__d)
    self.__n = self.__n // divisor
    self.__d = self.__d // divisor

  def __add__(self, addend):
    num = self.__n * addend.__d + self.__d * addend.__n
    den = self.__d * addend.__d
    return Fraction(num, den)

  def __sub__(self, subtrahend):
    num = self.__n * subtrahend.__d - self.__d * subtrahend.__n
    den = self.__d * subtrahend.__d
    return Fraction(num, den)

  def __mul__(self, multiplicand):
    num = self.__n * multiplicand.__n
    den = self.__d * multiplicand.__d
    return Fraction(num, den)

  def __truediv__(self, divisor):
    if divisor.__n == 0:
      raise ZeroDivisionError
    num = self.__n * divisor.__d
    den = self.__d * divisor.__n
    return Fraction(num, den)

  def __lt__(self, other):
    # The function has a time complexity of O(1) because there are a fixed number of
    # operations, being done in constant time.
    cross_product = self.__n * other.__d - other.__n * self.__d # Used cross-multiplication to remain in the integer domain.
    if cross_product < 0: # Returning True if self is less than other and False otherwise.
      return True 
    return False

  def __gt__(self, other):
    # The function has a time complexity of O(1) because there are a fixed number of
    # operations, being done in constant time.
    cross_product = self.__n * other.__d - other.__n * self.__d # Used cross-multiplication to remain in the integer domain.
    if cross_product > 0: # Returning True if self is greater than other and False otherwise.
      return True 
    return False

  def __eq__(self, other):
    # The function has a time complexity of O(1) because there are a fixed number of
    # operations, being done in constant time.
    cross_product = self.__n * other.__d - other.__n * self.__d # Used cross-multiplication to remain in the integer domain.
    if cross_product == 0: # Returning True if self equal to other and False otherwise.
      return True 
    return False

  def to_float(self):
    return self.__n / self.__d # This is safe because we don't allow a zero denominator.

  def __str__(self):
    return str(self.__n) + '/' + str(self.__d)

  def __repr__(self):
    return str(self) # Called when Python wants to display these objects in a container like a Python list.

if __name__ == '__main__':
  from Binary_Search_Tree import Binary_Search_Tree 
  fractions = [Fraction(1, 2), Fraction(7, 8), Fraction(3, 4), Fraction(5, 6), Fraction(9, 10)] # Creates a bunch of fraction objects and stores them in an array.
  bst = Binary_Search_Tree()
  for fraction in fractions:
      bst.insert_element(fraction) # Inserts each item from the array into a balanced BST.
  in_order_list = bst.to_list() # Using the new to_list method of Binary_Search_Tree.
  print('Original List:', fractions) # Prints the original array to show that the fractions have been sorted.
  print('In-order Traversal List:', in_order_list) # Prints the in-order traversal array to show that the fractions have been sorted.
