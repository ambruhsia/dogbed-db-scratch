from binary_tree import BinaryTree
from storage import Storage

class DBDB(object):

    def __init__(self, file_handle):
        self._storage_handler = Storage(file_handle)
        self._tree_structure = BinaryTree(self._storage_handler)

    def __getitem__(self, key):
        self._check_if_closed()
        return self._tree_structure.get(key)

    def _check_if_closed(self):
        if self._storage_handler.closed:
            raise ValueError('Database is closed.')
    def set_item(self, key, value):
        self._check_if_open()
        return self._tree_structure.set(key, value)
    def commit(self):
        self._assert_not_closed()
        self._tree.commit()
        