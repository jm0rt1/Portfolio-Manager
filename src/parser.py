from typing import Optional
import pandas
import enum
from pathlib import Path
from dataclasses import dataclass


class ColumnNames(str, enum.Enum):
    SYMBOL = "Symbol"
    LAST_PRICE_USD = "Last Price $"
    CHANGE_USD = "Change $"
    CHANGE_PCT = "Change %"
    QTY = "Quantity"
    PRICE_PAID_USD = "Price Paid $"
    DAYS_GAIN_USD = "Day's Gain $"
    TOTAL_GAIN_USD = "Total Gain $"
    VALUE_USD = "Value $"


@dataclass
class PortfolioData():
    df: pandas.DataFrame

    @property
    def symbol_column(self):
        return self.df[ColumnNames.SYMBOL]

    @property
    def last_price_usd_column(self):
        return self.df[ColumnNames.LAST_PRICE_USD]

    @property
    def change_usd_column(self):
        return self.df[ColumnNames.CHANGE_USD]

    @property
    def change_pct_column(self):
        return self.df[ColumnNames.CHANGE_PCT]

    @property
    def quantity_column(self):
        return self.df[ColumnNames.QTY]

    @property
    def price_paid_column(self):
        return self.df[ColumnNames.PRICE_PAID_USD]

    @property
    def days_gain_column(self):
        return self.df[ColumnNames.DAYS_GAIN_USD]

    @property
    def total_gain_column(self):
        return self.df[ColumnNames.TOTAL_GAIN_USD]

    @property
    def value_usd_column(self):
        col = self.df[ColumnNames.VALUE_USD]
        return col


class Parser():
    def __init__(self, path: Path = Path("./data/PortfolioDownload.csv")):
        self.__csv_data: Optional[pandas.DataFrame] = None
        try:
            with open(path, "r") as fp:
                self.__csv_data = pandas.read_csv(fp, header=7)
                pass
        except:
            raise

    @property
    def portfolio_data(self) -> PortfolioData:
        if self.__csv_data is not None:
            return PortfolioData(self.__csv_data)
        else:
            raise AttributeError("csv_data was not initialized properly")
