from collections import defaultdict
from copy import deepcopy
from random import shuffle, randint
import numpy as np
import os

myfile = open("names.txt")
content = myfile.read()
names = list(map(lambda x: x.lower(), content.split()))
names_dict = defaultdict(list)

# Remove the names used so far
used_names = ['geodude', 'exeggutor', 'rhyhorn', 'ninetales', 'starmie', 'ekans', 'staryu', 'sandshrew']
for name in used_names:
  used_names.remove(name)

# Reduce the size of names to test performance
shuffle(names)
names = names[:70]

# Create a dictionary where the key is the first letter of the name
for name in sorted(names):
  names_dict[name[0]].append(name)

# progress is list of 2-tuples.
# First value is the number of nodes that have been processed at that level of the call stack.
# Second value is the total number of nodes to be processed at that level of the call stack
def draw_progress(progress):
  output = ""
  for num_nodes, total_nodes in progress:
    output += (('*' * num_nodes) + ('-' * (total_nodes-num_nodes)) + '\n')
  return output

def minimax(minimizing: bool, prev_name: str, names_dict: dict, progress: list) -> (str, int):
  # Print progress with a 1/1000 chance 
  # to reduce output to terminal which slows down the program
  if randint(1, 1000) == 1000:
    os.system('clear')
    print(draw_progress(progress))
  
  # corresponding_names is a list of names whose first letter
  # is the same as the last letter of prev_name
  corresponding_names = names_dict[prev_name[-1]]
  if len(corresponding_names) == 0:
    return (None, 1) if minimizing else (None, -1)
  
  scores = []
  for i, name in enumerate(corresponding_names):
    names_dict_copy = deepcopy(names_dict)
    names_dict_copy[name[0]].remove(name)
    scores.append(minimax(not minimizing, name, names_dict_copy, progress + [(i, len(corresponding_names))])[1])
  
  if minimizing:
    return corresponding_names[np.argmin(scores)], min(scores)
  else:
    return corresponding_names[np.argmax(scores)], max(scores)

# If the retval contains 1, that means you lose
# If the retval contains -1, that means you wim
# Enter the name that the opponent and True for minimizing and the names_dict
# And the function will tell you if you can win, along with the best name to say
print(minimax(True, used_names[-1], names_dict, []))
