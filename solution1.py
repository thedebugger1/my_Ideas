def solution(data, n):
    newdata = []
    if len(data) < 100:
        for x in data:
            if data.count(x) <= n:
                newdata.append(x)
    return newdata


print(solution([1, 1, 2, 3], 1))



# data = [1, 1, 2, 5, 7, 11, 4, 5, 1, 6, 2, 6, 1, 3, 9, 5, 1, 0, 6, 4 ,5, 2, 3]
# n = 1
# newdata = []
# for x in data:
#     if data.count(x) <= n: 
#         newdata.append(x)
#
# print(*newdata, sep=", ")
