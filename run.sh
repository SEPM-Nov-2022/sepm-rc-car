rm rc-car.log 2>/dev/null
python3 -m rc_car.rc_car_launcher & 
python3 audit_server/audit_server.py
