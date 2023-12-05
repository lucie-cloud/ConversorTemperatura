# Interface gráfica com o Usuário

import PysimpleGUI as psg
import Conversor
from Conversor import cel_fahr
from Conversor import fahr_cel

layout = [
    [psg.Text('Escolha o tipo de conversão que deseja realizar: '), psg.InputText(Key='escolha==1')],
    [psg.Text('Escolha o tipo de conversão que deseja realizar: '), psg.InputText(key='escolha==2')],

    [psg.Button('Converter')],
         ]

janela = psg.Window('Conversor de Unidades: Graus Celsius e Fahrenheit', layout)
while True:
    eventos, valores = janela.read()
    if eventos==psg.WIN_CLOSED: break
    else:
        Cel = int (valores['escolha'])
        janela['Valor em Celsius']
        janela['Valor em Fahrenheit']
janela.close()