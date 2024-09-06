from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk  # Importando PIL

from obsidian2logseq import *
import os

class Root(Tk):
    def __init__(self):
        super().__init__()
        # Init object convert
        self.obj_convert = obsidian_to_logseq()

        self.title("Conversor de arquivos - Obsidian para Logseq")
        self.geometry("900x390")
        self.pasta_selecionada = ''
        # Definir a cor de fundo da janela como preto
        self.configure(bg="black")

        #---------------------------------------------------------------------------
        # Definindo as configurações das colunas
        self.columnconfigure(0, weight=0)  # Coluna do Botão 1 e Botão 2 não expande
        self.columnconfigure(1, weight=1)  # Coluna do Caminho/do/arquivo expande

        # Título (centralizado)
        self.label_title = Label(self, text= "Instruções",font = ("Arial Bold", 20),fg='#88c7cc', bg='black', borderwidth=2, relief="solid", padx=10, pady=10)
        self.label_title.grid(row=0, column=0, columnspan=2, sticky="nsew")  # Centralizado

        # Instruções de uso (alinhado à esquerda)
        self.label_instructions = Label(self, relief="solid",
                                        text="Para converter um projeto Obsidian para Logseq, selecione o local que está seu projeto Obsidian e após clique em Converter.", 
                                        borderwidth=2,  
                                        padx=10, pady=10, 
                                        anchor="w",
                                        font = ("Arial Bold", 10),
                                        fg='#88c7cc', 
                                        bg='black'
                                        )
        self.label_instructions.grid(row=1, column=0, columnspan=2, sticky="nsew")  # Alinhado à esquerda

        # Botão 1 (tamanho fixo)
        botao_selecionar = Button(self, text="Selecionar Pasta", 
                                  command = self._selecionar_pasta,
                                  relief="solid", 
                                  borderwidth=2,  
                                  width=15, 
                                  height=2,
                                  font = ("Arial Bold", 10),
                                  fg='#012d32', 
                                  bg='#88c7cc'
                                  )  # Tamanho fixo
        botao_selecionar.grid(row=2, column=0, padx=5, pady=5)

        # (Alinhado à esquerda)
        self.label = Label(self, textvariable= self.pasta_selecionada, 
                           borderwidth=2, 
                           padx=10, pady=10, 
                           anchor="w",
                           font = ("Arial Bold", 10),
                           fg='#88c7cc', 
                           bg='black')
        self.label.grid(row=2, column=1, sticky="nsew")

        # Botão 2 (tamanho fixo, igual ao Botão 1)
        botao_converter = Button(self, text="Converter", 
                                 command=self._converter,
                                 borderwidth=2, 
                                 relief="solid", 
                                 width=15, height=2,
                                 font = ("Arial Bold", 10),
                                 fg='#012d32', 
                                 bg='#88c7cc')  # Tamanho fixo
        botao_converter.grid(row=3, column=0, padx=5, pady=5)

        # Preenchendo a coluna da linha de Botão 2 para alinhar à esquerda
        botao_converter_placeholder = Label(self, text="", 
                                            borderwidth=2,
                                            bg='black')
        botao_converter_placeholder.grid(row=3, column=1, sticky="nsew")  # Placeholder para alinhar

        # Definindo o mesmo tamanho para as linhas
        for i in range(4):
            self.rowconfigure(i, weight=1)

        # Definir o caminho da imagem usando caminho relativo
        image_path = os.path.join(os.path.dirname(__file__), '../assets/obs2log.png')

        # Carregar a imagem com PIL, redimensionar e converter para PhotoImage
        original_image = Image.open(image_path)
        
        # Redimensionar a imagem (defina a largura e altura desejadas)
        resized_image = original_image.resize((387, 232), Image.LANCZOS)  # Aqui, 100x100 é o novo tamanho #(1550, 928)

        # Converter a imagem redimensionada para um formato compatível com tkinter
        self.photo = ImageTk.PhotoImage(resized_image)

        # Criar o Label com a imagem
        image_label = ttk.Label(
            self,
            image=self.photo,  # Referência à imagem
            compound='top',
            background="black"
        )
        # Adiciona a imagem na posição row=4, column=0
        #image_label.grid(row=4, column=0, columnspan=2, sticky="nsew")
        image_label.grid(row=4, column=0, columnspan=2, sticky="n")

        #---------------------------------------------------------------------------

    def _selecionar_pasta(self):
        # Abre o diálogo de seleção de diretório
        self.pasta_selecionada = filedialog.askdirectory()
        self.label['text'] = self.pasta_selecionada

        # Exibe a pasta selecionada em um popup e no console
        if self.pasta_selecionada:
            print(f"Pasta selecionada: {self.pasta_selecionada}")

    def _converter(self):
         # Exibe a pasta selecionada em um popup e no console
        if self.pasta_selecionada:
            #Convert files
            empty = self.obj_convert.convert_files(self.pasta_selecionada)
            print(f"Arquivo vazio? {empty}")    
            if empty :
                messagebox.showinfo("_converter", f"Não há arquivos para serem convertidos ou já foram convertidos.")
            else:
                messagebox.showinfo("_converter", f"Arquivos convertidos.")
            print(f"Pasta selecionada: {self.pasta_selecionada}")
if __name__ == "__main__":
    root = Root()
    root.mainloop()


"""
class Root(Tk):
    def __init__(self, tasks = None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        self.title("Convert Files")
        self.geometry("300x400")

        label = Label(self, text = "Add your path:", bg = "lightgrey", fg = "white", padx=5, pady=5)
        self.tasks.append(label)

        for task in self.tasks:
            task.pack(side=TOP, fill=X)

        self.task_create = Text(self, height=3, bg="white",fg="white")

        self.task_create.pack(side=BOTTOM, fill=X)

        self.bind("<Return>", self.add_task)
        self.colour_schemes = [{"bg":"lightgrey", "fg": "white"},{"bg":"grey","fg":"white"}]
    def add_task(self, event=None):
        task_text = self.task_create.get(1.0,TOP).strip()
if __name__ == "__main__":
    root = Root()
    root.mainloop()
"""
