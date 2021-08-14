def solution(priorities, location):
    cnt = 0
    queue = [x for x in range(len(priorities))]
    flag = False
    while queue and priorities:
        front = queue[0]
        front_p = priorities[0]

        if front_p < max(priorities):
            queue.append(front)
            priorities.append(front_p)
        else:
            cnt += 1
            if front == location:
                break
        queue.pop(0)
        priorities.pop(0)

    return cnt