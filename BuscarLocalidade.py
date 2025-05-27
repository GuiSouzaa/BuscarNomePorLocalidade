import pandas as pd

def buscar_localidade():
    df = pd.read_excel('Planilha/PlanilhaLocalidade.xlsx')

    while True:
        inputLocalidade = input('Insira a localidade ou para encerrar digite "sair":').strip()
        if inputLocalidade.lower() == 'sair':
            print('Encerrando...')
            break

        # A variavel a baixo recebe o meu input acima
        LocalidadeEncontrada = df[df['Localidade'] == inputLocalidade]
        #Colocar em um for para iterar sobre o meu df
        if not LocalidadeEncontrada.empty:
            for nome in LocalidadeEncontrada['Nome']: # Vai buscar o nome segundo a localidade
                print(nome)
        else:# Saidas para tentar exibir os nomes disponiveis
            print('nenhum nome foi encontrado')
            Localizar = input('deseja que eu liste todos os locais e nomes disponives no Df? s/n: ')
            if Localizar == 's':
                print(df[['Nome', 'Localidade']])
        
