import mss
import mss.tools
from PIL import Image
import os 
import PIL 
import glob
import json  
import socket
import sys
import time
# if len(sys.argv) == 3:
#     # Get "IP address of Server" and also the "port number" from
#     argument 1 and argument 2
#     ip = sys.argv[1]
#     port = int(sys.argv[2])
# else:
#     print("Run like : python3 server.py <arg1:server ip:this system IP 192.168.1.6> <arg2:server port:4444 >")
#     exit(1)

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the port
server_address = ("192.168.2.111", "4210")
s.connect(("192.168.2.111",4210))
print("Do Ctrl+c to exit the program !!")

# while True:
#     # print("####### Server is listening #######")
#     # data, address = s.recvfrom(4096)
#     # print("\n\n 2. Server received: ", data.decode('utf-8'), "\n\n")
#     send_data = input("Type some text to send => ")
#     s.sendto(send_data.encode('utf-8'), ("192.168.2.111", 4210))
#     print("\n\n 1. Server sent : ", send_data,"\n\n")
#     time.sleep(1)


while True:
    with mss.mss() as sct:
        # for filename in sct.save():
        #     print(filename)
        monitor={"top":1430, "left": 0, "width": 5120, "height": 10}
        output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
        sct_img = sct.grab(monitor)

        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        # print(output)
        # print(sct.monitors)
        image = mss.tools.to_png(sct_img.rgb, sct_img.size)
        # print(sct_img.size)
        image = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        # image.save("asdf.png")
        newsize= (73,1)
        image = image.resize(newsize)
        image = image.transpose(Image.FLIP_LEFT_RIGHT)
        # image.save("asdf.png")
        # image.show()
        for i in range(70):
            # print(image.getpixel((i,0)))
            # s.sendto(str(i).encode('utf-8'), ("192.168.2.111", 4210))
            pixels = list(image.getpixel((i,0)))
            pixels.append(int(i))
            # print(pixels)
            s.sendto(json.dumps({"r":pixels[0],"g":pixels[1],"b":pixels[2],"i":pixels[3]}).replace(" ","").encode('utf-8'), ("Schreibtisch", 4210))
        # print(list(image.getdata()))
        # sjon = json.dumps(list(image.getdata()))
        # print(sjon)
        time.sleep(0.1)