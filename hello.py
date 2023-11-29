#!./venv/bin/python3 
from subprocess import call
import time 
from random import randint
while True:
    n = randint(0, 2)
    mac = f"{2*str(n)}:{2*str(n+1)}:{2*str(n+2)}:{2*str(n+3)}:{2*str(n+4)}:{2*str(n+5)}"
    call(["ifconfig", 'eth0', 'down'])
    call(["ifconfig", 'eth0', 'hw', 'ether', mac])
    call(["ifconfig", 'eth0', 'up'])
    time.sleep(5)
print("Mac addres succesfuly changed!!!")
