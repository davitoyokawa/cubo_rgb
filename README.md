# Visualizador de Faces do Cubo RGB

Este é um projeto desenvolvido como parte da disciplina de Processamento Digital de Imagens (PDI) da Universidade Estadual de Maringá (UEM). O programa permite visualizar faces coloridas de um cubo simulado em 3D, onde cada face é pintada com cores RGB variáveis.

## Funcionalidades

- **Gerar Fatia de Face**: Gera uma fatia de uma face específica do cubo RGB com base no valor de um parâmetro \( i \).
  
- **Mostrar Intervalo de Faces**: Mostra um intervalo de fatias de todas as faces do cubo RGB para um intervalo de valores \( i \).

- **Interface Gráfica Interativa**: Uma GUI foi desenvolvida usando Tkinter para facilitar a interação com o programa, permitindo escolher opções, valores de \( i \), e visualizar as fatias das faces.

OBS: A visualização das faces do cubo foi baseada no cube 3D de Thiago Amendola em "https://openprocessing.org/sketch/744896/" 
Em que a primeira face é a Direita, a segunda face é a esquerda, a terceira face é em cima, a quarta face é embaixo, a quinta face é a da frente e a sexta face é a de trás.

## Pré-requisitos

- Python 3.x
- Bibliotecas necessárias: `numpy`, `opencv-python`

## Como Usar

1. **Instalação das Dependências**

   Instale as bibliotecas necessárias utilizando pip: pip install requirements.txt

2. **Executar o Programa**

Execute o script `main.py`:

3. **Interface Gráfica**

- Escolha uma opção entre "Face específica" ou "Todas as faces".
- Preencha o valor inicial de \( i \) (0-255).
- Se selecionado, preencha também o valor final de \( i \) e o passo de incremento.
- Para a opção "Face específica", informe o número da face (1-6).
- Clique no botão "Mostrar Face(s)" para visualizar as fatias das faces selecionadas.
- Se a opção "Todas as faces" estiver selecionada, só é possível inserir o Valor Inicial.

## Exemplos de Uso

-Para visualizar a face 6 do cubo com i = 150:
Opção Face específica
Valor inicial de i: 150
Face: 6
Resto: -

![image](https://github.com/davitoyokawa/cubo_rgb/assets/109833260/55ce4a8e-8ffb-41be-bdfd-1d39b37fb6df)

- Para visualizar a face 1 do cubo com valores de \( i \) de 0 a 200:
Opção: Face específica
Valor inicial de i: 0
Valor final de i: 200
Passo: 25
Face: 1

![image](https://github.com/davitoyokawa/cubo_rgb/assets/109833260/7469a0a1-0eaf-4c89-961f-356dbd77844e)

- Para visualizar as faces do cubo com valores de i = 0:
Opção: Todas as faces
Valor inicial de i: 0
Valor final de i: -
Passo: -

![image](https://github.com/davitoyokawa/cubo_rgb/assets/109833260/e74034d7-9b07-4eef-94aa-512aba23d47c)




