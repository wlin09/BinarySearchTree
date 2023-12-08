import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BST_Tester(unittest.TestCase):

  def setUp(self):
    self.bst = Binary_Search_Tree()

  def test_insert_and_in_order_traversal(self):
    # Test in-order traversal after inserting elements.
    values_to_insert = [5, 3, 2, 4, 1]
    for value in values_to_insert:
      self.bst.insert_element(value)
    expected_in_order = sorted(values_to_insert)
    self.assertEqual(self.bst.in_order(), f'[ {", ".join(map(str, expected_in_order))} ]')

  def test_remove_and_in_order_traversal(self):
    # Test in-order traversal after removing elements.
    values_to_insert = [5, 3, 1, 2, 4]
    for value in values_to_insert:
      self.bst.insert_element(value)
    values_to_remove = [3, 2, 1]
    for value in values_to_remove:
      self.bst.remove_element(value)
    expected_in_order = [4, 5]
    self.assertEqual(self.bst.in_order(), f'[ {", ".join(map(str, expected_in_order))} ]')

  def test_insert_and_pre_order_traversal(self):
    # Test pre-order traversal after inserting elements.
    values_to_insert = [4, 2, 5, 1, 3]
    for value in values_to_insert:
      self.bst.insert_element(value)
    expected_pre_order = [4, 2, 1, 3, 5]
    self.assertEqual(self.bst.pre_order(), f'[ {", ".join(map(str, expected_pre_order))} ]')

  def test_remove_and_pre_order_traversal(self):
    # Test pre-order traversal after removing elements.
    values_to_insert = [5, 3, 1, 2, 4]
    for value in values_to_insert:
      self.bst.insert_element(value)
    values_to_remove = [3, 2, 1]
    for value in values_to_remove:
      self.bst.remove_element(value)
    expected_in_order = [4, 5]
    self.assertEqual(self.bst.pre_order(), f'[ {", ".join(map(str, expected_in_order))} ]')

  def test__insert_and_post_order_traversal(self):
    # Test post-order traversal after inserting elements.
    values_to_insert = [4, 2, 1, 3, 5]
    for value in values_to_insert:
      self.bst.insert_element(value)
    expected_post_order = [1, 3, 5, 4, 2]
    self.assertEqual(self.bst.post_order(), f'[ {", ".join(map(str, expected_post_order))} ]')

  def test_remove_and_post_order_traversal(self):
    # Test post-order traversal after removing elements.
    values_to_insert = [5, 3, 1, 2, 4]
    for value in values_to_insert:
      self.bst.insert_element(value)
    values_to_remove = [3, 2, 1]
    for value in values_to_remove:
      self.bst.remove_element(value)
    expected_in_order = [5, 4]
    self.assertEqual(self.bst.post_order(), f'[ {", ".join(map(str, expected_in_order))} ]')

  def test_structure_after_insert(self):
    # Test structure of tree after inserting elements.
    values_to_insert = [1, 2, 3]
    for value in values_to_insert:
      self.bst.insert_element(value)
    expected_in_order = [1, 2, 3]
    expected_pre_order = [2, 1, 3]
    expected_post_order = [1, 3, 2]
    self.assertEqual(self.bst.in_order(), f'[ {", ".join(map(str, expected_in_order))} ]')
    self.assertEqual(self.bst.pre_order(), f'[ {", ".join(map(str, expected_pre_order))} ]')
    self.assertEqual(self.bst.post_order(), f'[ {", ".join(map(str, expected_post_order))} ]')

  def test_structure_after_remove(self):
    # Test structure of tree after inserting and removing elements.
    values_to_insert = [5, 3, 1, 2, 4]
    for value in values_to_insert:
      self.bst.insert_element(value)
    values_to_remove = [3, 5]
    for value in values_to_remove:
      self.bst.remove_element(value)
    expected_in_order = [1, 2, 4]
    expected_pre_order = [2, 1, 4]
    expected_post_order = [1, 4, 2]
    self.assertEqual(self.bst.in_order(), f'[ {", ".join(map(str, expected_in_order))} ]')
    self.assertEqual(self.bst.pre_order(), f'[ {", ".join(map(str, expected_pre_order))} ]')
    self.assertEqual(self.bst.post_order(), f'[ {", ".join(map(str, expected_post_order))} ]')

  def test_empty_tree_traversals(self):
    # Test traversals on an empty tree.
    self.assertEqual(self.bst.in_order(), '[ ]')
    self.assertEqual(self.bst.pre_order(), '[ ]')
    self.assertEqual(self.bst.post_order(), '[ ]')

  def test_empty_tree_traversals_after_remove(self):
    # Test traversals on an empty tree as a result of remove.
    values_to_insert = [4, 2, 1, 3, 5]
    for value in values_to_insert:
      self.bst.insert_element(value)
    values_to_remove = [1, 2, 3, 4, 5]
    for value in values_to_remove:
      self.bst.remove_element(value)
    self.assertEqual(self.bst.in_order(), '[ ]')
    self.assertEqual(self.bst.pre_order(), '[ ]')
    self.assertEqual(self.bst.post_order(), '[ ]')

  def test_height_of_tree(self):
    # Test the height of the tree after insertion.
    values_to_insert = [1, 2]
    for i, value in enumerate(values_to_insert):
      self.bst.insert_element(value)
      self.assertEqual(self.bst.get_height(), i + 1)

  def test_remove_nonexistent_element(self):
    # Test removing a nonexistent element.
    with self.assertRaises(ValueError):
      self.bst.remove_element(10)

  def test_insert_existing_element(self):
    # Test inserting an element that already exists.
    self.bst.insert_element(1)
    with self.assertRaises(ValueError):
      self.bst.insert_element(1)

if __name__ == '__main__':
  unittest.main()