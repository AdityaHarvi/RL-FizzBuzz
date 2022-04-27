import matplotlib.pyplot as plot


class Plotter():
    def __init__(self):
        plot.title("Errors per Episode (Behavioural Policy)")
        plot.ylabel("Errors Detected")
        plot.xlabel("Episode #")

        self.xData = []
        self.yData = []


    def addData(self, dataType, data):
        if dataType == "x":
            self.xData.append(data)
        else:
            self.yData.append(data)


    def showPlot(self):
        plot.plot(self.xData, self.yData)
        plot.show()
