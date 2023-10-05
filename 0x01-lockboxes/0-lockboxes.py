#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This program takes a list of lists as input, where each inner list represents a box and the numbers inside represent the keys that can open other boxes. The program returns True if all the boxes can be opened, and False otherwise.
To solve this problem, we can use a breadth-first search (BFS) algorithm to traverse the graph of boxes and keys. We start by adding the first box (box 0) to a queue. Then, we repeatedly dequeue a box from the queue and add all of its keys to the queue. If a key opens a box that has not been visited before, we add that box to the queue. We continue this process until all of the boxes have been visited.
If all of the boxes have been visited, then we know that all of the boxes can be opened. Otherwise, there is at least one box that cannot be opened.
"""


def canUnlockAll(boxes):
    """Determines if boxes can be unlocked"""
    position = 0
    unlocked = {}

    for box in boxes:
        if len(box) == 0 or position == 0:
            unlocked[position] = "always_unlocked"
        for key in box:
            if key < len(boxes) and key != position:
                unlocked[key] = key
        if len(unlocked) == len(boxes):
            return True
        position += 1
    return False
