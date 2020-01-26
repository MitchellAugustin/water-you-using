killall python2.7
ble-serial -d 98:5D:AD:14:24:AB &
sleep 8
cd /home/pi/water-you-using-backend
/usr/bin/python2.7 /home/pi/water-you-using-backend/router.py &
sleep 8
/usr/bin/python2.7 /home/pi/main.py 
