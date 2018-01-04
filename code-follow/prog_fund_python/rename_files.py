import os

def rename_files():
    saved_path = os.getcwd()
    file_list = os.listdir("../../prank")
    os.chdir("../../prank")

    print(file_list)
    
    nums = u"0123456789"
    nums = [ord(char) for char in nums]
    translate_to = [None for char in nums] 
    trans_table = dict(zip(nums, translate_to))

    for file_name in file_list:
        os.rename(file_name, file_name.translate(trans_table))
    os.chdir(saved_path)


rename_files()
