import sys
import os 

os.getcwd() ## ---> Juypter notebook

__file__  # la diferencia es que file nos da toda la ruta entera incluyendo el archivo no como jupiter
## Jupiter te lo da a la carpeta. La diferencia ese que en .py tienes que subir un puesto mas hasta llegar 
# a la carpeta


if __name__ == '_main_':
    import os 
    dir = os.path.dirname
    dir(__file__)
    # si quiero subir dos veces se pone dir dos veces
    dir(dir(__file__))
    sys.path.append(src_path)


    from dashboard.a import function_a


    