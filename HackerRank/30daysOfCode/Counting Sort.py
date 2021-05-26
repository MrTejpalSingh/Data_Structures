def countingSort(arr):
    freq_arr = [0 for i in range(100)]
    for i in arr:
        if i <= 100:
            freq_arr[i] += 1