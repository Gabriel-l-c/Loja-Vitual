class Produto:
    def __init__(self, nome:str , codigo:str, preco: float,  categoria:str):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.categoria = categoria
        self.quant_estoque = 0
        self.desconto_percentual = 0.0
        
    def dump_produto(self):
        return (self.nome, self.codigo, self.preco, self.categoria, self.quant_estoque, self.desconto_percentual)

    @staticmethod
    def load_produto(nome, codigo, preco, categoria, quant_estoque, desconto_percentual):
        produto = Produto(nome, codigo, preco, categoria)
        produto.quant_estoque =quant_estoque
        produto.desconto_percentual =desconto_percentual
        return produto
       
    def Preco(self):
        return float(self.preco) * float((1.0-float(self.desconto_percentual)))
   
    def Registrar_aquisicao(self, quant_estoque:int ):
        self.quant_estoque += quant_estoque
    
    def Registrar_venda(self, quant_comprada:int):
        if self.quant_estoque - quant_comprada >=0:
         self.quant_estoque -= quant_comprada
        else:
            print("Erro na computação, estoque negativo?")
    
    def Quantidade_em_estoque(self):
        produtos_em_estoque = self.quant_estoque
        return produtos_em_estoque
    
    def Atualizar_desconto(self, new_desconto:float):
        if new_desconto >=0.0 and new_desconto<1.0:
         self.desconto_percentual = new_desconto
        else:
            print("erro, desconto invalido")
            return 0
        
    def Atualizar_preco(self, new_preco):
        if new_preco >0 :
         self.preco = new_preco
        else:
            print("erro, valor invalido")
            return 0 
    
"""     def return_preco():
       preco = self.preco
       return preco """