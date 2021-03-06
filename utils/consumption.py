import pyRAPL


class ConsumptionMeasure:

    def __init__(self):
        pyRAPL.setup()

        self.report = pyRAPL.outputs.DataFrameOutput()
        self.measure_obj = pyRAPL.Measurement('consumption')

    def measure(self, func, epoch=2**20):
        return_obj = None
        self.epoch = epoch

        self.measure_obj.begin()

        for _ in range(self.epoch):
            return_obj = func()

        self.measure_obj.end()

        #print(self.measure_obj.result)
        self.result = self.measure_obj.result
        return return_obj

    def get_energy_consumption(self):
        return self.result.pkg[0]/self.epoch

    def get_duration(self):
        return self.result.duration/self.epoch


if __name__ == "__main__":

    consumption_measure = ConsumptionMeasure()
    consumption_measure.measure(lambda: print("Hello World"), epoch=2**10)
    print("Energy Consumption (in micro Joules)", consumption_measure.get_energy_consumption())
    print("Time Taken (in microseconds)", consumption_measure.get_duration())

