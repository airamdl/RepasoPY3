#Airam
import os
import shutil

def file_sorter():
    dir: str = os.getcwd()

    for file in os.listdir(dir):
        if os.path.isfile(file):
            _, extension = os.path.splitext(file) #Si por ejemplo el archivo es imagen.png nos daria una tupla con dos elementos y no nos interesa por lo que usamos el _
            extension = extension[1:]



            final_dir = os.path.join(dir, extension)
            if not os.path.exists(final_dir):
                os.makedirs(final_dir)

            shutil.move(os.path.join(dir, file), os.path.join(final_dir, file))

if __name__ == '__main__':
    file_sorter()