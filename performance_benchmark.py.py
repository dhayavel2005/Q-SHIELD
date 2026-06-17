"""
Performance Benchmark Module for Q-SHIELD

Measures:

1. Key Generation Time
2. Encapsulation Time
3. Decapsulation Time
4. Session Setup Latency

Author: Dhaya R.
"""

import time
import statistics

from src.kyber_module import KyberKEM


class PerformanceBenchmark:

    def __init__(self):

        self.kem = KyberKEM()

    def benchmark(self, runs=50):

        keygen_times = []

        encap_times = []

        decap_times = []

        total_times = []

        for i in range(runs):

            start_total = time.time()

            # Key Generation

            t1 = time.time()

            pk, sk = self.kem.generate_keypair()

            t2 = time.time()

            keygen_times.append(
                (t2 - t1) * 1000
            )

            # Encapsulation

            t3 = time.time()

            ct, ss1 = self.kem.encapsulate(pk)

            t4 = time.time()

            encap_times.append(
                (t4 - t3) * 1000
            )

            # Decapsulation

            t5 = time.time()

            ss2 = self.kem.decapsulate(
                ct,
                sk
            )

            t6 = time.time()

            decap_times.append(
                (t6 - t5) * 1000
            )

            end_total = time.time()

            total_times.append(

                (end_total - start_total)

                * 1000

            )

        print("\n========== RESULTS ==========\n")

        print(

            "Key Generation : "

            f"{statistics.mean(keygen_times):.3f} ms"

        )

        print(

            "Encapsulation : "

            f"{statistics.mean(encap_times):.3f} ms"

        )

        print(

            "Decapsulation : "

            f"{statistics.mean(decap_times):.3f} ms"

        )

        print(

            "Session Setup : "

            f"{statistics.mean(total_times):.3f} ms"

        )

        print("\nStandard Deviation")

        print(

            "Encapsulation : "

            f"{statistics.stdev(encap_times):.3f}"

        )

        print(

            "Decapsulation : "

            f"{statistics.stdev(decap_times):.3f}"

        )


if __name__ == "__main__":

    bench = PerformanceBenchmark()

    bench.benchmark(runs=50)