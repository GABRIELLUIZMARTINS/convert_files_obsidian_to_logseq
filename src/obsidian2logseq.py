import os
import json
import shutil

class Constants:
    """
    Class to extract constants from JSON file.
    
    """
    def __init__(self,):
        self.file_path = 'src/config.json'
        self.dados = self._load_data()

    def _load_data(self):
        try:
            with open(self.file_path, 'r') as arquivo:
                return json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading JSON file: {e}")
            return {}
    def get_constants(self):
        return self.dados.get('constantes')
    def get_path(self):
        return self.dados.get('path_project')[0]



class obsidian_to_logseq:
    """ Format Obsidian files to Logseq

    Args:
        obsidian_files (str): Path to obsidian files.
    """
    def __init__(self,obsidian_files = None):
        
        self.obsidian_files = obsidian_files
        conts = Constants()
        self.CONTANTS = conts.get_constants()
        
    # Extract the file name from the following pattern "![[file_name.extension|size]]" or "![[file_name.extension]]"
    def _separete_file_name_extension(self,old_text):
        half = '.'
        start_cut = '[['
        end_cut = ']]'
        or_end_cut = '|'

        text = old_text.split(start_cut)[1]
        text = text.split(end_cut)[0]

        #Extract file name
        file_name = text.split(half)[0]

        #Extract extension name
        extension = text.split(half)[1]
        extension = extension.split(or_end_cut)[0] if or_end_cut in extension else extension

        return file_name,extension
    
    # Finds the file path 
    def _find_file_path(self,file_name,extension):
        for root, _, files in os.walk(self.obsidian_files):
            for file in files:
                if file.endswith(extension) and (file == f"{file_name}.{extension}"):
                    return root

    def _copy_files(self,folder_files):
        folder_files = os.path.normpath(folder_files)
        folder_files = folder_files.replace("/", "\\")
        
        # Path to 'assets' folder
        pasta_assets = os.path.join(os.path.dirname(folder_files), 'assets')
        
        # Check if the 'assets' folder exists, if not, create it
        if not os.path.exists(pasta_assets):
            os.makedirs(pasta_assets)
            print(f"Pasta 'assets' criada em: {pasta_assets}")
        else:
            print(f"Pasta 'assets' já existe em: {pasta_assets}")

        # Copy all files from folder_files to the 'assets' folder
        for item in os.listdir(folder_files):
            origem = os.path.join(folder_files, item)
            destino = os.path.join(pasta_assets, item)

            # If it is a file, copy it to 'assets'
            if os.path.isfile(origem):
                try:
                    shutil.copy2(origem, destino)
                    print(f"File {origem} sucessfully copied to {destino}.")
                    #successfully copied to
                except PermissionError:
                    print(f"Errro: The file {origem} is already being used by another process.")
            else:
                print(f"{item} it is not a file, igonoring")
                
    def set_path_obsidian_files(self,obsidian_files):
        self.obsidian_files = obsidian_files

    # Rename files to logseq format
    def _rename(self,old_text):  
        # Case it is a file
        if not "![[" in old_text :
            return  old_text
        # If don't have files to convert
        self.flag_empty = False
    
        #Extract file name and extension
        file_name,extension = self._separete_file_name_extension(old_text)
        file_path =  self._find_file_path(file_name,extension)

        self._copy_files(file_path)
        if(extension == "png" or extension == "jpg"):
            #file_folder = os.path.basename(file_path)
            new_text = f'![{file_name}](../assets/{file_name}.{extension}){{:height 500, :width 500}}'
            print(f"New text: {new_text}")
            return new_text
        for ext in self.CONTANTS:
            if extension == ext:
                #file_folder = os.path.basename(file_path)
                file_path =  self._find_file_path(file_name,extension)
                new_text = f'![{file_name}](../assets/{file_name}.{extension})'
                print(f"New text: {new_text}")
                return new_text
        return old_text

    # Convert obsidian 
    def convert_files(self,obsidian_files):
        self.set_path_obsidian_files(obsidian_files)
        self.flag_empty = True
        # Finds the files .md
        for root, _, files in os.walk(self.obsidian_files):
            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    # Open files .md
                    with open(file_path, 'r+', encoding='utf-8') as f:
                        lines = f.readlines()
                        f.seek(0)
                        for line in lines:
                            new_line = ""
                            # Checks if have someone of extension from de config.json
                            for conts in self.CONTANTS:
                                new_line = self._rename(line) if (conts in line) else new_line
                            '''if new_line == "":
                                new_line = line
                            else:'''
                            new_line = line if new_line == "" else new_line 
                            f.write(new_line)
                        f.truncate()
        return self.flag_empty 

