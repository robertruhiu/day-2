def find_max_min(n):
  #This function returns the min and max num in a list
  # If the min==max, it returns the num of elements in the list
  list = []
  max_num = max(n)
  min_num = min(n)
  if min_num == max_num:
    num_of_elements = len(n)
    list.append(num_of_elements)
  else:
    list.append(min_num)
    list.append(max_num)
  return list
