rm rc-car.log 2>/dev/null
python3 rc_car/rc_car_launcher.py & 
python3 audit_server/audit_server.py
