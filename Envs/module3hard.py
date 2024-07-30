
def calculate_structure_sum(lst):
    sm = 0
    for i in lst:
        if isinstance(i, dict):
            sm += calculate_structure_sum(dic(i))
        elif isinstance(i, tuple):
            sm += calculate_structure_sum(tup(i))
        elif isinstance(i, list):
            sm += calculate_structure_sum(i)
        elif isinstance(i, set):
            sm += calculate_structure_sum(st(i))
        elif isinstance(i, str):
            sm += len(i)
        elif isinstance(i, int):
            sm += i
    return sm

def dic(elem):
    lst = [element for pair in elem.items() for element in pair]
    return lst

def tup(elem):
    lst = list(elem)
    return lst

def st(elem):
    if isinstance(elem,set):
        lst = list(elem)
    return lst

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)