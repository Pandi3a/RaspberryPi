import os
import getpass

usb="/media/"+getpass.getuser()+"/*/*"
# The source is a USB drive
dest="/home/"+getpass.getuser()+"/Videos"
# change dest corespondingly
os.system(" rsync -0 " + usb + " " + dest + " ")
