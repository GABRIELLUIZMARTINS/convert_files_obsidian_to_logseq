
if False:
    text_old = "![[410ce7ce27c939e0b11cccd73237cd4.jpg]]"
else:
    text_old= "![[Pasted image 20240610111054.png|500]]"


if not text_old[3] == '[' :
    print("OK",text_old[3]) 
    exit()
#Extract extension name
extension = text_old.split(".")[1].split("]")[0]
extension = extension.split("|")[0] if "|" in extension else extension

#Extract file name
file_name = text_old.split(".")[0].split("[[")[1] 

print(extension+"\n\n")

if(extension == "png" or extension == "jpg"):
    texto_novo = "!["+file_name+"](../assets/images/"+file_name+'.'+extension+"){:height 500, :width 500}"

    print(texto_novo)
    print("![Pasted image 20240823091746](../assets/images/Pasted image 20240823091746.png){:height 500, :width 500}")

"""
import os
import shutil


base_directory = 'C:/Users/gabriel.martins/Downloads/Projetos'
attachments_directory = 'C:/Users/gabriel.martins/OneDrive - Docol Metais Sanitários Ltda/Área de Trabalho/LogSeq/assets/images'

# Obsidian Image - "![[file_name.png|500]]" or "![[file_name.png]]"
# Logseq Image - "![file_name](../assets/images/file_name.extension){:height 500, :width 500}"

def rename(old_text):
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

def process_markdown_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r+', encoding='utf-8') as f:
                    lines = f.readlines()
                    f.seek(0)
                    for line in lines:
                        print(line+"8-8-8")
                        new_line = rename(line) if ("png" in line or "jpg" in line) else line
                        #new_line = rename(line)
                        f.write(new_line)
                    f.truncate()

def update_attachments_directory(source_directory,destination_directory):
    for root, _, files in os.walk(source_directory):
        for file in files:
            if file.endswith(".png") or file.endswith(".jpg"):
                file_path = os.path.join(root, file)  # Caminho completo do arquivo de origem
                destination = os.path.join(destination_directory, file)  # Caminho completo do arquivo de destino
                
                print("Copiando o arquivo:", file_path, "para", destination)
                shutil.copyfile(file_path, destination)  # Copia o arquivo de origem para o destino


process_markdown_files(base_directory)
update_attachments_directory(base_directory,attachments_directory)


"""