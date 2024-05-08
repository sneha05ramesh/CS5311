import time
import random
import string
import matplotlib.pyplot as plt

def rabin_karp_matcher(T, P, d, q):
    n = len(T)
    m = len(P)
    h = pow(d, m - 1) % q
    p = 0
    t0 = 0

    occurrences = []

    # Preprocessing
    for i in range(m):
        p = (d * p + ord(P[i])) % q
        t0 = (d * t0 + ord(T[i])) % q

    # Matching
    for s in range(n - m + 1):
        if p == t0:
            if P == T[s:s + m]:
                occurrences.append(s)

        if s < n - m:
            t_s1 = (d * (t0 - ord(T[s]) * h) + ord(T[s + m])) % q
            t0 = t_s1

    return occurrences

def benchmark_rabin_karp_matcher(text_length_range, num_tests, d, q):
    execution_times = []

    pattern_length = 10  # Fixed pattern length

    for text_length in text_length_range:
        total_time = 0
        for _ in range(num_tests):
            # Generate random text
            text = ''.join(random.choices(string.ascii_lowercase, k=text_length))

            start_time = time.time()
            occurrences = rabin_karp_matcher(text, 'abcdefghij', d, q)  # Fixed pattern 'abcdefghij'
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
    plt.title('Rabin-Karp Matcher Benchmark')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    text_length_range = [1000, 3000, 5000, 7000, 10000]
    num_tests = 5
    d = 256  # Size of the alphabet
    q = 101  # Prime number

    execution_times = benchmark_rabin_karp_matcher(text_length_range, num_tests, d, q)
    plot_execution_times(execution_times)
