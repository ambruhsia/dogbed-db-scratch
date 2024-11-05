*DBDB (Dog Bed Database)*

DBDB is a simple Python-based key-value database that allows you to store key-value pairs persistently on disk. It is designed to be durable, ensuring data survival in the face of system crashes and error conditions. Unlike many other databases, DBDB does not require all data to be held in memory, which allows it to store larger datasets than would be possible in RAM alone.

The database is built around the concept of immutable binary trees, with separate logical and physical layers. The logical layer abstracts key-value storage, while the physical layer handles disk storage.

*Architecture Overview*
interface.py: Implements the public dictionary-like API and integrates the BinaryTree for storage management.
logical.py: Defines the logical layer, including the base classes for interacting with the binary tree.
binary_tree.py: Implements the binary tree data structure used to manage keys and values.
storage.py: Handles disk storage, file management, and locking mechanisms.

**References**
***DBDB: Dog Bed Database by Taavi Burns***
CouchDB and the concepts of immutable data structures
