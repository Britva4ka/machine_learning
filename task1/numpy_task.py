import numpy as np
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class NumPy1:
    def __init__(self):
        logging.info('NumPy1 started:')
        self.massive = np.random.randint(0, 100, 10)
        logging.info(f"Created massive - \n{self.massive}")

    def mean_median_std(self):
        logging.info(f"Mean: {self.massive.mean()}")

        logging.info(f"Median: {np.median(self.massive)}")

        logging.info(f"Std: {self.massive.std()}")

    def replace_pairs_by_zeros(self):
        self.massive[self.massive % 2 == 0] = 0
        logging.info(f"{self.massive} is replaced by zeros")


class NumPy2:
    def __init__(self):
        logging.info('NumPy2 started:')
        self.massive = np.random.randint(0, 100, (3, 3))
        logging.info(f"Created massive - \n{self.massive}")

    def first_row(self):
        logging.info(f"First row - {self.massive[0]}")

    def last_col(self):
        logging.info(f"Last col - {self.massive[:, -1]}")

    def diagonal(self):
        logging.info(f"Diagonal - {self.massive.diagonal()}")


class NumPy3:
    def __init__(self):
        logging.info('NumPy3 started:')
        self.massive_2d = np.random.randint(0, 100, (3, 3))
        logging.info(f"Created massive - \n{self.massive_2d}")
        self.massive_1d = np.random.randint(0, 100, (3,))
        logging.info(f"Created massive - \n{self.massive_1d}")

    def broadcasting(self):
        logging.info(f"Result of broadcasting - \n{self.massive_2d + self.massive_1d}")


class NumPy4:
    def __init__(self):
        logging.info('NumPy4 started:')
        self.massive_2d = np.random.randint(0, 100, (5, 5))
        logging.info(f'Created massive - \n{self.massive_2d}')

    def unique_items(self):
        logging.info(f"Unique items - \n{np.unique(self.massive_2d)}")

    def row_sum_is_bigger_than(self, value: int = 250):
        result = self.massive_2d[np.sum(self.massive_2d, axis=1) > value]
        logging.info(f"Rows with summ bigger than {value} - \n{result}")


class NumPy5:
    def __init__(self):
        logging.info('NumPy5 started:')
        self.massive = np.arange(1, 21)
        logging.info(f"Created massive - \n{self.massive}")

    def reshape(self):
        self.massive = self.massive.reshape([4, 5])
        logging.info(f"Massive reshaped - \n{self.massive}")


if __name__ == '__main__':
    numpy_1 = NumPy1()
    numpy_1.mean_median_std()
    numpy_1.replace_pairs_by_zeros()

    numpy_2 = NumPy2()
    numpy_2.first_row()
    numpy_2.last_col()
    numpy_2.diagonal()

    numpy_3 = NumPy3()
    numpy_3.broadcasting()

    numpy_4 = NumPy4()
    numpy_4.unique_items()
    numpy_4.row_sum_is_bigger_than()

    numpy5 = NumPy5()
    numpy5.reshape()
