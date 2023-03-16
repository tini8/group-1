def remove_all_after(List, N):
    list = []
    for i in List:
        if i <= N:
            list.append(i)
    return list


List = [1,2,3,4,5]
N = 3
answer = remove_all_after(List, N)
print(answer)