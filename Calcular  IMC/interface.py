import PySimpleGUI as sg

class Imc_Interface:
    def __init__(self):
        
        theme = sg.theme("BlueMono")

        layout = [

            [sg.Text(      "Calcular IMC")],
            [sg.Text("Peso "), sg.Input(key="peso", size=(7,0)), sg.Text("EX: 75.0")],
            [sg.Text("Altura"), sg.Input(key="altura", size=(7,0)), sg.Text("EX: 1.73")],
            [sg.Button("Calcular")],
            [sg.Text(" ", size=(0,1), key="output")]
        
        ]

        self.window = sg.Window("Calcular IMC", layout)
    def init(self):
        while True:
            event, values = self.window.read()

            if event == sg.WINDOW_CLOSED:
                break
            if event == "Calcular":
                try:
                    self.weight = float(values["peso"])
                    self.height = float(values["altura"])

                    self.imc = self.weight // self.height**2
                    
                    self.window["output"].update(f"O seu IMC é ==> {self.imc}")
                except:
                    self.window["output"].update("Objeto não reconhecido, experimente colocar números.")
