from PySimpleGUI import PySimpleGUI as sg

sg.theme('DarkBlue3')
class Banco:
    def __init__(self) -> None:
        pass
    #layout
layout = [
    [sg.Button('Login'), sg.Input(key='login')], #botão para login
    [sg.Button('Cadastra-se'), sg.Input(key='cadastrar')] #botão para cadastra-se
]
janela = sg.Window('Menu', layout)

