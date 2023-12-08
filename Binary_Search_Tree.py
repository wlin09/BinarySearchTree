# Implementation of binary search tree. Performance analysis included for functions.
class Binary_Search_Tree:

  class __BST_Node:

    def __init__(self, value):
      # The constructor has a time complexity of O(1) because it does not depend on 
      # size, being done in constant time.
      self.value = value
      self.left = None
      self.right = None
      self.height = 1

  def __init__(self):
      # The constructor has a time complexity of O(1) because it does not depend on 
      # size, being done in constant time.
    self.__root = None

  def insert_element(self, value):
    # The function has a time complexity of O(log n) due to calling a function that
    #  has a time complexity of O(log n).
    self.__root = self.__insert_element(self.__root, value)

  def __insert_element(self, root, value):
    # The function has a time complexity of O(log n) because it involves traversing
    # the height of the tree, which involves a logarithmic number of nodes.
    if root is None:
      return self.__BST_Node(value) # Part of base case.
    elif value < root.value:
      root.left = self.__insert_element(root.left, value) # Part of recursive case.
    elif value > root.value:
      root.right = self.__insert_element(root.right, value) # Part of recursive case.
    else:
      raise ValueError # Value already exists in tree, part of base case.
    root.height = 1 + max(self.__get_height(root.left), self.__get_height(root.right))
    balance_factor = self.__get_balance_factor(root)
    if balance_factor > 1:
      if value < root.left.value:
        return self.__right_rotate(root)
      else:
        root.left = self.__left_rotate(root.left)
        return self.__right_rotate(root)
    if balance_factor < -1:
      if value > root.right.value:
        return self.__left_rotate(root)
      else:
        root.right = self.__right_rotate(root.right)
        return self.__left_rotate(root)
    return root

  def remove_element(self, value):
    # The function has a time complexity of O(log n) due to calling a function that
    #  has a time complexity of O(log n).
    self.__root = self.__remove_element(self.__root, value)

  def __remove_element(self, root, value):
    # The function has a time complexity of O(log n) because it involves traversing
    # the height of the tree, which involves a logarithmic number of nodes.
    if root is None:
      raise ValueError # Value not found in tree, part of base case.
    if value < root.value:
      root.left = self.__remove_element(root.left, value) # Part of recursive case.
    elif value > root.value:
      root.right = self.__remove_element(root.right, value) # Part of recursive case.
    else:
      if root.left is None:
        return root.right
      elif root.right is None:
        return root.left
      root.value = self.__min_value(root.right)
      root.right = self.__remove_element(root.right, root.value) # Part of recursive case.
    root.height = 1 + max(self.__get_height(root.left), self.__get_height(root.right))
    return self.__balance(root)

  def __balance(self, t):
    # The function has a time complexity of O(1) because it only involves 
    # rearranging pointers, being done in constant time.
    balance_factor = self.__get_balance_factor(t)
    if balance_factor > 1:
      if self.__get_balance_factor(t.left) < 0:
        t.left = self.__left_rotate(t.left)
      return self.__right_rotate(t)
    if balance_factor < -1:
      if self.__get_balance_factor(t.right) > 0:
        t.right = self.__right_rotate(t.right)
      return self.__left_rotate(t)
    return t

  def __get_balance_factor(self, node):
    # The function has a time complexity of O(1) because it involves computing the 
    # height of the left and right subtrees, being done in constant time.
    return self.__get_height(node.left) - self.__get_height(node.right)

  def __left_rotate(self, k): # 'k' represents the node that becomes the new root of the rotated subtree.
    # The function has a time complexity of O(1) because it only involves 
    # rearranging pointers and updating heights, being done in constant time.
    j = k.right # 'j' becomes the new root's left child and represents the right child of 'k'.
    m = j.left # 'm' becomes the right child of 'k' and represents the left child of 'j'.
    j.left = k
    k.right = m
    k.height = 1 + max(self.__get_height(k.left), self.__get_height(k.right))
    j.height = 1 + max(self.__get_height(j.left), self.__get_height(j.right))
    return j

  def __right_rotate(self, j): # 'j' represents the node that becomes the new root of the rotated subtree.
    # The function has a time complexity of O(1) because it only involves 
    # rearranging pointers and updating heights, being done in constant time.
    i = j.left # 'i' becomes the new root's right child and represents the left child of 'j'.
    m = i.right # 'm' becomes the left child of 'j' and represents the right child of 'i'.
    i.right = j
    j.left = m
    j.height = 1 + max(self.__get_height(j.left), self.__get_height(j.right))
    i.height = 1 + max(self.__get_height(i.left), self.__get_height(i.right))
    return i

  def __min_value(self, node):
    # The function has a time complexity of O(log n) because it involves traversing
    # to the leftmost leaf, which takes logarithmic time due to having to traverse
    # the left child of each node in the worst-case scenario.
    current = node
    while current.left is not None:
      current = current.left
    return current.value

  def in_order(self):
    # The function has a time complexity of O(n) because it calls on a function that
    # has a time complexity of O(n).
    result = self.__in_order(self.__root)
    return f'[ {", ".join(map(str, result))} ]' if result else '[ ]' # Ensures proper format.

  def __in_order(self, root):
    # The function has a time complexity of O(n) because it visits each node once,
    # resulting in linear time complexity.
    if root is None:
      return [] # Part of base case.
    return self.__in_order(root.left) + [root.value] + self.__in_order(root.right) # Part of recursive case.

  def pre_order(self):
    # The function has a time complexity of O(n) because it calls on a function that
    # has a time complexity of O(n).
    result = self.__pre_order(self.__root)
    return f'[ {", ".join(map(str, result))} ]' if result else '[ ]' # Ensures proper format.

  def __pre_order(self, root):
    # The function has a time complexity of O(n) because it visits each node once,
    # resulting in linear time complexity.
    if root is None:
      return [] # Part of base case.
    return [root.value] + self.__pre_order(root.left) + self.__pre_order(root.right) # Part of recursive case.

  def post_order(self):
    # The function has a time complexity of O(n) because it calls on a function that
    # has a time complexity of O(n).
    result = self.__post_order(self.__root)
    return f'[ {", ".join(map(str, result))} ]' if result else '[ ]' # Ensures proper format.

  def __post_order(self, root):
    # The function has a time complexity of O(n) because it visits each node once,
    # resulting in linear time complexity.
    if root is None:
      return [] # Part of base case.
    return self.__post_order(root.left) + self.__post_order(root.right) + [root.value] # Part of recursive case.

  def to_list_recursive(self):
    # The function has a time complexity of O(n) because it calls on a function that
    # has a time complexity of O(n).
    return self.__to_list_recursive(self.__root)

  def __to_list_recursive(self, root):
    # The function has a time complexity of O(n) because it visits each node once,
    # resulting in linear time complexity.
    if root is None:
      return [] # Part of base case.
    return self.__to_list_recursive(root.left) + [root.value] + self.__to_list_recursive(root.right) # Part of recursive case.

  def to_list(self):
    # The function has a time complexity of O(n) because it calls on a function that
    # has a time complexity of O(n).
    return self.__in_order(self.__root)

  def get_height(self):
    # The function has a time complexity of O(n) because it calls on a function that
    # has a time complexity of O(n).
    return self.__get_height(self.__root)

  def __get_height(self, root):
    # The function has a time complexity of O(n) because it visits each node once,
    # resulting in linear time complexity.
    if root is None:
      return 0 # Part of base case.
    return 1 + max(self.__get_height(root.left), self.__get_height(root.right)) # Part of recursive case.

  def __str__(self):
    # The function has a time complexity of O(n) because it calls on a function that
    # has a time complexity of O(n).
    return self.in_order()

if __name__ == '__main__':
  pass # Unit tests make the main section unnecessary.
