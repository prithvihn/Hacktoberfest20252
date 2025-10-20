from collections import deque
from typing import Deque, Union, List

class MonotonicQueue:
    """
    A specialized queue that maintains elements in a strictly monotonic order 
    (either increasing or decreasing) to enable O(1) retrieval of the max/min 
    element in the current queue state.
    
    Used primarily for optimizing Sliding Window Maximum/Minimum problems.
    """
    def __init__(self, mode: str = 'max'):
        """
        Initializes the queue.
        :param mode: 'max' for monotonically decreasing (to get max element), 
                     'min' for monotonically increasing (to get min element).
        """
        if mode not in ['max', 'min']:
            raise ValueError("Mode must be 'max' or 'min'")
            
        # The main deque stores the indices/values in monotonic order
        self._deque: Deque[Union[int, float]] = deque()
        self._mode = mode

    @property
    def extremum(self) -> Union[int, float, None]:
        """Returns the maximum (or minimum) element in O(1) time."""
        return self._deque[0] if self._deque else None

    def push(self, val: Union[int, float]):
        """
        Adds a value to the back of the queue, maintaining the monotonic property.
        :param val: The value to be added.
        """
        # Comparison logic depends on the mode
        if self._mode == 'max':
            # For 'max' mode, the deque is monotonically DECREASING
            # Remove smaller elements from the back before adding the new, larger/equal value
            while self._deque and self._deque[-1] < val:
                self._deque.pop()
        else: # self._mode == 'min'
            # For 'min' mode, the deque is monotonically INCREASING
            # Remove larger elements from the back before adding the new, smaller/equal value
            while self._deque and self._deque[-1] > val:
                self._deque.pop()
        
        self._deque.append(val)

    def pop_front(self, val: Union[int, float]):
        """
        Removes a value from the front if it is the current extremum. 
        Crucial for sliding window operations.
        :param val: The value being removed from the actual window.
        """
        # Only remove the front element if it matches the value being removed 
        # from the sliding window.
        if self._deque and self._deque[0] == val:
            self._deque.popleft()

# --- Example of use: Sliding Window Maximum Problem ---

def sliding_window_maximum(nums: List[int], k: int) -> List[int]:
    """
    Finds the maximum element in every sliding window of size k.
    Time Complexity: O(N) because each element is pushed and popped at most once.
    """
    if not nums or k <= 0:
        return []

    # Initialize a Monotonic Queue for 'max' mode (monotonically decreasing)
    mq = MonotonicQueue(mode='max')
    result: List[int] = []

    for i, val in enumerate(nums):
        # 1. Add the new element to the Monotonic Queue (maintains property)
        mq.push(val)

        # 2. Check if the window is formed (index i >= k-1)
        if i >= k - 1:
            # The extremum property gives the maximum of the current window
            result.append(mq.extremum)
            
            # 3. Remove the element that is sliding out of the window 
            # (element at index i - k + 1)
            old_val = nums[i - k + 1]
            mq.pop_front(old_val)
            
    return result

# Example Usage:
"""
if __name__ == '__main__':
    data = [1, 3, -1, -3, 5, 3, 6, 7]
    window_size = 3
    
    # Expected output: [3, 3, 5, 5, 6, 7]
    max_values = sliding_window_maximum(data, window_size)
    print(f"Data: {data}")
    print(f"Window Size (k): {window_size}")
    print(f"Sliding Window Maximums: {max_values}")
    
    # Another usage (e.g., minimum)
    mq_min = MonotonicQueue(mode='min')
    mq_min.push(10); mq_min.push(5); mq_min.push(12)
    print(f"Min Extremum after 10, 5, 12: {mq_min.extremum}") # Should be 5
"""
