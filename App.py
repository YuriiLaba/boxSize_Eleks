from tkinter import *

WORK_AREA = 50

class App:
    def __init__(self, master):
        self.master = master
        master.title("Box Sizer")
        # master.geometry("auto")

        self.sensorsButton = Button(master, text="Sensors", width=25, height=10, background='red',
                               command=lambda: self.measure(self.get_distance()))
        self.sensorsButton.grid(row=0, column=0)

        self.cameraButton = Button(master, text="Camera", width=25, height=10, background='yellow', command=self.measure)
        self.cameraButton.grid(row=0, column=1)

        self.clearButton = Button(master, text="Clear Results", width=15, height=5, background='pink', command=self.clear)
        self.clearButton.grid(row=0, column=3)


        self.resultSensors = Label(master, width=25, height=10, background='grey')
        self.resultSensors.grid(row=1, column=0)

        self.resultCamera = Label(master, width=25, height=10, background='grey')
        self.resultCamera.grid(row=1, column=1)



    def get_distance(self):
        distances = []
        length_firstSensor = 15
        distances.append(length_firstSensor)
        length_secondSensor = 15
        distances.append(length_secondSensor)

        width_firstSensor = 15
        distances.append(width_firstSensor)
        width_secondSensor = 15
        distances.append(width_secondSensor)

        height_firstSendor = 15
        distances.append(height_firstSendor)
        return distances

    def measure(self, distances):
        length = WORK_AREA - (distances[0]+distances[1])
        width = WORK_AREA - (distances[2] + distances[3])
        height = WORK_AREA - distances[4]
        self.resultSensors.config(text="Measured using distances sensors" + '\n' + '\n'
                                       + "Length: " + str(length) + '\n'
                                       + "Width: " + str(width) + '\n'
                                       + "Height: " + str(height)
                                  )


    def clear(self):
        self.resultSensors.config(text="")
        self.resultCamera.config(text="")

root = Tk()
my_gui = App(root)
root.mainloop()