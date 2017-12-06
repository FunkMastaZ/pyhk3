import pyhk


def fun():
    print("Do something")

# create pyhk class instance
hot = pyhk.pyhk()

# add hotkey
id1 = hot.addHotkey(['Ctrl', 'Alt', '7'], fun)

# start looking for hotkey.
hot.start()
