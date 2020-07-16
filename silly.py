#!/usr/bin/env python


try:
    import pyperclip
    we_pyperclipin = True;
except ModuleNotFoundError:
    we_pyperclipin = False;
    print("Install pyperclip if you want silly text to be automatically copied to your clipboard (pip install pyperclip)")

while (True):
    silly = ''.join([(x.upper() if i%2==0 else x.lower()) for i, x in enumerate(input())])
    if we_pyperclipin: pyperclip.copy(silly)
    print(silly)
