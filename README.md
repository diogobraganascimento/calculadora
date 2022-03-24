# Calculadora

> Código em Python simples para criação de um calculadora com funções simples de soma, divisão, subtração e divisão.

## Biblioteca utilizada: https://docs.python.org/3/library/tkinter.html

### Funções criadas:
* entrar_valores;
* calcular;
* limpar_tela;

### Criação da janela 
* title = Escreve um titulo na parte superior da calculadora;
* geometry = Define as dimensões da calculadora (largura X altura);
* config = Aqui foi configurado o background da calculadora;

![image](https://user-images.githubusercontent.com/64949287/159867471-a415231c-42f7-4990-9ec6-cb47f95a853d.png)

### Criação do mostrador
* Frame = Configuração do mostrador de resultado com largura, altura e cor;
* grid = Separado a calculadora em duas partes e o mostrador foi configurado em '0' para ficar na parte superior;

![image](https://user-images.githubusercontent.com/64949287/159868574-9e53b29b-bc36-4318-ab26-cbfa40e98dfc.png)

### Criação do corpo
* Frame = Como feito no mostrador, aqui também definimos o corpo da calculadora em largura e altura e a cor foi deixada padrão;
* grid = Para o corpo foi definido '1' para que fique abaixo do mostrador;

![image](https://user-images.githubusercontent.com/64949287/159869275-35af9a82-15ad-4db6-8dda-bb65a5448635.png)

### Criação do botão
Na criação dos botões é basicamente da mesma forma mudando apenas nome, tamanho e função que é chamada;
* text = define o nome;
* width = define a largura;
* height = define altura;
* bg (background) = define a cor;
* font = define a fonte, tamanho e tipo de escrita (negrito, italico, sublinhado);
* relief = define o estilo de relevo do botão;
* command = Aqui definimos qual a função o botão deve chamar;
