class carro():
    #classe para um carro
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.odometro = 0

    def nome_descritivo(self):
        nome_longo = str(self.ano)+' '+self.marca+' '+self.modelo
        return nome_longo.upper()
     
    def ler_km(self):
     #Imprima uma declaração mostrando a quilometragem do carro.
        print('\nEsse carro rodou: '+str(self.odometro)+' km')
        
     #Defina a leitura do odômetro         
    def atualizar_odometro(self,quilometros):
        #Rejeite a alteração
        if quilometros >= self.odometro:
            self.odometro = quilometros
        else:
            print('você não pode reverter o odômetro ')
            #incremetro
    def incremento_odo(self,miles):
        self.odometro += miles
        
        #Herança <==>
class carro_eletrico(carro):
#Representa os aspectos de um carro, específico para veículos elétricos.
    def __init__(self,marca,modelo,ano):
    #Inicializar atributos da classe pai.
        super().__init__(marca, modelo,ano)
        
minha_tesla = carro_eletrico('tesla','modelos',2017)
print(minha_tesla.nome_descritivo())
        
        
    
    