def XOR(n):
    val = n % 4
    if val == 0:
        return n
    if val == 1:
        return 1
    if val == 2:
        return n + 1
    return 0


def solution(start, length):
    if length == 1:
        return start
    val = XOR(start + 2 * (length - 1))
    if start > 1:
        val = val ^ XOR(start - 1)
    for i in range(length - 2):
        elems = length - 2 - i
        init = start + length * (2 + i) - 1
        val = val ^ XOR(init + elems) ^ XOR(init)
    return val


print(solution(9, 7))
# print(XOR(16))
# print(17^18^19^20)
# def solution(start, length):
#     size = length*length
#     list1 = []
#     list2 = []
#     x = (length*2)-1
#     for i in range(start, start+size):
#         list1.append(i)
#     for y in range(start, start+x):
#         list2.append(y)
#     if length == 1:
#         return 1
#     ans =
