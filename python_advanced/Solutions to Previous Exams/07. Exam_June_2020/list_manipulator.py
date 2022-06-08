from collections import deque

def list_manipulator(nums, *args):
    nums = deque(nums)
    args = list(args)
    if args[0] == 'add' and args[1] == 'beginning':
        for arg in reversed(args[2:]):
            nums.appendleft(arg)
    elif args[0] == 'add' and args[1] == 'end':
        for arg in args[2:]:
            nums.append(arg)
    elif args[0] == 'remove' and args[1] == 'beginning':
        if len(args) > 2:
            index = args[2]
            while index:
                nums.popleft()
                index -= 1
        else:
            nums.popleft()
    elif args[0] == 'remove' and args[1] == 'end':
        if len(args) > 2:
            index = args[2]
            while index:
                nums.pop()
                index -= 1
        else:
            nums.pop()
    return list(nums)

print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))