import pandas as pd
import os

# load data
class Acquisition:
    def __init__(self, currency, *args, **kwargs):
        self.currency = currency
        self.DATASETS_BASE_DIR = '../datasets/'
        
        if self.currency == 'usd':
            self.file = os.path.join(self.DATASETS_BASE_DIR, 'USD_IDR Historical Data.csv')
        elif self.currency == 'jpy':
            self.file = os.path.join(self.DATASETS_BASE_DIR, 'JPY_IDR Historical Data.csv')
        else:
            print('datasets not found.')
    
    def loadData(self):
        dataframe = pd.read_csv(self.file, sep=',')
        self.dataframe = dataframe
        
    def cleaning(self):
        # conver object to time in date column
        self.dataframe['Date'] = self.dataframe.Date.apply(
            lambda x: pd.to_datetime(x).strftime('%Y-%m-%d')
        )
        # replace commas symbol
        self.dataframe = self.dataframe.replace(',', '', regex=True)
        # clear % symbol
        self.dataframe = self.dataframe.replace('%', '', regex=True)
        
class Preprocessing:
    def split(self):
        n_datasets = len(self.dataframe)
        train_scale = int(0.8*n_datasets)
        self.training = self.dataframe[:train_scale]
        self.testing = self.dataframe[train_scale:]
        