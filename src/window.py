from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk  

from obsidian2logseq import *
import os

class Window(Tk):
    def __init__(self):
        super().__init__()

        # Init object convert
        self.obj_convert = obsidian_to_logseq()

        # Window configuration
        self.title("Conversor de arquivos - Obsidian para Logseq")
        self.geometry("900x390")
        self.pasta_selecionada = ''
        
        # Define the background color of the window as black
        self.configure(bg="black")


        # Setting up column configurations
        self.columnconfigure(0, weight=0)  # The column of buttons does not expand 
        self.columnconfigure(1, weight=1)  # The file path column expands

        # Title (Centered)
        self.label_title = Label(self, text= "Instruções",font = ("Arial Bold", 20),fg='#88c7cc', bg='black', borderwidth=2, relief="solid", padx=10, pady=10)
        self.label_title.grid(row=0, column=0, columnspan=2, sticky="nsew")

        # Usage instructions 
        self.label_instructions = Label(self, relief="solid",
                                        text="Para converter um projeto Obsidian para Logseq, selecione o local que está seu projeto Obsidian e após clique em Converter.", 
                                        borderwidth=2,  
                                        padx=10, pady=10, 
                                        anchor="w",
                                        font = ("Arial Bold", 10),
                                        fg='#88c7cc', 
                                        bg='black'
                                        )
        self.label_instructions.grid(row=1, column=0, columnspan=2, sticky="nsew")  

        # Bottun 1 (Fixed size)
        botao_selecionar = Button(self, text="Selecionar Pasta", 
                                  command = self._selecionar_pasta,
                                  relief="solid", 
                                  borderwidth=2,  
                                  width=15, 
                                  height=2,
                                  font = ("Arial Bold", 10),
                                  fg='#012d32', 
                                  bg='#88c7cc'
                                  )  
        botao_selecionar.grid(row=2, column=0, padx=5, pady=5)

        #Path of the selected folder
        self.label = Label(self, textvariable= self.pasta_selecionada, 
                           borderwidth=2, 
                           padx=10, pady=10, 
                           anchor="w",
                           font = ("Arial Bold", 10),
                           fg='#88c7cc', 
                           bg='black')
        self.label.grid(row=2, column=1, sticky="nsew")

        # Bottun 2 (Fixed size)
        botao_converter = Button(self, text="Converter", 
                                 command=self._converter,
                                 borderwidth=2, 
                                 relief="solid", 
                                 width=15, height=2,
                                 font = ("Arial Bold", 10),
                                 fg='#012d32', 
                                 bg='#88c7cc')  # Tamanho fixo
        botao_converter.grid(row=3, column=0, padx=5, pady=5)

        # Filling the column of bottun 2 row to align left
        botao_converter_placeholder = Label(self, text="", 
                                            borderwidth=2,
                                            bg='black')
        botao_converter_placeholder.grid(row=3, column=1, sticky="nsew") 

        # Defining the same size for the rows
        for i in range(4):
            self.rowconfigure(i, weight=1)


        #---------------------------------------------------------------------------

        # Set the image path using a relative path
        image_path = os.path.join(os.path.dirname(__file__), '../assets/obs2log.png')

        # Load the image with PIL, resize it and convert it to PhotoImage 
        original_image = Image.open(image_path)
        
        # Resize the image (set the desired width and height) 
        resized_image = original_image.resize((387, 232), Image.LANCZOS) 

        # Convert the resized image to a tkinter compatible format
        self.photo = ImageTk.PhotoImage(resized_image)

        # Create the label with the image
        image_label = ttk.Label(
            self,
            image=self.photo,  # Image reference
            compound='top',
            background="black"
        )
        image_label.grid(row=4, column=0, columnspan=2, sticky="n")

        #---------------------------------------------------------------------------

    def _selecionar_pasta(self):
        # Open the directory selection dialog
        self.pasta_selecionada = filedialog.askdirectory()
        self.label['text'] = self.pasta_selecionada

        # Shows the selected folder in a popup window and the console
        if self.pasta_selecionada:
            print(f"Pasta selecionada: {self.pasta_selecionada}")

    def _converter(self):
        if self.pasta_selecionada:
            #Convert files
            empty = self.obj_convert.convert_files(self.pasta_selecionada)
            print(f"Empty file? {empty}")    
            if empty :
                messagebox.showinfo("_converter", f"Não há arquivos para serem convertidos ou já foram convertidos.")
            else:
                messagebox.showinfo("_converter", f"Arquivos convertidos.")
            print(f"Pasta selecionada: {self.pasta_selecionada}")