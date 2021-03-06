# automation.py
from shutil import move
import os

dir = os.path.dirname
sep = os.sep


# directory paths
current_dir = dir(__file__)#la carpeta en la que me encuentro en este fichero
from_dir = current_dir + sep + "from_folder" + sep 
to_folder = current_dir + sep + "to_folder" + sep 

doc_file = to_folder + sep + "doc" + sep
img_file = to_folder + sep + "image" + sep

if not os.path.exists(to_folder): #si no existe la carpeta la cras
       os.mkdir(to_folder)
if not os.path.exists(img_file): #si no existe la carpeta la cras
       os.mkdir(img_file)
if not os.path.exists(doc_file):
       os.mkdir(doc_file)
       
# category wise file types #los archivosque quiero encontrar para pasar a la carpeta
doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff')

def get_non_hidden_files_except_current_file(root_dir):
  return [f for f in os.listdir(root_dir) if os.path.isfile(root_dir + f) and not f.startswith('.')]
#listdir busca todas las carpetaws que hay dentro del archivo y los que no empiezan por . eso es starswith ., esos son archivos ocultos
def move_files(files):
  for file in files:
    # file moved and overwritten if already exists
    if file.endswith(doc_types):
      move(from_dir + file, doc_file)
      print('file {} moved to {}'.format(file, doc_file))
    elif file.endswith(img_types):
      move(from_dir + file, img_file)
      print('file {} moved to {}'.format(file, img_file))
    else:
          print("~~~~~~~~~~~~")
          print(str(file))
          print("This file is not an image or document")

if __name__ == "__main__":
  files = get_non_hidden_files_except_current_file(from_dir)
  
  move_files(files)