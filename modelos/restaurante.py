from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria): 
        self._nome = nome.title()
        self.categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{ "Nome Restaurante:".ljust(25)} | {"Categoria:".ljust(25)} | '
              f'{"Avaliação".ljust(25)} | {"Status:".ljust(25)} ')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} |'
                  f' {str(restaurante.media_avaliacao).ljust(25)} | {restaurante.ativo.ljust(25)}')
    
    def alterar_status_restaurante(self):
        self._ativo = not self._ativo
    
    @property
    def ativo(self):
        return 'Ativado' if self._ativo else 'Desativado'
    
    
    @property
    def media_avaliacao(self):
       if not self._avaliacao:
           return 0 
       soma_das_nota = sum(avaliacao._nota for avaliacao in self._avaliacao)
       quantidade_de_notas = len(self._avaliacao)
       media = round(soma_das_nota/quantidade_de_notas)
       return media
    
    def avaliar_restaurante(self, cliente, nota):
        if nota > 5 or nota < 0:
            while nota > 5:
                nota = int(input('Nota não pode ser maior que 5, avalie novamente:'))
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        else:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
    
    @property
    def imprimir_cardapio(self):
        print(f'Cardápio do {self._nome}:\n')
        for i, item in enumerate(self._cardapio, start = 1):
            if hasattr(item, 'descricao'):
                mensagem = f'{i} Produto: {item._nome.ljust(25)} | Preço: {str(item._preco).ljust(25)} | Descrição: {item.descricao}'
            else:
                mensagem = f'{i} Produto: {item._nome.ljust(25)} | Preço: {str(item._preco).ljust(25)} | Tamanho: {item.tamanho}'
            print(mensagem)


    
    


