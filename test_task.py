# Task 1
def unique_list(spisok: list):
  return list(set(spisok))


# Task 2
def range_list(min_item: int,max_item: int):
  return list(range(min_item,max_item + 1))


# Task 3
class Point:
  def __init__(self,x,y):
    self.x = x
    self.y = y

  def get_distance(self,point):
    return (((self.x - point.x)**2 + (self.y - point.y)**2), 0,5)

  def set_dot_x(self,x):
    self.x = x

  def set_dot_y(self,y):
    self.y = y


# Task 4
def sorting_strings(strings: list):
    sorted_strings = sorted(strings, key=len)
    asc_length = sorted_strings[:]
    desc_length = list(reversed(sorted_strings))
    
    return asc_length, desc_length
