import os
def rename_files():
    file_list = os.listdir(r"C:\Trey\Teo\alphabet")
    #You will have to insert your own directory here.
    saved_path = os.getcwd()
    print("Current Directory is "+saved_path)
    os.chdir(r"C:\Trey\Teo\alphabet")
    #And insert it here.
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "1234567890"))
    os.chdir(saved_path)

rename_files()
