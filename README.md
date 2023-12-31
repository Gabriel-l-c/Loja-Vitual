﻿# Loja-Vitual
Descrição
O trabalho consiste em criar uma loja virtual em que pessoas podem comprar itens usando
programação orientada a objetos em Python. Os usuários do sistema podem gerenciam os
produtos vendidos, realizar compras e ver relatórios. Devem ser criadas as seguintes classes de
domínio:
Pessoa
• Atributos:
o Nome: str
o Email: str
o Cpf: str
• Métodos:
o Construtor
Produto
• Atributos:
o Nome: str
o Código: str
o Preco: float (privado; > 0)
o Quantidade em estoque: int (inicialmente 0; privado; >= 0)
o Desconto percentual: float (inicialmente 0, privado; >= 0 e < 1)
o Categoria: str
• Métodos:
o construtor que receba como argumentos o nome, o código, o preço e a categoria
do produto. Os demais campos devem ser inicializados com valores padrão.
o preco: retorna o preco aplicando o desconto percetual.
Descrição
O trabalho consiste em criar uma loja virtual em que pessoas podem comprar itens usando
programação orientada a objetos em Python. Os usuários do sistema podem gerenciam os
produtos vendidos, realizar compras e ver relatórios. Devem ser criadas as seguintes classes de
domínio:
Pessoa
• Atributos:
o Nome: str
o Email: str
o Cpf: str
• Métodos:
o Construtor
Produto
• Atributos:
o Nome: str
o Código: str
o Preco: float (privado; > 0)
o Quantidade em estoque: int (inicialmente 0; privado; >= 0)
o Desconto percentual: float (inicialmente 0, privado; >= 0 e < 1)
o Categoria: str
• Métodos:
o construtor que receba como argumentos o nome, o código, o preço e a categoria
do produto. Os demais campos devem ser inicializados com valores padrão.
o preco: retorna o preco aplicando o desconto percetual.
o Construtor. Não recebe nenhum argumento e inicializa os atributos com seus
valores padrão.
o Iniciar compra: cria um objeto do tipo Compra e o define como a compra aberta. Se
uma compra aberta já existir, exiba uma mensagem de erro informando que a
pessoa deve finalizar ou cancelar a compra antes de criar uma nova.
o Buscar produto: recebe como entrada o código do produto, busca o objeto na lista
de produtos e retorna o objeto. Se ele não existir, retorne None.
o Cancelar compra: define a compra aberta como None.
o Finalizar compra: adiciona a compra na lista de compras finalizadas e define a
compra aberta como None. Em um sistema real, neste ponto, o usuário deveria
realizar o pagamento e definir o endereço de entrega, mas não faremos isso. Por
fim, para cada item na compra, desconte a quantidade comprada da quantidade em
estoque do produto.
As operações de inserir, atualizar e remover produtos da compra em andamento
podem ser feitas usando diretamente os métodos da classe Compra existentes no
atributo “Compra aberta”.
o Métodos de Relatório (métodos normais da classe Loja):
▪ Número de produtos: retorna o número de produtos vendidos na loja.
▪ Número de vendas: retorna o número de compras concluídas.
▪ Valor total vendido: retorna a soma dos valores totais das compras
concluídas.
▪ Valor médio das compras: retorna o valor total médio das compras
concluídas.
▪ Número de usuários: retorna o número de pessoas diferentes que já fizeram
compras na loja.
▪ Usuário que mais fez compras: retorna um objeto do tipo Pessoa
representando a pessoa que mais finalizou compras na loja.
▪ 5 produtos mais caros: Retorne uma lista contendo os 5 produtos mais caros
da loja. Não é válido mostrar os dados na tela diretamente no método. O
método deve funcionar mesmo se existirem menos de 5 produtos
cadastrados. Neste caso, devem ser retornados todos os produtos
cadastrados.
▪ 5 produtos mais vendidos e o valor total que a loja recebeu com as vendas
do produto. O método pode exibir os dados diretamente e não é necessário
retorná-los como, por exemplo, uma lista. Os dados devem ser exibidos de
forma ordenada, do produto que levou ao maior montante para o que levou
para o menor. O método deve funcionar mesmo se existirem menos de 5
produtos cadastrados. Neste caso, devem ser exibidos todos os produtos
cadastrados.
▪ Para cada pessoa, some o valor total das compras feitas pela pessoa. Mostre
na tela os nomes das pessoas e seguido pelo CPF e o valor total das compras.
Os dados devem ser ordenados pelo nome da pessoa (ordem alfabética).
Não é necessário retornar os dados como uma lista.
o Salvar: Salva os dados de produtos e compras de forma que as informações
persistam mesmo que o programa seja encerrado. A compra aberta não deve ser
salva.
o Carregar: Lê os dados de produtos e compras do arquivo e usa estas informações
para preencher as respectivas listas.
App
• Atributos
o loja: objeto do tipo loja
• Métodos
o Construtor: Não deve receber argumentos e deve inicializar o atributo loja com um
novo objeto do tipo Loja.
o Menu: deve exibir um menu com as opções listadas na próxima seção e retornar a
opção escolhida pelo usuário.
o Executar: deve repetidamente mostrar o menu para o usuário e realizar a opção
escolhida até que seja selecionada a opção de sair.
Opções do Menu
1. Cadastrar produto: Solicite que o usuário digite os dados do produto, cria um objeto do tipo
Produto e o adiciona na lista de produtos da loja.
2. Ver lista de produtos: Mostra na tela o código, o nome e o valor (com desconto) de todos os
produtos da loja, um por linha. Para cada produto, deve ser exibido o índice do produto na
lista.
3. Ver detalhes de produto: Solicita que o usuário digite o código de um produto e mostre
todas as suas informações, incluindo o valor de desconto e o valor bruto (sem desconto).
4. Atualizar desconto de produto: Solicita que o usuário digite o código de um produto e um
novo valor de desconto e atualiza o desconto do produto.
5. Registrar aquisição de produto: Solicita que o usuário digite o código de um produto e a
quantidade comprada junto ao fornecedor e incrementa a quantidade em estoque do
produto.
6. Remover produto: Solicita que o usuário digite o código de um produto e remove o produto
da lista.
7. Iniciar compra: Ao iniciar a compra, solicite que o usuário digite os dados do cliente que está
fazendo a compra. Use estes dados para criar um objeto do tipo Pessoa que será passado
para o construtor da nova Compra.
8. Cancelar compra
9. Finalizar compra
10. Adicionar item na compra: Solicita que o usuário digite o código do produto e a quantidade
sendo comprada e adiciona o item na compra. Se o produto já existir compra, deve ser
exibida uma mensagem de erro e ele não deve ser adicionado novamente.
11. Visualizar compra
12. Remover item da compra: Solicita que o usuário digite o índice do item na lista da compra e
remove o respectivo item.
13. Atualizar quantidade de item na compra: Solicita que o usuário digite o índice do item na
lista da compra e a nova quantidade e atualiza o item.
14. Relatório - Número de produtos.
15. Relatório - Número de vendas.
16. Relatório - Valor total vendido.
17. Relatório - Valor médio das compras.
18. Relatório - Número de usuários.
19. Relatório - Usuário que mais fez compras.
20. Relatório - 5 produtos mais caros.
21. Relatório - 5 produtos mais vendidos.
22. Relatório – Montante por pessoa. 
