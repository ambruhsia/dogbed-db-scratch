# dbdb/storage.py

class Storage(object):
    # ...
    def commit_root_address(self, root_address):
        self.lock()
        self._f.flush()
        self._seek_superblock()
        self._write_integer(root_address)
        self._f.flush()
        self.unlock()

    def acquire_lock(self):
        if not self.is_locked:
            portalocker.lock(self._file_handle, portalocker.LOCK_EX)
            self.is_locked = True
            return True
        else:
            return False
