import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkBrown4')
        #Layout
        layout = [
        [sg.Text('Nome:',size=(5,0)),sg.Input(size=(15,0),key='nome')],
        [sg.Text('Idade:',size=(5,0)),sg.Input(size=(15,0),key='idade')],
        [sg.Text('Quais provedores de e-mail são aceitos?')],
        [sg.Checkbox('Gmail',key='gmail'),sg.Checkbox('Outlook',key='outlook'),sg.Checkbox('Yahoo',key='yahoo')],
        [sg.Text('Aceita Cartão')],
        [sg.Radio('Sim','cartoes',key='aceitaCartao'),sg.Radio('Não','cartoes',key='naoAceitaCartao')],
        [sg.Slider(range=(0,100),default_value=0,orientation='h',size=(15,20),key='sliderVelocidade')],
        [sg.Button('Enviar')],
        [sg.Output(size=(30,30))]
        ]
        #Janela

        self.janela = sg.Window('Dados do usuário').layout(layout)
        #Extrair dados da tela

        self.button,self.values = self.janela.Read()

    def Iniciar(self):
        while True:
            self.button,self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao_sim = self.values['aceitaCartao']
            aceita_cartao_nao = self.values['naoAceitaCartao']
            velocidade_script = self.values['sliderVelocidade']
            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'aceita gmail: {aceita_gmail}')
            print(f'aceita yahoo: {aceita_yahoo}')
            print(f'aceita_outlook: {aceita_outlook}')
            print(f'aceita cartao: {aceita_cartao_sim}')
            print(f'nao aceita cartao: {aceita_cartao_nao}')
            print(f'Velocidade Script: {velocidade_script}')

tela = TelaPython()
tela.Iniciar()
