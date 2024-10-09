from matplotlib import pyplot as plt
from pandas import DataFrame


class HDHP:
    """
    A class for computing health insurance costs.
    """

    data = {"expenses": list(range(0, 40000, 100))}

    def __init__(
        self,
        annual_premium,
        employer_hsa_contribution,
        deductible,
        out_of_pocket_max,
        coinsurance,
        name="",
    ):
        self.annual_premium = annual_premium
        self.employer_hsa_contribution = employer_hsa_contribution
        self.deductible = deductible
        self.out_of_pocket_max = out_of_pocket_max
        self.coinsurance = coinsurance
        self.name = name

        HDHP.data[self.name] = self.get_plot_data()

    def get_annual_cost(self, expected_bills):
        amount_under_deductible = min(self.deductible, expected_bills)
        amount_over_deductible = max(0, expected_bills - self.deductible)
        cooinsurance_maximum = self.out_of_pocket_max - self.deductible

        return (
            self.annual_premium
            - self.employer_hsa_contribution
            + amount_under_deductible
            + min(
                cooinsurance_maximum,
                self.coinsurance * amount_over_deductible,
            )
        )

    def get_plot_data(self):
        y = []
        cost = 0
        for cost in HDHP.data["expenses"]:
            total_cost = self.get_annual_cost(cost)
            y += [total_cost]

        return y

    @classmethod
    def plot(cls):
        df = DataFrame(cls.data)
        df.set_index("expenses", inplace=True)
        print(df)
        df.plot(
            xlabel="Expected Health Insurance Expenses",
            ylabel="Total Health Insurance Costs",
        )
        plt.show()
  

if __name__ == "__main__":
    a = HDHP(
        annual_premium=840 + 1284 + 672,
        employer_hsa_contribution=0,
        deductible=5000,
        out_of_pocket_max=10000,
        coinsurance=0.2,
        name="HDHP1",
    )

    HDHP.plot()
