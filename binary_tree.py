import pickle

import logical
print(dir(logical))  # This will list all the attributes of the logical module

from logical import LogicalDataHandler
from logical import ValueRef

class BinaryNode(object):
# ...
    def store_refs(self, storage):
        self.value_ref.store(storage)
        self.left_ref.store(storage)
        self.right_ref.store(storage)


class BinaryNodeRef(ValueRef):
    def prepare_to_store(self, storage):
        if self._referent:
            self._referent.store_refs(storage)

    @staticmethod
    def referent_to_string(referent):
        return pickle.dumps({
            'left': referent.left_ref.address,
            'key': referent.key,
            'value': referent.value_ref.address,
            'right': referent.right_ref.address,
            'length': referent.length,
        })

class BinaryTree(LogicalDataHandler):
    # ...

    def fetch_value(self, node, key):
        while node is not None:
            if key < node.key:
                node = self._navigate(node.left_reference)
            elif node.key < key:
                node = self._navigate(node.right_reference)
            else:
                return self._navigate(node.value_reference)
        raise KeyError("Key not found.")

    def insert_node(self, current_node, key, value_reference):
        if current_node is None:
            new_node = BinaryNode(
                self.node_reference_class(), key, value_reference, self.node_reference_class(), 1)
        elif key < current_node.key:
            new_node = BinaryNode.from_node(
                current_node,
                left_reference=self.insert_node(
                    self._navigate(current_node.left_reference), key, value_reference))
        elif current_node.key < key:
            new_node = BinaryNode.from_node(
                current_node,
                right_reference=self.insert_node(
                    self._navigate(current_node.right_reference), key, value_reference))
        else:
            new_node = BinaryNode.from_node(current_node, value_reference=value_reference)
        return self.node_reference_class(referent=new_node)