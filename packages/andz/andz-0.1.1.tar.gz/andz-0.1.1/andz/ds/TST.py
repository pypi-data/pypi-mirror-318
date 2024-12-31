#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: nbro

Created: 05/09/2015

Updated: 28/09/2017

# Description

Ternary-search tries (or trees) combine the time efficiency of other tries with
the space efficiency of binary-search trees.

An advantage compared to hash maps is that ternary search tries support sorting,
but the keys of a ternary-search trie can only be strings, whereas a hash map
supports any kind of hashable keys.

## TSTs vs Hashing

### Hashing

- Need to examine entire key
- Search miss and hits cost about the same
- Performance relies on hash function
- Does not support ordered symbol table operations

### TSTs

- Works only for strings (or digital keys)
- Only examines just enough key characters
- Search miss may involve only a few characters
- Supports ordered symbol table operations:
    - keys-that-match
    - keys-with-prefix
    - longest-prefix-of

### Bottom line

TSTs are:

- faster than hashing (especially for search misses)
- more flexible than red-black trees

# TODO

- Improve is_tst function

# References

- https://www.cs.upc.edu/~ps/downloads/tst/tst.html
- https://www.cs.princeton.edu/~rs/strings/
- http://algs4.cs.princeton.edu/52trie/TST.java.html
- https://www.youtube.com/watch?v=CIGyewO7868
- https://en.wikipedia.org/wiki/Ternary_search_tree
- http://stackoverflow.com/a/27178771/3924118
"""

__all__ = ["TST"]


class _TSTNode:
    """A _TSTNode has 6 fields:

    - key, which is a character;

    - value, which is None if self is not a terminal node (of an inserted
    string in the TST);

    - parent, which is a pointer to a _TSTNode representing the parent of
    self;

    - left, which is a pointer to a _TSTNode whose key is smaller
    lexicographically than key;

    - right, which is similarly a pointer to a _TSTNode whose key is greater
    lexicographically than key;

    - mid, which is a pointer to a _TSTNode whose key is the following
    character of key in an inserted string."""

    # pylint: disable=too-many-arguments
    def __init__(self, key, value=None, parent=None, left=None, mid=None, right=None):
        if not isinstance(key, str):
            raise TypeError("key must be an instance of str.")
        if not key:
            raise ValueError("key must be a string of length >= 1.")
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.mid = mid
        self.right = right

    def is_left_child(self) -> bool:
        """
        Return true if self is the left child of its parent, else false.

        If self has no parent, an ``AttributeError`` is raised.
        """
        if not self.parent:
            raise AttributeError("self does not have a parent.")
        if self.parent.left:
            return self.parent.left == self
        return False

    def is_right_child(self) -> bool:
        """
        Return true if self is the right child of its parent, else false.

        If self has no parent, an ``AttributeError`` is raised.
        """
        if not self.parent:
            raise AttributeError("self does not have a parent.")
        if self.parent.right:
            return self.parent.right == self
        return False

    def is_mid_child(self) -> bool:
        """
        Return true if self is the middle child of its parent, else false.

        If self has no parent, an ``AttributeError`` is raised.
        """
        if not self.parent:
            raise AttributeError("self does not have a parent.")
        if self.parent.mid:
            return self.parent.mid == self
        return False

    def has_children(self) -> bool:
        """
        Return true if self has a left, right or middle child, else false.
        """
        return self.left or self.right or self.mid

    def __str__(self):
        return f"{self.key}: {self.value}"

    def __repr__(self):
        return self.__str__()


class TST:
    """
    An implementation of a typical ternary-search trie (or tree).

    It does not allow (through public methods) empty strings to be inserted.

    In general, the way the ternary search tree looks like highly depends on the
    order of insertion of the keys, that is, inserting the same keys but in
    different orders produces internally a different structure or shape of the
    ternary-search tree.
    """

    def __init__(self):
        self._n = 0
        self._root = None

    @property
    def size(self) -> int:
        """
        Return the number of strings in self.
        """
        return self._n

    def is_empty(self) -> bool:
        """
        Return true if the size of self is zero, false otherwise.

        Time complexity: O(1).
        """
        return self.size == 0

    def _is_root(self, u: _TSTNode) -> bool:
        result = self._root == u
        if result:
            assert u.parent is None
        else:
            assert u.parent is not None
        return result

    def count(self) -> int:
        """Counts the number of strings in this TST.

        This method recursively passes through all the nodes and counts the ones
        which have a non None value.

        YOU SHOULD CLEARLY USE size INSTEAD: THIS METHOD IS HERE ONLY FOR THE
        FUN OF WRITING CODE!

        Time complexity: O(n), where n is the number of nodes in this TST."""
        c = self._count(self._root, 0)
        assert c == self.size
        return c

    def _count(self, node: _TSTNode, counter: int) -> int:
        """Helper method to self.count.

        Time complexity: O(m), where m is the number of nodes under node."""
        if node is None:  # Base case.
            return counter

        counter = self._count(node.left, counter)
        if node.value is not None:
            counter += 1

        counter = self._count(node.mid, counter)
        counter = self._count(node.right, counter)

        return counter

    def insert(self, key: str, value: object) -> None:
        """Inserts the key into the symbol table and associates with it value,
        overwriting an eventual associated old value, if the key is already in
        this ternary-search tree.

        If key is not an instance of str, TypeError is raised.
        If key is an empty string, ValueError is raised.
        If value is None, ValueError is raised.

        Nodes whose value is not None represent the last character of an
        inserted word.

        Time complexity: O(m + h), where m = length(key), which also represents
        how many times we follow the middle link, and h is the number of left
        and right turns. So, a lower bound of the complexity would be Ω(m)."""
        assert is_tst(self)

        if not isinstance(key, str):
            raise TypeError("key must be an instance of type str.")
        if not key:
            raise ValueError("key must be a string of length >= 1.")
        if value is None:
            raise ValueError("value cannot be None.")
        self._root = self._insert(self._root, key, value, 0)

        assert is_tst(self)

    def _insert(self, node: _TSTNode, key: str, value: object, index: int) -> _TSTNode:
        """Inserts key with value into this TST starting from node."""
        if node is None:
            node = _TSTNode(key[index])

        if key[index] < node.key:
            node.left = self._insert(node.left, key, value, index)
            node.left.parent = node
        elif key[index] > node.key:
            node.right = self._insert(node.right, key, value, index)
            node.right.parent = node
        else:  # key[index] == node.key
            if index < len(key) - 1:
                # If we are not at the end of the key, this is a match, so we
                # recursively call self._insert from index + 1, and we move to
                # the mid node (char) of node.
                #
                # Note: the last index of the key is len(key) - 1.
                node.mid = self._insert(node.mid, key, value, index + 1)
                node.mid.parent = node
            else:
                if node.value is None:
                    self._n += 1
                node.value = value

        return node

    def search(self, key: str) -> object:
        """Returns the value associated with key, if key is in this TST, else
        None.

        If key is not an instance of str, TypeError is raised.
        If key is an empty string, ValueError is raised.

        The search in a TST works as follows.

        We start at the root and we compare its character with the first
        character of key.

            - If they are the same, we follow the middle link of the root node.

            - If the first character of key is smaller lexicographically than
            the key at the root, then we take the left link or pointer.

            We do this because we know that all strings that start with
            characters that are smaller lexicographically than key[0] are on its
            left subtree.

            - If the first character of key is greater lexicographically
            than the key at the root, we take similarly the right link.

        We keep applying this idea at every node.

        Moreover, when there is a match, next time we compare the key of the
        next node with the next character of key.

        For example, if there's a match between the first node (the root) and
        key[0], we follow the middle link, and the next comparison is between
        the key of the specific next node and key[1] (not key[0]).

        Time complexity: O(m + h). Check self.insert to see what m and h are."""
        if not isinstance(key, str):
            raise TypeError("key must be an instance of type str.")
        if not key:
            raise ValueError("key must be a string of length >= 1.")

        node = self._search(self._root, key, 0)

        if node is not None:
            assert self.search_iteratively(key) == node.value
            return node.value
        assert self.search_iteratively(key) is None
        return None

    def _search(self, node: _TSTNode, key: str, index: int) -> _TSTNode:
        """Searches for the node containing the value associated with key
        starting from node.

        If returns None or a node with value None if there's no such node."""
        if node is None:
            return None

        if key[index] < node.key:
            return self._search(node.left, key, index)
        if key[index] > node.key:
            return self._search(node.right, key, index)
        if index < len(key) - 1:
            # This is a match, but we are not at the last character of key.
            return self._search(node.mid, key, index + 1)
        # This is a match, and we are at the last character of key.
        return node  # node could be None!!

    # pylint: disable=too-many-branches
    def search_iteratively(self, key: str) -> object:
        """Iterative alternative to self.search."""
        if not isinstance(key, str):
            raise TypeError("key must be an instance of type str.")
        if not key:
            raise ValueError("key must be a string of length >= 1.")

        node = self._root

        if node is None:
            return None

        # Up to the penultimate index (i.e. len(key) - 1), because if we reach
        # the penultimate character and it's a match, then we follow the mid
        # node (i.e. we end up in what's possibly the last node).
        index = 0

        while index < len(key) - 1:
            while node and key[index] != node.key:
                if key[index] < node.key:
                    node = node.left
                else:
                    node = node.right

            if node is None:  # Unsuccessful search.
                return None

            # Arriving here only if exited from the while loop because the
            # condition key[i] != node.key was false, that is
            # key[index] == node.key, thus we follow the middle link.
            node = node.mid
            index += 1

        assert index == len(key) - 1

        # If node is not None, then we may still need to go left or right, and
        # we stop when either we find a node which has the same key as the last
        # character of key, or when node ends up being set to None, i.e. the key
        # does not exist in this TST.
        while node and key[index] != node.key:
            if key[index] < node.key:
                node = node.left
            else:
                node = node.right

        if node is None:  # Unsuccessful search.
            return None
        # We exit the previous while loop because key[index] == node.key.
        return node.value  # This can be None!!

    def contains(self, key: str) -> bool:
        """Returns true if key is in this TST, False otherwise.

        Time complexity: O(m + h). See the complexity analysis of self.insert
        for more info about m and h."""
        return self.search(key) is not None

    def delete(self, key: str) -> object:
        """Deletes and returns the value associated with key in this TST, if key
        is in this TST, otherwise it returns None.

        If key is not an instance of str, TypeError is raised.
        If key is an empty string, ValueError is raised.

        Time complexity: O(m + h + k). Check self.search to see what m and h
        are. k is the number of "no more necessary" cleaned up after deletion of
        the node associated with key. Unnecessary nodes are nodes with no
        children and value equal to None."""
        assert is_tst(self)

        if not isinstance(key, str):
            raise TypeError("key must be an instance of type str.")
        if not key:
            raise ValueError("key must be a string of length >= 1.")

        # Note: calling self._search, since self.search does not return a Node,
        # but the value associated with the key passed as parameter.
        node = self._search(self._root, key, 0)

        if node is not None and node.value is not None:
            result = node.value  # Forget the string tracked by node.
            node.value = None
            self._n -= 1
            self._delete_fix(node)
        else:
            result = None

        assert is_tst(self)

        return result

    def _delete_fix(self, u: _TSTNode) -> None:
        """Does the clean up of this TST after deletion of node u."""
        assert u.value is None

        # While u has no children and his value is None, forget about u and
        # start from his parent. So, this while loop terminates when either u is
        # None, u has at least one child, or u's value is not None.
        while u and not u.has_children() and u.value is None:
            if self._is_root(u):
                assert self._n == 0
                self._root = None
                break

            if u.is_left_child():
                u.parent.left = None
            elif u.is_right_child():
                u.parent.right = None
            else:
                u.parent.mid = None

            p = u.parent
            u.parent = None
            u = p

        if u.has_children() and u.value is None:
            assert self._count(u, 0) > 0

    def traverse(self) -> None:
        """Traverses all nodes in this TST and prints the key: value
        associations.

        Time complexity: O(n), where n is the number of nodes in self."""
        self._traverse(self._root, "")

    def _traverse(self, node: _TSTNode, prefix: str) -> None:
        """Helper method to self.traverse.

        Time complexity: O(m), where m is the number of nodes under node."""
        if node is None:  # Base case.
            return

        self._traverse(node.left, prefix)
        if node.value is not None:
            print(prefix + node.key, ": ", node.value)

        self._traverse(node.mid, prefix + node.key)
        self._traverse(node.right, prefix)

    def keys_with_prefix(self, prefix: str) -> list:
        """Returns all keys in this TST that start with prefix.

        If prefix is not an instance of str, TypeError is raised.

        If prefix is an empty string, then all keys in this TST that start with
        an empty string, thus all keys are returned."""
        if not isinstance(prefix, str):
            raise TypeError("prefix must be an instance of str!")

        kwp = []

        if not prefix:
            self._keys_with_prefix(self._root, [], kwp)
        else:
            node = self._search(self._root, prefix, 0)

            if node is not None:
                if node.value is not None:
                    # A key equals to prefix was found in the TST with an
                    # associated value.
                    kwp.append(prefix)

                self._keys_with_prefix(node.mid, list(prefix), kwp)

        return kwp

    def _keys_with_prefix(self, node: _TSTNode, prefix_list: list, kwp: list) -> None:
        """Returns all keys rooted at node given the prefix given as a list of
        characters prefix_list."""
        if node is None:
            return

        self._keys_with_prefix(node.left, prefix_list, kwp)

        if node.value is not None:
            kwp.append("".join(prefix_list + [node.key]))

        prefix_list.append(node.key)
        self._keys_with_prefix(node.mid, prefix_list, kwp)

        prefix_list.pop()
        self._keys_with_prefix(node.right, prefix_list, kwp)

    def all_pairs(self) -> dict:
        """Returns all pairs of (key: value) from this TST as a Python dict."""
        pairs = {}
        self._all_pairs(self._root, [], pairs)
        return pairs

    def _all_pairs(self, node: _TSTNode, key_list: list, all_dict: list) -> None:
        if node is None:
            return

        self._all_pairs(node.left, key_list, all_dict)

        if node.value is not None:
            key = "".join(key_list + [node.key])
            assert key not in all_dict
            all_dict[key] = node.value

        key_list.append(node.key)
        self._all_pairs(node.mid, key_list, all_dict)

        key_list.pop()
        self._all_pairs(node.right, key_list, all_dict)

    def longest_prefix_of(self, query: str) -> str:
        """Returns the key in this TST which is the longest prefix of query, if
        such a key exists, else it returns None.

        If query is not a string TypeError is raised.
        If query is a string but empty, ValueError is raised.

        If this TST is empty, it returns an empty string."""
        if not isinstance(query, str):
            raise TypeError("query is not an instance of str!")
        if not query:
            raise ValueError("empty strings not allowed in this TST!")

        # It keeps track of the length of the longest prefix of query.
        length = 0

        x = self._root
        i = 0

        while x is not None and i < len(query):
            c = query[i]

            if c < x.key:
                x = x.left
            elif c > x.key:
                x = x.right
            else:
                i += 1
                if x.value is not None:
                    length = i
                x = x.mid

        return query[:length]

    def keys_that_match(self, pattern: str) -> list:
        """Returns a list of keys of this TST that match pattern.

        A key k of length m matches pattern if:

        1. m = length(pattern), and
        2. Either k[i] == pattern[i] or k[i] == '.'.

            - Example: if pattern == ".ood", then k == "good" would match, but
            not k == "foodie".

        If pattern is not a str, TypeError is raised.
        If pattern is an empty string, ValueError is raised."""
        if not isinstance(pattern, str):
            raise TypeError("pattern is not an instance of str!")
        if not pattern:
            raise ValueError("pattern cannot be an empty string")

        keys = []
        self._keys_that_match(self._root, [], 0, pattern, keys)
        return keys

    # pylint: disable=too-many-arguments
    def _keys_that_match(
        self, node: _TSTNode, prefix_list: list, i: int, pattern: str, keys: list
    ) -> None:
        """Stores in the list keys the keys that match pattern starting from
        node."""
        if node is None:
            return

        c = pattern[i]

        if c == "." or c < node.key:
            self._keys_that_match(node.left, prefix_list, i, pattern, keys)

        if c == "." or c == node.key:  # pylint: disable=consider-using-in

            if i == len(pattern) - 1 and node.value is not None:
                # If i is the last index and its value is not None.
                keys.append("".join(prefix_list + [node.key]))

            if i < len(pattern) - 1:
                prefix_list.append(node.key)
                self._keys_that_match(node.mid, prefix_list, i + 1, pattern, keys)
                prefix_list.pop()

        if c == "." or c > node.key:
            self._keys_that_match(node.right, prefix_list, i, pattern, keys)


# pylint: disable=protected-access
def is_tst(t: TST) -> bool:
    """These propositions should always be true at the BEGINNING
    and END of every PUBLIC method of this TST.

    Call this method if you want to ensure the invariants are holding."""
    if not isinstance(t, TST):
        return False
    if t._n < 0:
        return False
    if t._n == 0:
        return t._root is None
    if not isinstance(t._root, _TSTNode) or t._root.parent is not None:
        return False
    return True
