from gui.window import Window
from gui.draw import Draw

win = Window()

win.open()

Draw.set_cell(1,1, 1)

while win.is_running:
    
    win.update()
    Draw.draw_grid()
    win.tick()