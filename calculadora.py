import PySimpleGUI as sg

class Tela:
    def __init__(self):
        #Layout
        layout = [
            [sg.Output(size=(20,0),key='output')],
            [sg.Button('7',key='7'), sg.Button('8',key='8'),sg.Button('9',key='9'),sg.Button('+',key='+')],
            [sg.Button('4',key='4'), sg.Button('5',key='5'),sg.Button('6',key='6'),sg.Button('-',key='-')],
            [sg.Button('1',key='1'), sg.Button('2',key='2'),sg.Button('3',key='3'),sg.Button('*',key='*')],
            [sg.Button('0',key='0'), sg.Button('=',key='='),sg.Button('/',key='/')]            
        ]
        #Janela

        self.janela = sg.Window('Calculadora').layout(layout)

        #Extrair dados

        self.button, self.values=self.janela.Read()

    def number_click(event):
        global vars
        if var['decimal']:
            var['back'].append(event)
        else:
            var['front'].append(event)
            update_display(fromat_number())

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()

            if self.button is None:
                break

            if self.button in ['0','1','2','3','4','5','6','7','8','9']:
                number_click(event)

            n1 = self.values['1']
            n2 = self.values['2']
            n3 = self.values['3']
            n4 = self.values['4']
            n5 = self.values['5']
            n6 = self.values['6']
            n7 = self.values['7']
            n8 = self.values['8']
            n9 = self.values['9']
            n0 = self.values['0']

            soma = self.values['+']
            sub = self.values['-']
            mult = self.values['*']
            div = self.values['/']
            

            print(self.values)
            if n1:
                number = 1
            if n2:
                number = 2
            if n3:
                number = 3
            if n4:
                number = 4
            if n5:
                number = 5
            if n6:
                number = 6
            if n7:
                number = 7
            if n8:
                number = 8
            if n9:
                number = 9
            if n0:
                number = 0
            

            if self.values['=']:
                if soma:
                    conta = number+number
                if sub:
                    conta = number-number
                if mult:
                    conta = number*number
                if div:
                    conta = number/number
                print(conta)

tela = Tela()
tela.Iniciar()