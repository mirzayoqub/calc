import pyttsx3


class Neuron:
    def __init__(self, name):
        self.__name = name
        self.robot = pyttsx3.init()

    def says(self):
        self.robot.say(f'hello {self.__name}' + 'can i you help something')

        self.robot.runAndWait()

    def how(self, answer):
        self.robot.say(answer)
        self.robot.runAndWait()








