

def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num)/len(list_num), 2)

assert average_num([1,2]) == 1.5
assert average_num(['a', 'b']) == 'Bad request'
assert average_num([1,'a']) == 'Bad request'
assert average_num([-1, -2]) == -1.5
assert average_num([1,2,3,4]) == 2.5
assert average_num([1.1,2.5,3.9]) == 2.5
assert average_num([1.122,2.522,3]) == 2.21
assert average_num([1, 1, 1, 1]) == 1.0
assert average_num([0,0]) == 0
assert average_num([0,1,-2,2]) == 0.25