#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This program takes a list of lists as input, where each inner list represents a box and the numbers inside represent the keys that can open other boxes. The program returns True if all the boxes can be opened, and False otherwise.
To solve this problem, we can use a breadth-first search (BFS) algorithm to traverse the graph of boxes and keys. We start by adding the first box (box 0) to a queue. Then, we repeatedly dequeue a box from the queue and add all of its keys to the queue. If a key opens a box that has not been visited before, we add that box to the queue. We continue this process until all of the boxes have been visited.
If all of the boxes have been visited, then we know that all of the boxes can be opened. Otherwise, there is at least one box that cannot be opened.
"""
def canUnlockAll(boxes):
  """
  This function takes a list of lists as input, where each inner list represents a box and the numbers inside represent the keys that can open other boxes. The function returns True if all the boxes can be opened, and False otherwise.
  Args:
    boxes: A list of lists, where each inner list represents a box and the numbers inside represent the keys that can open other boxes.
  Returns:
    True if all the boxes can be opened, and False otherwise.
  """
  # Create a queue to store the boxes that need to be visited.
  queue = [0]
  # Create a set to store the boxes that have been visited.
  visited = set()
  # While there are boxes in the queue, dequeue a box and add its keys to the queue.
  while queue:
    box = queue.pop(0)
    visited.add(box)
    for key in boxes[box]:
      if key not in visited:
        queue.append(key)
  # If all of the boxes have been visited, then return True. Otherwise, return False.
  return len(visited) == len(boxes)
