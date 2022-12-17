from PySimpleGUI import PySimpleGUI as sg

sg.theme('DarkBlue3')
class Banco:
    def __init__(self) -> None:
        pass
    #login
    layout = [
        [sg.Button('Login')],
        [sg.Button('Cadastra-se')]
    ]
