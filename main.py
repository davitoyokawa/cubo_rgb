import numpy as np
import cv2 as cv
import tkinter as tk
from math import ceil, sqrt
from tkinter import messagebox, ttk

# Definindo a cor de fundo
background_color = "#C0FFEE"

def gerar_fatia(face, i):
    size = 256
    cubo = np.zeros((size, size, 3), dtype=np.uint8)

    if face == 1:
        cima = np.linspace([255, 0, 255], [255, 255, 255], size)
        baixo = np.linspace([255, 0, 0], [255, 255, 0], size)
        cubo = np.linspace(cima, baixo, size).astype(np.uint8)
        cubo[:, :, 0] = 255 - i
    elif face == 2:
        cima = np.linspace([0, 255, 255], [0, 0, 255], size)
        baixo = np.linspace([0, 255, 0], [0, 0, 0], size)
        cubo = np.linspace(cima, baixo, size).astype(np.uint8)
        cubo[:, :, 0] = i
    elif face == 3:
        cima = np.linspace([255, 255, 255], [0, 255, 255], size)
        baixo = np.linspace([255, 255, 0], [0, 255, 0], size)
        cubo = np.linspace(cima, baixo, size).astype(np.uint8)
        cubo[:, :, 1] = 255 - i
    elif face == 4:
        cima = np.linspace([0, 0, 255], [255, 0, 255], size)
        baixo = np.linspace([0, 0, 0], [255, 0, 0], size)
        cubo = np.linspace(cima, baixo, size).astype(np.uint8)
        cubo[:, :, 1] = i
    elif face == 5:
        cima = np.linspace([255, 0, 0], [255, 255, 0], size)
        baixo = np.linspace([0, 0, 0], [0, 255, 0], size)
        cubo = np.linspace(cima, baixo, size).astype(np.uint8)
        cubo[:, :, 2] = i
    elif face == 6:
        cima = np.linspace([0, 0, 255], [0, 255, 255], size)
        baixo = np.linspace([255, 0, 255], [255, 255, 255], size)
        cubo = np.linspace(cima, baixo, size).astype(np.uint8)
        cubo[:, :, 2] = 255 - i

    # Trocar superior esquerdo com inferior direito e Rotacionar 180 graus para melhor visualização
    cubo[:, :, 0] = cubo[:, :, 0].T
    cubo[:, :, 1] = cubo[:, :, 1].T
    cubo[:, :, 2] = cubo[:, :, 2].T
    cubo = cv.rotate(cubo, cv.ROTATE_180)

    return cubo

def mostrar_intervalo_faces(i_start, i_end, opcao, passo, face=None):
    images = []
    for i in range(i_start, i_end + 1, passo):
        if opcao == 1 and face:
            images.append(gerar_fatia(face, i))
        elif opcao == 2:
            for f in range(1, 7):
                images.append(gerar_fatia(f, i))

    num_images = len(images)
    cols = ceil(sqrt(num_images))
    rows = ceil(num_images / cols)

    # Preencher a grade de imagens
    grid = []
    for r in range(rows):
        row_images = []
        for c in range(cols):
            idx = r * cols + c
            if idx < num_images:
                row_images.append(images[idx])
            else:
                row_images.append(np.zeros_like(images[0]))  # Preencher com imagens vazias
        grid.append(np.hstack(row_images))
    final_image = np.vstack(grid)

    cv.imshow(f"Intervalo de i: {i_start} - {i_end} com passo {passo}", final_image)
    cv.waitKey(0)
    cv.destroyAllWindows()

