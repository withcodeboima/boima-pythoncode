# Modules are extra parts that we can attach to our program
# For example if you want to random numbers we would add the random module to our program
# We can also create our own modules across multiple files to make the code more organised
# Adding extra parts 
# You can import from the python standard library. These are preinstalled with python
# External modules are made by other programmers. They give us huge amount of extra functionality.
# For example game development, data analysis machine,learning graphic user interfaces are 
# all functionalities we get from extrenal modules.
# These modules are imported like standard modules 
# However we first need to instal them. This usually happens in the powershell or the terminal
# Command line are the way to interact with your computer by writing text

# import pyautogui
# from time import sleep

# pyautogui is an external module that allows us to control the mouse and keyboard
# We can use it to automate tasks on our computer
# sleep(1)
# pyautogui.write("Hello world!")

# import pyautogui
# from time import sleep

# sleep(2)

# pyautogui.press("win")
# sleep(1)

# pyautogui.write("notepad", interval=0.1)
# sleep(1)

# pyautogui.press("enter")
# sleep(2)

# pyautogui.write("Hello world!", interval=0.1)

import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.xlabel('second numbers')
plt.show()


# import matplotlib.pyplot as plt

# sizes = [40, 30, 20, 10]
# labels = ["A", "B", "C", "D"]

# plt.pie(sizes, labels=labels)
# plt.show()