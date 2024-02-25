import logging
import pandas as pd
import numpy as np

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class Pandas1:
    def __init__(self):
        self.df = pd.DataFrame(data=np.array(
            [['Анна', 'Богдан', 'Катерина', 'Михайло', 'Олена'],
             [25, 30, 22, 35, 28],
             ['Київ', 'Львів', 'Одеса', 'Харків', 'Одеса']]
        ).T,
            columns=["Імʼя", "Вік", "Місто"]
        )
        self.df['Вік'] = pd.to_numeric(self.df['Вік'], errors='coerce')
        logging.info(f"Created DF - \n{self.df}")

    def add_int_col(self):
        self.df['Кол-во детей'] = np.random.randint(1, 100, size=len(self.df))
        logging.info(f"Added int col - \n{self.df}")

    def filter_by_threshold(self, threshold):
        filtered_df = self.df[self.df['Кол-во детей'] > threshold]
        logging.info(f"Filtered DataFrame - \n{filtered_df}")

    @staticmethod
    def load_and_display_data(file_path):
        loaded_df = pd.read_csv(file_path)
        logging.info(f"Loaded DataFrame - \n{loaded_df.head()}")

    def calculate_and_display_statistics(self):
        numeric_stats = self.df.describe()
        logging.info(f"Numeric Statistics - \n{numeric_stats}")

    def display_unique_values(self, column_name):
        unique_values = self.df[column_name].unique()
        logging.info(f"Unique values in column '{column_name}' - \n{unique_values}")


if __name__ == '__main__':
    pandas_instance = Pandas1()
    pandas_instance.add_int_col()
    pandas_instance.filter_by_threshold(50)
    pandas_instance.load_and_display_data('wine.csv')
    pandas_instance.calculate_and_display_statistics()
    pandas_instance.display_unique_values('Місто')
