# Priority Queue implementation in Python


# Function to heapify the tree
def heapify(arr, n, i):
    # Find the largest among root, left child and right child
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    #print("print l r",l,r)
    if l < n and arr[i] < arr[l]:
        #print("left node",arr[l])
        largest = l

    if r < n and arr[largest] < arr[r]:
        #print("right node",arr[r])
        largest = r

    # Swap and continue heapifying if root is not largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# Function to insert an element into the tree
def insert(array, newNum):
    array.append(newNum)
    size = len(array)
    for i in range((size // 2) -1, -1, -1):
            heapify(array, size, i)

# Function to delete an element from the tree
def deletenode(array, num):
    size = len(array)
    #i = 0
    for i in range(0, size):
        if num == array[i]:
            break
    #print(i)
    array[i], array[size - 1] = array[size - 1], array[i]

    del array[size - 1]

    for i in range((len(array) // 2) - 1, -1, -1):
        heapify(array, len(array), i)

def rootnode(array):
 print(array[0])

#Driver Code
arr = []

insert(arr, 3)
#insert(arr, 4)
#insert(arr, 9)
#insert(arr, 5)
#insert(arr, 2)
print("max heap",arr)
#deleteNode(arr,9)
#print("After deleting an element: ", arr)
#print("root node is:")
#rootnode(arr)