
import pandas
from pandas.core.frame import DataFrame
from pandas.core.series import Series
import matplotlib
from src.parser import ColumnNames, PortfolioData
from copy import copy, deepcopy


class Analyzer():
    def __init__(self, csv_data: PortfolioData) -> None:
        self.csv_data = csv_data

    def analyze(self):
        percent_allocation_df = self.calculate_weights()
        sorted_percent_allocation_df = deepcopy(
            percent_allocation_df).sort_values(by="Percent Of Portfolio", ascending=False, ignore_index=True)
        # plot = percent_allocation_df.plot(
        #     kind="pie", labels=percent_allocation_df["Symbol"], y="Percent Of Portfolio", autopct='%1.1f%%', figsize=(8, 4.5), legend=False, pctdistance=1.5, fontsize=6)
        writer = pandas.ExcelWriter("output.xlsx")
        sorted_percent_allocation_df.to_excel(
            writer, "Portfolio Security Weights", index=False)
        writer.save()

        # get target weights
        result = pandas.read_excel("./input.xlsx")
        val = self.csv_data.value_usd_column[25]

        # using current total market value calculate target market values from target weights
        result["target value"] = val * result["Target"]

        # compare target market value to current actual market value (they should be close or the same -- say within 1% for now)

        # Calculate difference Target Value - Initial Value for each holding

        # Divide each holding's difference by share price

        # round down
        sorted_percent_allocation_df["Percent Of Portfolio"] = 100 * \
            sorted_percent_allocation_df["Percent Of Portfolio"]
        return sorted_percent_allocation_df

    def calculate_weights(self) -> pandas.DataFrame:
        total = self.csv_data.value_usd_column.iloc[-1]
        cash = self.csv_data.value_usd_column.iloc[-2]
        securities_values = self.csv_data.value_usd_column[0:-1]
        symbols = self.csv_data.symbol_column[0:-1]

        percentages = []
        for i, symbol in enumerate(symbols):
            percentages.append(securities_values[i] / total)

        percentages_series = Series(percentages)
        percentages_series.name = "Percent Of Portfolio"
        percent_allocation_df = pandas.concat(
            [symbols, percentages_series], axis=1)

        return percent_allocation_df


class WeightsFileGenerator():
    def __init__(self):
        pass
