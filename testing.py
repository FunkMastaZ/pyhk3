import pyhk


def fun():
    print
    "Do something"


# create pyhk class instance
hot = pyhk.pyhk()

# add hotkey
id1 = hot.addHotkey(['mouse left'], fun)

# start looking for hotkey.
hot.start()
