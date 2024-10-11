import pandas as pd
def ReadArrayFromCsv(Filenname):
    df=pd.read_csv(Filenname)
    return df

def BubbleSort(Array, ColumnsArray):
    n = len(Array)
    if len(ColumnsArray)>1:
        for i in range(n):
            for j in range(0, n - i - 1):
                should_swap = False
                for k in range(len(ColumnsArray)):
                    if Array[j][ColumnsArray[k]] > Array[j + 1][ColumnsArray[k]]:
                        should_swap = True
                        break
                    elif Array[j][ColumnsArray[k]] < Array[j + 1][ColumnsArray[k]]:
                        should_swap = False
                        break  
                if should_swap:
                    Array[j], Array[j + 1] = Array[j + 1], Array[j]
    else:
        number=ColumnsArray[0]
        for i in range(n):
            for j in range(n-i-1):
                if Array[j][number]>Array[j+1][number]:
                    Array[j], Array[j+1]=Array[j+1], Array[j]
    return Array

def SelectionSort(Array, ColumnsArray):
    n = len(Array)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            for k in range(len(ColumnsArray)):
                if Array[j][ColumnsArray[k]] < Array[min_idx][ColumnsArray[k]]:
                    min_idx = j
                    break 
                elif Array[j][ColumnsArray[k]] > Array[min_idx][ColumnsArray[k]]:
                    break
        Array[i], Array[min_idx] = Array[min_idx], Array[i]
    return Array


def InsertionSort(Array, ColumnsArray):
    n = len(Array)
    for i in range(1, n):
        key = Array[i]
        j = i - 1
        shift = False
        while j >= 0:
            for k in range(len(ColumnsArray)):
                if Array[j][ColumnsArray[k]] > key[ColumnsArray[k]]:
                    shift = True
                    break
                elif Array[j][ColumnsArray[k]] < key[ColumnsArray[k]]:
                    shift = False
                    break
            else:
                shift = True
            if shift:
                Array[j + 1] = Array[j]
                j -= 1
            else:
                break
        Array[j + 1] = key
    return Array

def merge(left, right, ColumnsArray):
    sorted_Array = []
    i = j = 0
    while i < len(left) and j < len(right):
        for k in range(len(ColumnsArray)):
            if left[i][ColumnsArray[k]] < right[j][ColumnsArray[k]]:
                sorted_Array.append(left[i])
                i += 1
                break
            elif left[i][ColumnsArray[k]] > right[j][ColumnsArray[k]]:
                sorted_Array.append(right[j])
                j += 1
                break
        else:
            sorted_Array.append(left[i])
            i += 1
    while i < len(left):
        sorted_Array.append(left[i])
        i += 1

    while j < len(right):
        sorted_Array.append(right[j])
        j += 1

    return sorted_Array


def MergeSort(Array, ColumnsArray):
    if len(Array) <= 1:
        return Array

    mid = len(Array) // 2
    left_half = MergeSort(Array[:mid], ColumnsArray)
    right_half = MergeSort(Array[mid:], ColumnsArray)

    return merge(left_half, right_half, ColumnsArray)

def QuickSort(Array, ColumnsArray):
    if len(Array) <= 1:
        return Array
    else:
        pivot = Array[0]        
        lesser = []
        greater = []
        
        for row in Array[1:]:
            for k in range(len(ColumnsArray)):
                if row[ColumnsArray[k]] < pivot[ColumnsArray[k]]:
                    lesser.append(row)
                    break
                elif row[ColumnsArray[k]] > pivot[ColumnsArray[k]]:
                    greater.append(row)
                    break 
            else:
                lesser.append(row)

        return QuickSort(lesser, ColumnsArray) + [pivot] + QuickSort(greater, ColumnsArray)

def LargestNumber(Array,index):
    column_data = [row[index] for row in Array if type(row[index]) == int]
    return max(column_data)

def CountingSort(Array, ColumnArray):
    TemporaryArray = Array.copy()
    
    for col_index in ColumnArray:
        maximum = LargestNumber(TemporaryArray, col_index)        
        count = [0] * (maximum + 1)
        output = [None] * len(TemporaryArray)
        for row in TemporaryArray:
            if type(row[col_index]) == int:
                num = int(row[col_index])
                count[num] += 1
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        for i in range(len(TemporaryArray)):
            row = TemporaryArray[i]
            if type(row[col_index]) == int:
                num = int(row[col_index])
                output[count[num] - 1] = row
                count[num] -= 1
        TemporaryArray = output

    return TemporaryArray

