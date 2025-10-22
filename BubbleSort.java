/**
 * Title: BubbleSort.java
 * Description: Implements the Bubble Sort algorithm in Java.
 * Time Complexity: O(n^2) - suitable for learning, not for large datasets.
 */

public class BubbleSort {

    /**
     * Sorts an array of integers using the Bubble Sort algorithm.
     * In each pass, it 'bubbles up' the largest element to its correct position.
     *
     * @param arr The array of integers to be sorted.
     */
    public static void sort(int[] arr) {
        int n = arr.length;
        boolean swapped;
        
        // Traverse through all array elements
        for (int i = 0; i < n - 1; i++) {
            swapped = false;
            
            // Last i elements are already in place, so we don't need to check them.
            for (int j = 0; j < n - 1 - i; j++) {
                
                // Compare two adjacent elements
                if (arr[j] > arr[j + 1]) {
                    
                    // Swap arr[j] and arr[j+1]
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }
            
            // Optimization: If no two elements were swapped by inner loop, then the array is sorted
            if (!swapped) {
                break;
            }
        }
    }

    /**
     * Helper method to print the array.
     * @param arr The array to print.
     */
    public static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + (i == arr.length - 1 ? "" : ", "));
        }
        System.out.println();
    }

    // --- Main method for testing the implementation ---
    public static void main(String[] args) {
        int[] unsortedArray = {64, 34, 25, 12, 22, 11, 90};
        
        System.out.print("Unsorted Array: ");
        printArray(unsortedArray);
        
        // Call the sort method
        sort(unsortedArray);
        
        System.out.print("Sorted Array (Bubble Sort): ");
        printArray(unsortedArray); // Expected output: 11, 12, 22, 25, 34, 64, 90
    }
}
