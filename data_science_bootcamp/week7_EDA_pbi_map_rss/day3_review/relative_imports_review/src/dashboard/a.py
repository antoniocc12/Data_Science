import os, sys
dir = os.path.dirname
src_path = dir(dir(__file__))
print("")
#print(src_path)
sys.path.append(src_path)
from utils.c import function_c

def function_a():
    print ("Function a")
    return function_c()

if __name__ == '__main__':
    #print("src_path:\n", src_path)
    function_a()