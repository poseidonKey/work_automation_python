import pywinmacro as p
import time

# time.sleep(5)
# print(p.get_mouse_position())

p.key_on("window")
p.key_press_once("r")
# p.key_on("r")
p.key_off("window")
# p.key_off("r")
# time.sleep (1)
# p.move_mouse((108,940))
# time.sleep(2)
# p.l_click()

p.typing("notepad")
# time.sleep(1)
p.key_press_once("enter")