def mostrar_interface_grafica():
    def toggle_intervalo():
        opcao = int(opcao_var.get())
        state = tk.NORMAL if intervalo_var.get() and opcao == 1 else tk.DISABLED
        valor_i_end_label.config(state=state)
        valor_i_end_entry.config(state=state)
        passo_label.config(state=state)
        passo_entry.config(state=state)
        face_label.config(state=tk.NORMAL if opcao == 1 else tk.DISABLED)
        face_entry.config(state=tk.NORMAL if opcao == 1 else tk.DISABLED)
        intervalo_check.config(state=tk.NORMAL if opcao == 1 else tk.DISABLED)

    def mostrar_resultado():
        try:
            opcao = int(opcao_var.get())
            
            # Verificar se os campos estão vazios
            if valor_i_start_entry.get() == "":
                raise ValueError("Por favor, preencha o valor inicial de i.")
            
            i_start = int(valor_i_start_entry.get())
            if i_start < 0 or i_start > 255:
                raise ValueError("Valor de i deve estar entre 0 e 255.")

            if intervalo_var.get() and opcao == 1:
                if valor_i_end_entry.get() == "":
                    raise ValueError("Por favor, preencha o valor final de i.")
                i_end = int(valor_i_end_entry.get())
                if i_end < 0 or i_end > 255 or i_end < i_start:
                    raise ValueError("Valor final de i deve estar entre 0 e 255 e maior ou igual ao valor inicial.")
                if passo_entry.get() == "":
                    raise ValueError("Por favor, preencha o campo Passo.")
                passo = int(passo_entry.get())
                if passo <= 0:
                    raise ValueError("Passo deve ser maior que 0.")
            else:
                i_end = i_start
                passo = 1

            if opcao == 1:
                if face_entry.get() == "":
                    raise ValueError("Por favor, escolha uma face (1-6).")
                face = int(face_entry.get())
                if face < 1 or face > 6:
                    raise ValueError("Escolha uma face válida (1-6).")
                mostrar_intervalo_faces(i_start, i_end, opcao, passo, face)
            elif opcao == 2:
                mostrar_intervalo_faces(i_start, i_end, opcao, passo)
            else:
                messagebox.showerror("Opção Inválida", "Escolha uma opção válida (1 ou 2).")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    # Configuração da janela principal
    root = tk.Tk()
    root.title("Visualizador de Faces do Cubo RGB")
    root.geometry("400x400")
    root.configure(bg=background_color)

    # Frame para a opção
    frame_opcao = tk.Frame(root, bg=background_color)
    frame_opcao.pack(pady=10)

    opcao_label = tk.Label(frame_opcao, text="Escolha uma opção:", bg=background_color)
    opcao_label.pack(anchor=tk.W)

    Toolbutton = ttk.Style()
    Toolbutton.configure("Toolbutton", padding=5, background="white")

    opcao_var = tk.StringVar(value="1")
    opcao_radio1 = ttk.Radiobutton(frame_opcao, text="Face específica", variable=opcao_var, value="1", command=toggle_intervalo,
                                    style="Toolbutton", width=13)
    opcao_radio1.pack(anchor=tk.W)
    opcao_radio2 = ttk.Radiobutton(frame_opcao, text="Todas as faces", variable=opcao_var, value="2", command=toggle_intervalo,
                                    style="Toolbutton", width=13)
    opcao_radio2.pack(anchor=tk.W)

    # Frame para a face e o valor i
    frame_face = tk.Frame(root, bg=background_color)
    frame_face.pack(pady=10)

    face_label = tk.Label(frame_face, text="Face (1-6):", bg=background_color)
    face_label.grid(row=0, column=0, sticky=tk.W, pady=5)
    face_entry = ttk.Entry(frame_face)
    face_entry.grid(row=0, column=1, pady=5)

    valor_i_start_label = tk.Label(frame_face, text="Valor inicial de i (0-255):", bg=background_color)
    valor_i_start_label.grid(row=1, column=0, sticky=tk.W, pady=5)
    valor_i_start_entry = ttk.Entry(frame_face)
    valor_i_start_entry.grid(row=1, column=1, pady=5)

    valor_i_end_label = tk.Label(frame_face, text="Valor final de i (0-255): ", bg=background_color)
    valor_i_end_label.grid(row=2, column=0, sticky=tk.W, pady=5)
    valor_i_end_entry = ttk.Entry(frame_face, state=tk.DISABLED)
    valor_i_end_entry.grid(row=2, column=1, pady=5)

    # Frame para o intervalo
    frame_intervalo = tk.Frame(root, bg=background_color)
    frame_intervalo.pack(pady=5)

    intervalo_var = tk.BooleanVar()
    intervalo_check = ttk.Checkbutton(frame_intervalo, text="Mostrar intervalo de i", variable=intervalo_var, command=toggle_intervalo, 
                                      style='Custom.TCheckbutton')
    intervalo_check.pack(anchor=tk.W)

    s1 = ttk.Style()
    s1.configure('Custom.TCheckbutton',
                font=('', 10),
                )

    s1.map('Custom.TCheckbutton',
          background=[('selected', background_color), ('!selected', background_color)],
          foreground=[('selected', 'black'), ('!selected', 'blue')],
          arrowcolor=[('selected', '#FFFFFF'), ('!selected', 'blue')],
          bordercolor=[('active', 'blue')],
          )

    passo_label = tk.Label(frame_intervalo, text="Passo:", bg=background_color)
    passo_label.pack(anchor=tk.W, pady=5)
    passo_entry = ttk.Entry(frame_intervalo, state=tk.DISABLED)
    passo_entry.pack(anchor=tk.W)

    # Botão para mostrar o resultado
    button = ttk.Button(root, text="Mostrar Face(s)", command=mostrar_resultado, style="Davi.TButton", width=13)
    button.pack(pady=10, anchor=tk.NW, padx=128)  

    s2 = ttk.Style()
    s2.configure('Davi.TButton', foreground='green', background='lightgreen', font=("", 12))

    root.mainloop()

if __name__ == "__main__":
    mostrar_interface_grafica()
