### DOCUMENTATION

#### Before run 
```yum install python3-pip
    pip3 install sched
    pip3 install argparse
```

#### Run script
``` python3 pharse1.py -c "announce flow route {match { destination 8.8.8.8/32; source 101.96.88.0/24; destination-port =53; protocol udp; } then { discard;}"

NOTE: Hiện tại đang để  tự động xóa sau 30s, lưu vào file test1.txt. ( có thể sửa trong file pharse1.py)