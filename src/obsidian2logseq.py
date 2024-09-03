import os
import shutil

class rename_and_copy_images:
    def __init__(self,base_directory,attachments_directory):
        
        self.base_directory = base_directory
        self.attachments_directory = attachments_directory

        self.process_markdown_files(self.base_directory)
        self.update_attachments_directory(base_directory,attachments_directory)


    def rename(self,old_text):
    
        if not old_text[3] == '[' :
            return  old_text

        #Extract extension name
        extension = old_text.split(".")[1].split("]")[0]
        extension = extension.split("|")[0] if "|" in extension else extension

        #Extract file name
        file_name = old_text.split(".")[0]
        print("file_name"+file_name)
        file_name = file_name.split("[[")[1] if "[[" in file_name else file_name.split("[")[1]

        if(extension == "png" or extension == "jpg"):
            new_text = "!["+file_name+"](../assets/images/"+file_name+'.'+extension+"){:height 500, :width 500}"
            print(new_text)
            return new_text
        return old_text

    def process_markdown_files(self):
        for root, _, files in os.walk(self.base_directory):
            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r+', encoding='utf-8') as f:
                        lines = f.readlines()
                        f.seek(0)
                        for line in lines:
                            print(line+"8-8-8")
                            new_line = self.rename(line) if ("png" in line or "jpg" in line) else line
                            f.write(new_line)
                        f.truncate()

    def update_attachments_directory(self):
        for root, _, files in os.walk(self.base_directory):
            for file in files:
                if file.endswith(".png") or file.endswith(".jpg"):
                    file_path = os.path.join(root, file)  # Caminho completo do arquivo de origem
                    destination = os.path.join(self.attachments_directory, file)  # Caminho completo do arquivo de destino
                    
                    print("Copiando o arquivo:", file_path, "para", destination)
                    shutil.copyfile(file_path, destination)  # Copia o arquivo de origem para o destino



