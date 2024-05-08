import time
import random
import string
import matplotlib.pyplot as plt

def compute_prefix_function(P):
    m = len(P)
    prefix_function = [0] * m
    k = 0

    for q in range(1, m):
        while k > 0 and P[k] != P[q]:
            k = prefix_function[k - 1]
        if P[k] == P[q]:
            k += 1
        prefix_function[q] = k

    return prefix_function

def kmp_matcher(T, P):
    n = len(T)
    m = len(P)
    prefix_function = compute_prefix_function(P)
    q = 0

    occurrences = []

    for i in range(n):
        while q > 0 and P[q] != T[i]:
            q = prefix_function[q - 1]
        if P[q] == T[i]:
            q += 1
        if q == m:
            occurrences.append(i - m + 1)
            q = prefix_function[q - 1]

    return occurrences

def benchmark_kmp_matcher(text_length_range, pattern_length, num_tests):
    execution_times = []

    for text_length in text_length_range:
        total_time = 0
        for _ in range(num_tests):
            # Generate random text
            text = ''.join(random.choices(string.ascii_lowercase, k=text_length))
            pattern = ''.join(random.choices(string.ascii_lowercase, k=pattern_length))

            start_time = time.time()
            occurrences = kmp_matcher(text, pattern)
            end_time = time.time()

            total_time += end_time - start_time

        avg_time = total_time / num_tests
        execution_times.append((text_length, avg_time))

    return execution_times

def plot_execution_times(execution_times):
    text_lengths = [time[0] for time in execution_times]
    execution_times = [time[1] for time in execution_times]

    plt.figure(figsize=(10, 6))
    plt.plot(text_lengths, execution_times, marker='o')
    plt.xlabel('Text Length')
    plt.ylabel('Execution Time (s)')
    plt.title('KMP Matcher Benchmark')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    text_length_range = [1000, 3000, 5000, 7000,10000]
    pattern_length = 10  # Fixed pattern length
    num_tests = 5

    execution_times = benchmark_kmp_matcher(text_length_range, pattern_length, num_tests)
    plot_execution_times(execution_times)
