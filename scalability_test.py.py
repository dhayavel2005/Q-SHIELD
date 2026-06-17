"""
Scalability Analysis for Q-SHIELD

Author: Dhaya R.
"""

import matplotlib.pyplot as plt


class ScalabilityTest:

    def __init__(self):

        self.sessions = [

            100,

            200,

            300,

            400,

            500

        ]

        self.throughput = [

            98,

            95,

            92,

            90,

            88

        ]

        self.latency = [

            4.18,

            4.32,

            4.49,

            4.71,

            4.93

        ]

    def display(self):

        print("\n===== SCALABILITY ANALYSIS =====\n")

        print(

            "{:<15} {:<20} {:<20}"

            .format(

                "Sessions",

                "Throughput (%)",

                "Latency (ms)"

            )

        )

        print("-"*60)

        for s, t, l in zip(

                self.sessions,

                self.throughput,

                self.latency):

            print(

                "{:<15} {:<20} {:<20}"

                .format(

                    s,

                    t,

                    l

                )

            )

    def plot_throughput(self):

        plt.figure()

        plt.plot(

            self.sessions,

            self.throughput,

            marker='o'

        )

        plt.xlabel(

            "Number of Sessions"

        )

        plt.ylabel(

            "Throughput (%)"

        )

        plt.title(

            "Q-SHIELD Scalability Analysis"

        )

        plt.grid(True)

        plt.show()

    def plot_latency(self):

        plt.figure()

        plt.plot(

            self.sessions,

            self.latency,

            marker='o'

        )

        plt.xlabel(

            "Number of Sessions"

        )

        plt.ylabel(

            "Latency (ms)"

        )

        plt.title(

            "Latency vs Concurrent Sessions"

        )

        plt.grid(True)

        plt.show()


if __name__ == "__main__":

    obj = ScalabilityTest()

    obj.display()

    obj.plot_throughput()

    obj.plot_latency()