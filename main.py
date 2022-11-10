from random import randint

import random
from datetime import datetime
random.seed(datetime.now())

# random data sample to ensure more than one data sample gets used.
_items = [randint(0, 10) for n in range(10)] # this list may have dupes
print(_items)


# this is the control data - this is for cross-validation
s_items = list(set([n for n in _items]))
sorted(s_items)
print(s_items)
expected_first_max = s_items[-1]
expected_second_max = s_items[-2]
print('expected_first_max = {}'.format(expected_first_max))
print('expected_second_max = {}'.format(expected_second_max))
##################################################################################


# this function uses one coded loop however because the first_max can appear at the end of the list one must execute the loop twice.
def first_and_second_max(items):
  items = list(set(items))  # the list must not have dupes for any of this to work
  def get_a_max(alist):
    maximum = -99999999999999999
    for v in items:
      maximum = max(v, maximum)
    return maximum


  first_max = get_a_max(items)
  items = set(items) - set([first_max]) # remove all instances of first_max and reconsider
  second_max = get_a_max(items)
  return first_max, second_max

try:
  first_max, second_max = first_and_second_max(_items)
  assert first_max == expected_first_max, 'Check your code, something went wrong with the first_max'
  assert second_max == expected_second_max, 'Check your code, something went wrong with the second_max'
  print('first_max = {}'.format(first_max))
  print('second_max = {}'.format(second_max))
except:
  print('Cross validation failed.')
else:
  print('Cross validation succeeded.')
  