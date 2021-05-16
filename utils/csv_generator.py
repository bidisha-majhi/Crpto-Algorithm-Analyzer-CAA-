import pandas as pd
import os

RESULT_BASE_PATH='results/'

class CSVGenerator:

    def __init__(self, output_csv=None):
        if output_csv and os.path.exists(RESULT_BASE_PATH+output_csv):
            self.df = self.read_csv(RESULT_BASE_PATH+output_csv)
        else:
            self.df = pd.DataFrame(columns=['ALGORITHM', 'FILE NAME', 'FILE SIZE', 'MODE', 'DURATION', 'ENERGY CONSUMPTION'])

    def read_csv(self, output_csv):
        df = pd.read_csv(output_csv, header=0, index_col=0)
        return df

    def add_or_update_value(self, algorithm, file_name, file_size, mode, duration, energy_consumed, index=None):
        print(f"Added Some Value in index {index if index is not None else len(self.df.index)}...")
        self.df.loc[index if index is not None else len(self.df.index)] = [algorithm, file_name, file_size, mode, duration, energy_consumed]
        print(f"Successfully added value in index {index if index is not None else len(self.df.index)-1}")

    def delete_value(self, index):
        try:
            if type(index) == int:
                index = [index]
            index = list(index)
            print(f"Deleting Row {index}...")
            self.df.drop(index, axis=0, inplace=True)
            print(f"Sucessfully Deleted Row: {index}")
        except KeyError:
            print(f"Row not found: {index}")

    def reset_index(self):
        self.df.reset_index(inplace=True, drop=True)
        print("Successfully reset index")

    def save_csv(self, file_name='output.csv'):
        self.df.to_csv(RESULT_BASE_PATH + file_name, header=True, index=True)
        print(f"File saved successfully: {file_name}")


if __name__ == "__main__":
    a = CSVGenerator(output_csv='output.csv')

    algorithm = "AES 128".title().strip()
    file_name = "Somefile.txt"
    file_size = 100
    mode = "encryption".title().strip()
    duration = 10
    energy_consumed = 10
    a.add_or_update_value(algorithm, file_name, file_size, mode, duration, energy_consumed)
    # a.delete_value([3,5,6])
    a.reset_index()
    a.save_csv()
    print("")
    print(a.df)
