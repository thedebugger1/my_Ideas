# Remember, M becomes f, and F creates M
def solution(x, y):
    goal = (int(x), int(y))
    start = (1, 1)
    gen = [start]
    c = 0
    while gen:
        next_gen = []
        for m, f in gen:
            if (m, f) == goal:
                return str(c)
            mf = m + f
            if mf <= goal[0]:
                next_gen.append((mf, f))
            if mf <= goal[1]:
                next_gen.append((m, mf))

        # Go to next generation
        gen = next_gen
        c += 1
    return 'impossible'


print(solution('4', '7'))
print(solution('9', '8'))








