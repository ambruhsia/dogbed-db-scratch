class ValueRef(object):
# ...
    def store(self, storage):
        if self._referent is not None and not self._address:
            self.prepare_to_store(storage)
            self._address = storage.write(self.referent_to_string(self._referent))
            
class LogicalDataHandler(object):
    # ...

    def retrieve(self, key):
        if not self._storage.is_locked:
            self._update_tree_reference()
        return self._fetch(self._navigate(self._tree_reference), key)
    
    def update_tree_reference(self):
        self._tree_reference = self.node_reference_class(
            address=self._storage.get_root_address())
        
    def insert(self, key, value):
        if self._storage.lock():  # Lock storage before proceeding
            self._update_tree_reference()
        self._tree_reference = self._insert_node(
            self._navigate(self._tree_reference), key, self.value_reference_class(value))
        
    def commit(self):
        self._tree_ref.store(self._storage)
        self._storage.commit_root_address(self._tree_ref.address)
        
        
    