def solution(arr, k):
    cnt = 0
    quick_sort_ASC(arr, 0, len(arr) - 1, cnt, k)
    print(cnt)


# 퀵 정렬 - 오름차순 (Quick Sort - Ascending)
def partition_ASC(arr, start, end, cnt, k):
    pivot = arr[start]
    L = start
    R = end
    done = False

    while not done:
        while L <= len(arr) - 1 and arr[L] <= pivot:
            if R - L <= k:
                if L == len(arr) - 1:  # 리스트를 벗어나는 것을 방지
                    break
                L += 1

        while R >= 0 and pivot < arr[R]:
            if R - L <= k:
                if R == 0:  # 리스트를 벗어나는 것을 방지
                    break
            R -= 1

        if R <= L:  # 교차했다면
            done = True

        else:  # 교차하지 않았다면
            arr[L], arr[R] = arr[R], arr[L]

    cnt += 1
    arr[start], arr[R] = arr[R], arr[start]
    return R  # 새로운 pivot 위치 리턴


def quick_sort_ASC(arr, start, end, cnt, k):
    if start < end:
        pivot = partition_ASC(arr, start, end, cnt, k)
        quick_sort_ASC(arr, start, pivot - 1, cnt, k)
        quick_sort_ASC(arr, pivot + 1, end, cnt, k)
    return arr

