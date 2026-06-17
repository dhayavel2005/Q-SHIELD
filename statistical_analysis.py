"""
Statistical Analysis for Q-SHIELD

Computes:

1. Mean
2. Standard Deviation
3. 95% Confidence Interval

Author: Dhaya R.
"""

import statistics
import math


class StatisticalAnalysis:

    def __init__(self):

        # Example data from 50 runs

        self.session_setup = [

            4.18, 4.22, 4.11, 4.20, 4.16,

            4.19, 4.21, 4.14, 4.17, 4.18

        ] * 5

    def analyze(self):

        mean_val = statistics.mean(

            self.session_setup

        )

        std_val = statistics.stdev(

            self.session_setup

        )

        n = len(

            self.session_setup

        )

        margin = (

            1.96 *

            std_val /

            math.sqrt(n)

        )

        lower = mean_val - margin

        upper = mean_val + margin

        print(

            "\n===== STATISTICAL ANALYSIS ====="

        )

        print(

            "\nNumber of Runs :",

            n

        )

        print(

            "Mean : "

            f"{mean_val:.3f} ms"

        )

        print(

            "Standard Deviation : "

            f"{std_val:.3f}"

        )

        print(

            "95% Confidence Interval : "

            f"[{lower:.3f}, "

            f"{upper:.3f}]"

        )


if __name__ == "__main__":

    obj = StatisticalAnalysis()

    obj.analyze()
