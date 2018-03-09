# RaspberryPi Video
Raspberry Pi Project to loop trough videos from Videos folder and rsync from USB flash drive when inserted(every 5 minutes scans for usb drive and videos)

################################################################################

1.Place scripts in home directory.

2.Give them permissions:

   $ chmod 755 /home/pi/usbsync.sh
   $ chmod 755 /home/pi/usbsync.py
   $ chmod 755 /home/pi/videoplayer.sh

3.Add to crontab
    
   $ crontab -e 

choose your prefered editor and at the end add these two lines:

*/5 * * * * /home/pi/usbsync.sh  -- This line makes sure that everey 5 minutes the usbsync.sh is executed and files are copied from usb stick.
@reboot /home/pi/videoplayer.sh  -- This cronjob executes the script on boot.

################################################################################

The script videoplayer.sh is from http://www.cenolan.com/2013/03/looping-video-playlist-omxplayer-raspberry-pi/ 

I do not take credit for it at all!!! Thakns to this guy i owe him a beer!!!
