import shutil,os

def zipper(output_name,dir_name): # the zip function
    shutil.make_archive(output_name,'zip',dir_name)
    print('Zipping the directory'+str(dir_name))

zipper('myZip',os.path.dirname(os.path.abspath(__file__)))
# call function and give it required params.
#This example uses the current directory.
#One can use tkinter to select any other directory.
#This can be imported in mail2.py and be used as a preprocessing tool before sending attachments