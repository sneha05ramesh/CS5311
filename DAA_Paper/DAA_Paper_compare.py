import time
import random
import string
import matplotlib.pyplot as plt

def naive_string_matcher(T, P):
    n = len(T)
    m = len(P)
    occurrences = []

    for s in range(n - m + 1):
        if P == T[s:s + m]:
            occurrences.append(s)

    return occurrences

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

def benchmark_algorithms(text_length_range, pattern_length, num_tests, d, q):
    naive_times = []
    rabin_karp_times = []
    kmp_times = []

    for text_length in text_length_range:
        total_naive_time = 0
        total_rabin_karp_time = 0
        total_kmp_time = 0

        for _ in range(num_tests):
            text = ''.join(random.choices(string.ascii_lowercase, k=text_length))
            pattern = ''.join(random.choices(string.ascii_lowercase, k=pattern_length))

            # Naive
            start_time = time.time()
            occurrences = naive_string_matcher(text, pattern)
            end_time = time.time()
            total_naive_time += end_time - start_time

            # Rabin-Karp
            start_time = time.time()
            occurrences = rabin_karp_matcher(text, pattern, d, q)
            end_time = time.time()
            total_rabin_karp_time += end_time - start_time

            # KMP
            start_time = time.time()
            occurrences = kmp_matcher(text, pattern)
            end_time = time.time()
            total_kmp_time += end_time - start_time

        avg_naive_time = total_naive_time / num_tests
        avg_rabin_karp_time = total_rabin_karp_time / num_tests
        avg_kmp_time = total_kmp_time / num_tests

        naive_times.append(avg_naive_time)
        rabin_karp_times.append(avg_rabin_karp_time)
        kmp_times.append(avg_kmp_time)

    return naive_times, rabin_karp_times, kmp_times

def plot_execution_times(text_length_range, naive_times, rabin_karp_times, kmp_times):
    plt.figure(figsize=(10, 6))
    plt.plot(text_length_range, naive_times, label='Naive')
    plt.plot(text_length_range, rabin_karp_times, label='Rabin-Karp')
    plt.plot(text_length_range, kmp_times, label='KMP')
    plt.xlabel('Text Length')
    plt.ylabel('Execution Time (s)')
    plt.title('Comparison of String Matching Algorithms')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    text_length_range = [1000, 3000, 5000, 7000,10000]
    pattern_length = 10
    num_tests = 5
    d = 256  # Size of the alphabet
    q = 101  # Prime number

    naive_times, rabin_karp_times, kmp_times = benchmark_algorithms(text_length_range, pattern_length, num_tests, d, q)
    plot_execution_times(text_length_range, naive_times, rabin_karp_times, kmp_times)
