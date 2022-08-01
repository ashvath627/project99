import os
import time
import shutil

from cv2 import threshold

dir_path = input('Enter Folder Path:')

threshold = time.time() - 30*86400
for i in os.listdir(dir_path):
    try:
        if os.path.getmtime(dir_path + '//' + i) < threshold:
            os.remove(dir_path + '//' + i)
            print(i + ' deleted.')
    
    except:
        pass