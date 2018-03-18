try:
    import pygame.midi
except ImportError:
    try:
        import pip
    except ImportError:
        print("Installing pip")
        import urllib.request
        urllib.request.urlretrieve("https://bootstrap.pypa.io/get-pip.py", "getpip.py")
        import getpip
        getpip.main()
        import pip
        print("Installing pygame")
        pip.main(['install', 'pygame'])
    print("Installing pygame...")
    pip.main(['install', 'pygame'])
import os
import json
import sys
try:
    import keyboard
except ImportError:
    try:
        import pip
    except ImportError:
        print("Installing pip")
        import urllib.request
        urllib.request.urlretrieve("https://bootstrap.pypa.io/get-pip.py", "getpip.py")
        import getpip
        getpip.main()
        import pip
        print("Installing keyboard")
        pip.main(['install', 'keyboard'])
    print("Installing keyboard")
    pip.main(['install', 'keyboard'])
try:
    import mouse
except ImportError: 
    try:
        import pip
    except ImportError:
        print("Installing pip")
        import urllib.request
        urllib.request.urlretrieve("https://bootstrap.pypa.io/get-pip.py", "getpip.py")
        import getpip
        getpip.main()
        import pip
        print("Installing mouse")
        pip.main(['install', 'mouse'])
    print("Installing mouse")    
    pip.main(['install', 'mouse'])


pygame.midi.init()
def get_device():  
    count = pygame.midi.get_count()
    xd = []
    for i in range(0,count):
        xddd = pygame.midi.get_device_info(i) + (i, 0)
        xd.append(xddd)
    for i in range(0,2):
        for i in xd:
            if i[2] == 0:
                del xd[xd.index(i)]
    for i in range(0,len(xd)):
        lol = str(i)
        device = xd[i][1]
        loll = device.decode("utf-8")
        print("[" + lol  + "]" + " " + loll)
    device = int(input("Select device: "))
    if device > len(xd) - 1 or device < 0:
        print("Invalid device...")
        get_device()    
    return xd[device][5]


def firstrun(port):
    if os.path.isfile("config.json") == True:
        pass
    else:
        print("Play the upper note and the lower note in your midi instrument.")
        xd = []
        while True:
            if len(xd) == 4:
                break
            msg = port.read(1)
            if not msg:
                continue    
            xd.append(msg)
        for i in xd:
            ii = i[0][0][2]
            if ii == 0: 
                del xd[xd.index(i)]
            else:
                pass
        range_midi = []
        for i in xd:
            ii = i[0][0][1]
            range_midi.append(ii)
        print("Press key for q: ")
        q = ''
        while True:
            if q is not '':
                break
            msg = port.read(1)
            if not msg:
                continue
            if msg[0][0][2] == 0:
                continue    
            q = str(msg[0][0][1])
        print("Press key for w:")
        w = ''
        while True:
            if w is not '':
                break
            msg = port.read(1)
            if not msg:
                continue
            if msg[0][0][2] == 0:
                continue     
            w = str(msg[0][0][1])
        print("Press key for e:")
        e = ''
        while True:
            if e is not '':
                break
            msg = port.read(1)
            if not msg:
                continue   
            if msg[0][0][2] == 0:
                continue  
            e = str(msg[0][0][1])
        print("Press key for r:")
        r = ''
        while True:
            if r is not '':
                break
            msg = port.read(1)
            if not msg:
                continue   
            if msg[0][0][2] == 0:
                continue  
            r = str(msg[0][0][1])
        print("Press key for d:")
        d = ''
        while True:
            if d is not '':
                break
            msg = port.read(1)
            if not msg:
                continue   
            if msg[0][0][2] == 0:
                continue  
            d = str(msg[0][0][1])
        print("Press key for f:")
        f = ''
        while True:
            if f is not '':
                break
            msg = port.read(1)
            if not msg:
                continue   
            if msg[0][0][2] == 0:
                continue  
            f = str(msg[0][0][1])
        print("Press key for left click:")
        leftclick = ''
        while True:
            if leftclick is not '':
                break
            msg = port.read(1)
            if not msg:
                continue   
            if msg[0][0][2] == 0:
                continue  
            leftclick = str(msg[0][0][1])
        print("Press key for right click:")
        rightclick = ''
        while True:
            if rightclick is not '':
                break
            msg = port.read(1)
            if not msg:
                continue   
            if msg[0][0][2] == 0:
                continue  
            rightclick = str(msg[0][0][1])
        jsondict = {
            'min_range': str(range_midi[0]),
            'max_range': str(range_midi[1]),
            'q': q,
            'w': w,
            'e': e,
            'r': r,
            'd': d,
            'f': f,
            'leftclick': leftclick,
            'rightclick': rightclick
        }
        with open("config.json", "w") as filee:
            json.dump(jsondict, filee)

def readconfig(parameter):
    parameter = str(parameter)
    read = open("config.json", "r")
    xd = json.load(read)
    return xd[parameter]

device = get_device()
port = pygame.midi.Input(device)
firstrun(port)
###read config#######
q = int(readconfig('q'))
w = int(readconfig('w'))
e = int(readconfig('e'))
r = int(readconfig('r'))
d = int(readconfig('d'))
f = int(readconfig('f'))
leftclick = int(readconfig('leftclick'))
rightclick = int(readconfig('rightclick'))
#####################
while True:
    try:
        msg = port.read(1)
        if not msg:
            continue
        if msg[0][0][2] == 0:
            continue
        if  msg[0][0][1] == q:
            keyboard.send('q')
        if  msg[0][0][1] == w:
            keyboard.send('w')
        if  msg[0][0][1] == e:
            keyboard.send('e')
        if  msg[0][0][1] == r:
            keyboard.send('r')
        if  msg[0][0][1] == d:
            keyboard.send('d')
        if  msg[0][0][1] == f:
            keyboard.send('f')
        if  msg[0][0][1] == leftclick:
            mouse.click(button='left')
        if  msg[0][0][1] == rightclick:
            mouse.right_click()             
        print(msg)
    except KeyboardInterrupt:
        break

pygame.midi.quit()
print("Bye!!")
try:
    sys.exit(0)
except SystemExit:
    os._exit(0)

