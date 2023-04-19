import os
import shutil

from_dir = "C:/Users/lului/Downloads"
to_dir = "C:/Users/lului/OneDrive/Área de Trabalho/códigos em python/progeto 111/arquivos_documentos"
list_of_files = os.listdir(from_dir)
#sprint(list_of_files)

for lop in (list_of_files):
    name, extension = os.path.splitext(lop)
    
    if extension == "":
        continue
    if extension in['.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir +'/' +lop
        path2 = to_dir +'/' +'Arquivos_Documentos'
        path3 = to_dir + '/' +'Arquivos_ Documentos' +'/' +lop

        if os.path.exists(path2):
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            shutil.move(path1, path3)