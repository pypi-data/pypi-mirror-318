#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: nbro

Created: 01/08/2015

Updated: 28/09/2017

# Description

## Red-black tree property

1. Every node is either red or black.

2. The root is black.

3. Every NIL or leaf node is black.

4. If a node is red, then both its children are black, which also means that
there cannot be two red nodes in a row.

5. For every node x, each path from x to its descendant leaves has the same
number of black nodes.

## Lemma

The height h(x) of a red-black tree with n internal nodes is at most

    2 * log₂(n + 1),

that is,

    h(x) <= 2 * log₂(n + 1),

which is equivalent to

    h(x) / 2 <= log₂(n + 1),

which is equivalent to

    n >= 2^(h(x) / 2) - 1.

To possibly better understand the previous statements, we can perform the
reversed reasoning:

    n >= 2^(h(x) / 2) - 1 ⇔

    n + 1 >= 2^(h(x) / 2)

Now, we log both parts:

    log₂(n + 1) >= log₂(2^(h(x) / 2)) ⇔

    log₂(n + 1) >= h(x) / 2 * log₂(2) ⇔

    log₂(n + 1) >= h(x) / 2 * 1 ⇔

    2 * log₂(n + 1) >= h(x)


### Proof

We want to prove (by induction) that, for all x, size(x) >= 2^bh(x) - 1.

1. Base case: x is a leaf, so size(x) = 0 and bh(x) = 0.

2. Induction hypothesis: consider y₁, y₂, and x such that

    parent(y₁) = parent(y₂) = x,

and assume () that

    size(y₁) >= 2^bh(y₁) - 1, and
    size(y₂) >= 2^bh(y₂) - 1.

We want to prove: size(x) >= 2^bh(x) - 1.

1.3. Induction step

size(x) = size(y₁) + size(y₂) + 1 >= (2^bh(y₁) - 1) + (2^bh(y₂) - 1) + 1

Since

        +---------------------------------+
        | bh(y),      if color(y) = red   |
bh(x) = |                                 |
        | bh(y) + 1,  if color(y) = black |
        +---------------------------------+

size(x) >= (2^(bh(x) - 1) - 1) + (2^(bh(x) - 1) - 1) + 1 = (2^bh(x) - 1).

Since every red node has black children, in every path from x to a leaf
node, at least half the nodes are black, thus

    bh(x) >= h(x) / 2.

So: n = size(x) >= 2^(h(x) / 2) - 1.

Therefore: h(x) <= 2 * log₂(n + 1).

## Red-black tree operations

A red-black tree works as a binary-search tree for search, insert, etc, so the
complexity of those operations is T(n) = O(h), that is T(n) = O(log₂(n)), which
is also the worst case complexity.

# References

