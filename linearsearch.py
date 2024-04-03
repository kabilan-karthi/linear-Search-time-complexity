import time
import matplotlib.pyplot as plt

def linear_search(arr, target):
    start_time = time.time()
    
    for i in range(len(arr)):
        if arr[i] == target:
            end_time = time.time()
            return i, end_time - start_time
    
    end_time = time.time()
    return -1, end_time - start_time

def plot_graph(input_sizes, execution_times):
    plt.plot(input_sizes, execution_times, marker='o')
    plt.xlabel('Input Size')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Linear Search Time Complexity')
    plt.grid(True)
    plt.show()

def main():
    input_sizes = [100, 1000, 5000, 10000, 20000]
    execution_times = []
    
    for size in input_sizes:
        arr = list(range(size))
        target = size - 1
        
        index, time_taken = linear_search(arr, target)
        execution_times.append(time_taken)
        
        print(f"Input Size: {size}, Time Taken: {time_taken} seconds")
    
    plot_graph(input_sizes, execution_times)

if __name__ == '__main__':
    main()
