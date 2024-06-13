import os
import glob

if __name__ == "__main__":
    dirs = os.listdir(os.path.join('./images'))
    print(dirs)
    for d in dirs:
        dir_path = os.path.join('./images/' + d)
        f = os.listdir(dir_path)
        i = 1
        for fil in f:
            file_path = os.path.join('./images/' + d + "/" + fil)
            print(file_path)
            new_name = str(i) + "-" + d + ".txt"
            print(new_name)
            new_file_name = os.path.join('./text/' + d + "/" + new_name)
            i += 1
            try:
                f = open(new_file_name, 'x')
            except Exception as e:
                print(e)
