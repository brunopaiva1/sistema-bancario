from PySimpleGUI import PySimpleGUI as sg

sg.theme('DarkBlue3')
class Banco:
    def __init__(self) -> None:
        pass
    #layout
    layout = [
        [sg.Button('Login')], #botão para login
        [sg.Button('Cadastra-se')] #botão para cadastra-se
    ]
