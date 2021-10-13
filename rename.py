
# Python program to rename all file
# names in your directory
import os
 
os.chdir('/home/remnux/Pictures/doc_samples/clean')
print(os.getcwd())
 
for count, f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)
    f_name = "sample" + str(count)
 
    new_name = f'{f_name}{f_ext}'
    os.rename(f, new_name)
