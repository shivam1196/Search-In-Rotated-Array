# PROBLEM 8
## Search in a Rotated Sorted Array
The expected run time complexity for this solution was suppose to be O(log n)
Hence we made a few enhancement to find out the pivot element by using binary search as it has a runtime
complexity of O(log n).
After finding the pivot element, it became easy to find an element based upon the pivot element value by using
binary search

<br>

### Algorithm:
1. Find Pivot :
    we need to find the element in the array whose next is smaller than the element using binary search
    First check for middle element if found return mid else
    Check if middle element is less than first element then find pivot in left subarray
    otherwise in right sub-array
2. Divide array in Two parts from pivot and search for element in both subarrays using binary search


### Time Complexity Analysis:
 O(log n)(finding the pivot element) + O(log n)(searching the element) = O(2logn) which is O(log n)


### Space Complexity Analysis:
• O(n) to store array