- https://en.wikipedia.org/wiki/Red%E2%80%93black_tree
- Slides by prof. A. Carzaniga
- Chapter 13 of Introduction to Algorithms (3rd ed.) by CLRS
"""

import math

from andz.ds.BST import BST, _BSTNode, is_bst

__all__ = ["RBT", "is_rbt"]

RED = "RED"
BLACK = "BLACK"


class _RBTNode(_BSTNode):
    """Class to represent a node of a RBT."""

    # pylint: disable=too-many-arguments
    def __init__(self, key, color=BLACK, parent=None, left=None, right=None):
        _BSTNode.__init__(self, key, parent, left, right)
        self.color = color


class RBT(BST):
    """Red-black tree, which is a self-balancing binary-search tree.

    Since it's self-balancing operations such as inserting, searching or
    deletion all take O(log₂(n))."""

    def __init__(self):
        BST.__init__(self)

    def insert(self, key) -> None:
        """Inserts key into this RBT.

        This operation is similar to the insert operation of a classical BST,
        but, in this case, the red-black tree property must be maintained, so
        additional work is needed.

        There are several cases of inserting into a RBT to handle:

        1. key is the root node.

        2. key.parent is BLACK.

        3. key.parent and the uncle of key are RED.

        The uncle of key will be the left child of key.parent.parent, if
        key.parent is the right child of key.parent.parent, otherwise the uncle
        will be the right child of key.parent.parent.

        4. key.parent is RED, but key.uncle is BLACK (or None).

        key.grandparent exists because key.parent is RED.

            4.1. key is added to the right of a left child of key.parent.parent
            (grandparent).

            4.2. or key is added to the left of a right child of
            key.parent.parent.

            4.3. key is added to the left of a left child of key.parent.parent.

            4.4. or key is added to the right of a right child of
            key.parent.parent.

        _fix_insertion handles these cases in the same order as above.

        Time complexity: O(log₂(n))."""
        assert is_rbt(self)

        if key is None:
            raise ValueError("key cannot be None")

        key_node = _RBTNode(key)

        c = self._root  # Current node.
        p = None  # Current node's parent.

        while c is not None:
            p = c
            if key_node.key < c.key:
                c = c.left
            else:  # key.key >= c.key
                c = c.right

        key_node.parent = p

        # while loop was not executed even once.
        # Case 1: node is inserted as root.
        if p is None:
            self._root = key_node
        elif p.key > key_node.key:
            p.left = key_node
        else:  # p.key < key.key
            p.right = key_node

        key_node.color = RED
        self._n += 1
        self._fix_insertion(key_node)

        assert is_rbt(self)

    def _fix_insertion(self, u: _RBTNode) -> None:
        # u is the root and we color it BLACK.
        if u.parent is None:
            u.color = BLACK

        elif u.parent.color == BLACK:
            return

        elif u.parent.color == RED and (u.uncle is not None and u.uncle.color == RED):
            u.parent.color = BLACK
            u.uncle.color = BLACK
            u.grandparent.color = RED
            self._fix_insertion(u.grandparent)

        elif u.parent.color == RED and (u.uncle is None or u.uncle.color == BLACK):

            # u is added as a right child to a node that is the left child.
            if u.parent.is_left_child() and u.is_right_child():

                # left_rotation does not violate the property: all paths from
                # any given node to its leaf nodes contain the same number of
                # black nodes.
                self._left_rotate(u.parent)

                # With the previous _left_rotate call, u.parent has become the
                # left child of u, or, u bas become the parent of what before
                # was u.parent.
                #
                # We can pass to case 5, where we have 2 red nodes in a row,
                # specifically, u.parent and u, which are both left children of
                # their parents.

                self._fix_insertion(u.left)

            # u is added as a left child to a node that is the right child.
            elif u.parent.is_right_child() and u.is_left_child():
                self._right_rotate(u.parent)
                self._fix_insertion(u.right)

            # u is added as a left child to a node that is the left child.
            elif u.parent.is_left_child() and u.is_left_child():
                # Note: grandparent is known to be black, since its former child
                # could not have been RED without violating property 4.
                self._right_rotate(u.grandparent)
                u.parent.color = BLACK
                u.parent.right.color = RED

            # u is added as a right child to a node that is the right child.
            elif u.parent.is_right_child() and u.is_right_child():
                self._left_rotate(u.grandparent)
                u.parent.color = BLACK
                u.parent.left.color = RED

            else:
                assert False

    def _left_rotate(self, u: _RBTNode) -> _RBTNode:
        """Left rotates the subtree rooted at node u.

        Returns the node which is at the previous position of u, that is it
        returns the parent of u.

        Time complexity: O(1)."""
        assert u.has_right_child()

        u.right.parent = u.parent

        # Only the root has a None parent.
        if not u.has_parent():
            self._root = u.right

        # Checking if u is a left or a right child, in order to set the new left
        # or right child respectively of its parent.
        elif u.is_left_child():
            u.parent.left = u.right
        else:
            u.parent.right = u.right

        u.parent = u.right

        # The new right child of u becomes what is the left child of its
        # previous right child.
        u.right = u.parent.left

        # Set u to be the parent of its new right child.
        if u.has_right_child():
            u.right.parent = u

        # Set u to be the new left child of its new parent.
        u.parent.left = u
        return u.parent

    def _right_rotate(self, u: _RBTNode) -> _RBTNode:
        """Right rotates the subtree rooted at node u.

        Time complexity: O(1)."""
        assert u.has_left_child()

        u.left.parent = u.parent

        if not u.has_parent():
            self._root = u.left
        elif u.is_left_child():
            u.parent.left = u.left
        else:
            u.parent.right = u.left

        u.parent = u.left
        u.left = u.parent.right

        if u.has_left_child():
            u.left.parent = u

        u.parent.right = u
        return u.parent

    # pylint: disable=too-many-statements, too-many-branches
    def delete(self, key: object) -> None:
        """Delete key from this RBT object.

        Time complexity: O(log₂(n))."""
        assert is_rbt(self)

        # A few checks of the inputs given.
        if key is None:
            raise ValueError("key cannot be None")

        key_node = self._search_key_iteratively(key, self._root)
        if key_node is None:
            raise LookupError("key not in this BST")

        # If key has 2 non-leaf children, then replace key with its successor.
        # Note: we exchange also the colors of key and its successor.
        if key_node.has_left_child() and key_node.has_right_child():
            s = self._successor(key_node)
            self._switch(key_node, s)
            key_node.color, s.color = s.color, key_node.color

        # At least one of the children must be None. Particularly, if key was
        # exchanged with its successor, key now should not have a left child.
        assert not key_node.has_left_child() or not key_node.has_right_child()

        # At this point key has at most 1 child.
        # Keep in mind this when reading the next cases!

        # If key is a red node and it has a child, we simply replace it with its
        # child c, which must be black by property 4.

        # This can only occur when key has 2 leaf children, because if key had a
        # black non-leaf child on one side, but just a leaf child on the other
        # side, then the count of black nodes on both sides would be different,
        # thus the tree would violate property 5.
        if key_node.color == RED:

            # A few checks while in alpha stage.
            assert not key_node.has_left_child() and not key_node.has_right_child()
            assert key_node != self._root

            if key_node.is_left_child():
                key_node.parent.left = None
            else:
                key_node.parent.right = None

        else:  # key.color == BLACK

            # One of the children of key is red.

            # Simply removing key could break properties 4, i.e., both children
            # of every red node are black, because key.parent could be red, and
            # 5, i.e. all paths from any given node to its leaf nodes contain
            # the same number of black nodes), but if we repaint c (the child)
            # BLACK, both of these properties are preserved.

            if key_node.has_left_child() and key_node.left.color == RED:
                if self._root != key_node:
                    if key_node.is_left_child():
                        key_node.parent.left = key_node.left
                    else:
                        key_node.parent.right = key_node.left

                key_node.left.parent = key_node.parent
                key_node.left.color = BLACK

                if self._root == key_node:
                    self._root = key_node.left

            elif key_node.has_right_child() and key_node.right.color == RED:
                if self._root != key_node:
                    if key_node.is_left_child():
                        key_node.parent.left = key_node.right
                    else:
                        key_node.parent.right = key_node.right

                key_node.right.parent = key_node.parent
                key_node.right.color = BLACK

                if self._root == key_node:
                    self._root = key_node.right
            else:
                # This the complex case: both key and c (the child) are BLACK.

                # This can only occur when deleting a black node which has 2
                # leaf children, because if the black node key had a black
                # non-leaf child on one side but just a leaf child on the other
                # side, then the count of black nodes on both sides would be
                # different, thus the tree would have been an invalid red–black
                # tree by violation of property 5.
                assert not key_node.has_left_child() and not key_node.has_right_child()

                # 6 cases
                if self._root != key_node:

                    assert key_node.sibling is not None

                    # Note: key.sibling cannot be None, because otherwise the
                    # subtree containing it would have fewer black nodes than
                    # the subtree containing key.
                    #
                    # Specifically, the subtree containing key would have a
                    # black height of 2, whereas the one containing the sibling
                    # would have a black height of 1.
                    self._delete_case_1(key_node)

                    # We begin by replacing key with its child c.
                    # Note: both children of key are leaf children.
                    if key_node.is_left_child():
                        key_node.parent.left = None
                    else:
                        key_node.parent.right = None

                else:
                    self._root = None

        self._n -= 1

        assert is_rbt(self)

    def _delete_case_1(self, u: _RBTNode) -> None:
        # This check is necessary because this function is also called from the
        # _delete_case_3 function.
        if u.parent is not None:
            self._delete_case_2(u)

    def _delete_case_2(self, u: _RBTNode) -> None:
        if u.sibling.color == RED:

            assert u.parent.color == BLACK

            u.sibling.color = BLACK
            u.parent.color = RED

            if u.is_left_child():
                self._left_rotate(u.parent)
            else:
                self._right_rotate(u.parent)

            assert u.sibling.color == BLACK

        self._delete_case_3(u)

    # pylint: disable=too-many-boolean-expressions
    def _delete_case_3(self, u: _RBTNode) -> None:
        # Not sure if the children of u.sibling can be None.
        if (
            u.parent.color == BLACK
            and u.sibling.color == BLACK
            and (
                (u.sibling.left and u.sibling.left.color == BLACK) or not u.sibling.left
            )
            and (
                (u.sibling.right and u.sibling.right.color == BLACK)
                or not u.sibling.right
            )
        ):

            u.sibling.color = RED
            self._delete_case_1(u.parent)
        else:
            self._delete_case_4(u)

    # pylint: disable=too-many-boolean-expressions
    def _delete_case_4(self, u: _RBTNode) -> None:
        # Not sure if the children of u.sibling can be None.
        if (
            u.parent.color == RED
            and u.sibling.color == BLACK
            and (
                (u.sibling.left and u.sibling.left.color == BLACK) or not u.sibling.left
            )
            and (
                (u.sibling.right and u.sibling.right.color == BLACK)
                or not u.sibling.right
            )
        ):

            u.sibling.color = RED
            u.parent.color = BLACK
        else:
            self._delete_case_5(u)

    def _delete_case_5(self, u: _RBTNode) -> None:
        assert u.sibling is not None

        if u.sibling.color == BLACK:
            if (
                u.is_left_child()
                and (not u.sibling.right or u.sibling.right.color == BLACK)
                and u.sibling.left.color == RED
            ):

                u.sibling.color = RED
                u.sibling.left.color = BLACK
                self._right_rotate(u.sibling)

            elif (
                u.is_right_child()
                and (not u.sibling.left or u.sibling.left.color == BLACK)
                and u.sibling.right.color == RED
            ):

                u.sibling.color = RED
                u.sibling.right.color = BLACK
                self._left_rotate(u.sibling)

        self._delete_case_6(u)

    def _delete_case_6(self, u: _RBTNode) -> None:
        assert u.sibling is not None

        u.sibling.color, u.parent.color = u.parent.color, u.sibling.color

        if u.is_left_child():
            assert u.sibling.right
            u.sibling.right.color = BLACK
            self._left_rotate(u.parent)
        else:
            assert u.sibling.left
            u.sibling.left.color = BLACK
            self._right_rotate(u.parent)

    def remove_max(self) -> None:
        """Removes the greatest element from self.

        Time complexity: O(log₂(n))."""
        assert is_rbt(self)
        if self._root is not None:
            m = self.maximum()
            assert m is not None
            self.delete(m)
            assert is_rbt(self)

    def remove_min(self) -> None:
        """Removes the smallest element from self.

        Time complexity: O(log₂(n))."""
        assert is_rbt(self)
        if self._root is not None:
            m = self.minimum()
            assert m is not None
            self.delete(m)
            assert is_rbt(self)


def black_height(n: _RBTNode) -> int:
    """Returns the black-height of the node n."""
    if n is None:
        return 1

    if not isinstance(n, _RBTNode):
        raise TypeError("n must be an instance of _RBTNode")

    left_bh = black_height(n.left)
    right_bh = black_height(n.right)

    if left_bh != right_bh:
        return -1
    return left_bh + (1 if n.color == BLACK else 0)


def upper_bound_height(t: RBT) -> bool:
    """Returns true if the height of the red-black tre t is bounded above by
    log₂(n + 1)."""
    return t.height() <= 2 * math.log2(t.size + 1)


# pylint: disable=protected-access
def is_rbt(t: RBT) -> bool:
    """Returns true if t is a valid RBT object, false otherwise."""

    def are_all_red_or_black(t: RBT) -> bool:
        """Returns true if all colors are either RED or BLACK."""

        def h(n: _RBTNode) -> bool:
            if n is not None:
                if (
                    n.color != BLACK and n.color != RED
                ):  # pylint: disable=consider-using-in
                    return False
                return h(n.right) and h(n.left)
            return True

        return h(t._root)

    def is_root_black(t: RBT) -> bool:
        """Returns true if the root is BLACK (or it is None), false
        otherwise."""
        if t._root is not None:
            return t._root.color == BLACK
        return True

    def has_not_consecutive_red_nodes(t: RBT) -> bool:
        def h(n: _RBTNode) -> bool:
            if n is not None:
                if n.parent is not None and n.color == RED and n.parent.color == RED:
                    return False
                if n.parent is None and n.color == RED:
                    return False
                return h(n.left) and h(n.right)
            return True

        return h(t._root)

    def all_paths_have_same_black_height(t: RBT) -> bool:
        return black_height(t._root) != -1

    def are_all_rbt_nodes(t: RBT) -> bool:
        def h(n: _RBTNode) -> bool:
            if n is not None:
                if not isinstance(n, _RBTNode):
                    return False
                return h(n.left) and h(n.right)
            return True

        return h(t._root)

    if not is_bst(t):
        return False

    if not isinstance(t, RBT):
        return False

    if not are_all_rbt_nodes(t):
        return False

    if not upper_bound_height(t):
        return False

    return (
        are_all_red_or_black(t)
        and is_root_black(t)
        and has_not_consecutive_red_nodes(t)
        and all_paths_have_same_black_height(t)
    )
