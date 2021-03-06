# Organise script that allows you to 
# Move files by there extensions into
# The correct folder 

# Import modules
import os
import shutil
import send2trash

# focus directory
os.chdir('C:/Users/dylan/Downloads')

# variables
word = ['.doc', '.rtf']
pictures = ['.jpeg', '.jpg', '.png']
executable = ['.exe']

# Word documents
for word in os.listdir():
    shutil.move(word, 'D:/Word Documents')
    break

# Pictures
for pictures in os.listdir():
    shutil.move(pictures, 'D:/Pictures')
    break

# executable
for executable in os.listdir():
    shutil.move(executable, 'D:/Executable')
    break



