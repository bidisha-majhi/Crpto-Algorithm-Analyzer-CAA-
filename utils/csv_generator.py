import pandas as pd


class CSVGenerator:

    def __init__(self, output_csv=None):
        if output_csv:
            self.df = self.read_csv(output_csv)
        else:
            self.df = pd.DataFrame(columns=['Algorithm', 'File Size', 'Mode', 'Time Taken', 'Power Consumption'])

    def read_csv(self, output_csv):
        df = pd.read_csv("results/" + output_csv, header=0, index_col=0)
        return df

    def add_or_update_value(self, algorithm, file_size, mode, time_taken, power_consumption, index=None):
        print(f"Added Some Value in index {index or len(self.df.index)}...")
        self.df.loc[index or len(self.df.index)] = [algorithm, file_size, mode, time_taken, power_consumption]
        print(f"Successfully added value in index {index or len(self.df.index) - 1}")

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
        self.df.to_csv('results/' + file_name, header=True, index=True)
        print(f"File saved successfully: {file_name}")


if __name__ == "__main__":
    a = CSVGenerator(output_csv='output.csv')

    algorithm = "AES 128".title().strip()
    file_size = 100
    mode = "encryption".title().strip()
    time_taken = 10
    power_consumed = 10
    # a.add_or_update_value(algorithm, file_size, mode, time_taken, power_consumed)
    # a.delete_value([3,5,6])
    a.reset_index()
    a.save_csv()
    print("")
    print(a.df)