def CountingSortForRadix(Array, column, digit):
    buckets = [[] for _ in range(10)]
    for row in Array:
        Index = (row[column] // 10**digit) % 10
        buckets[Index].append(row)
    return [row for bucket in buckets for row in bucket]

def RadixSort(Array, ColumnsArray):
    MaximumValues = [max(row[column] for row in Array) for column in ColumnsArray]
    max_digits = [len(str(value)) for value in MaximumValues]

    for column, max_digit in zip(ColumnsArray, max_digits):
        for digit in range(max_digit):
            Array = CountingSortForRadix(Array, column, digit)

    return Array

def BucketSort(Array, ColumnsArray):
    buckets = {}
    
    for col_index in ColumnsArray:
        for row in Array:
            key = row[col_index]
            if key not in buckets:
                buckets[key] = []
            buckets[key].append(row)
    sorted_buckets = sorted(buckets.items())
    sorted_output = []
    for key, bucket in sorted_buckets:
        sorted_output.extend(bucket)

    return sorted_output

def OddEvenSort(Array, ColumnsArray):
    n = len(Array)
    sorted = False

    while not sorted:
        sorted = True

        # Perform odd indexed passes
        for i in range(1, n, 2):
            if i < n - 1:
                if CompareRows(Array[i], Array[i + 1], ColumnsArray) > 0:
                    Array[i], Array[i + 1] = Array[i + 1], Array[i]  # Swap
                    sorted = False

        # Perform even indexed passes
        for i in range(0, n, 2):
            if i < n - 1:
                if CompareRows(Array[i], Array[i + 1], ColumnsArray) > 0:
                    Array[i], Array[i + 1] = Array[i + 1], Array[i]  # Swap
                    sorted = False

    return Array

def CompareRows(row1, row2, ColumnsArray):
    for col in ColumnsArray:
        if row1[col] < row2[col]:
            return -1
        elif row1[col] > row2[col]:
            return 1
    return 0  # They are equal

def ShellSort(Array, ColumnsArray):
    n = len(Array)
    gap = n // 2  # Start with a large gap

    while gap > 0:
        # Perform a gapped insertion sort for this gap size
        for i in range(gap, n):
            temp = Array[i]
            j = i

            # Shift earlier gap-sorted elements up until the correct location for data[i] is found
            while j >= gap and compare_rows(Array[j - gap], temp, ColumnsArray) > 0:
                Array[j] = Array[j - gap]
                j -= gap

            # Put temp (the original data[i]) in its correct location
            Array[j] = temp
        
        gap //= 2  # Reduce the gap for the next iteration
    
    return Array

def compare_rows(row1, row2, ColumnsArray):
    for col in ColumnsArray:
        value1 = row1[col]
        value2 = row2[col]

        if value1 < value2:
            return -1
        elif value1 > value2:
            return 1
    return 0  # They are equal
def CombSort(arr, key_columns):
    def get_key(item):
        # Build a tuple of keys based on the columns provided in key_columns
        return tuple(item[col] for col in key_columns)

    def next_gap(gap):
        # Shrink gap using the shrink factor (1.3 is a common choice)
        gap = (gap * 10) // 13
        if gap < 1:
            return 1
        return gap

    n = len(arr)
    gap = n
    swapped = True

    # Start with a large gap and then reduce it until the list is sorted
    while gap != 1 or swapped:
        # Calculate next gap
        gap = next_gap(gap)
        swapped = False

        # Compare elements with the current gap
        for i in range(n - gap):
            # Compare tuples based on the selected key columns
            if get_key(arr[i]) > get_key(arr[i + gap]):
                # Swap if they are out of order
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
    return arr
def GenomeSort(arr, key_columns):
    def get_key(item):
        # Create a tuple of values from the specified key columns
        return tuple(item[col] for col in key_columns)

    # Sort the list using Python's built-in sort, which performs Timsort
    # Timsort is highly efficient for practical use cases and handles multi-key sorting
    arr.sort(key=get_key)
    return arr


