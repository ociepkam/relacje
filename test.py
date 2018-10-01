import psychopy.visual
import psychopy.event
import numpy as np

win = psychopy.visual.Window(
    size=[400, 400],
    fullscr=False,
    monitor='testMonitor', units='pix',
    screen=0, color='Gainsboro', winType='pygame')





def draw_arrow(win, color, start, end, arrow_long, arrow_width):
    line = psychopy.visual.Line(win=win, units="pix", lineColor=color)

    x = end[0] - start[0]
    y = end[1] - start[1]
    d = np.sqrt(x**2 + y**2)

    # main line
    line.start = start
    line.end = end
    line.draw()

    x1 = end[0] - end[0] * arrow_long / d + end[1] * arrow_width / d
    y1 = end[1] - end[1] * arrow_long / d - end[0] * arrow_width / d

    line.start = [x1, y1]
    line.end = end
    line.draw()

    x1 = end[0] - end[0] * arrow_long / d - end[1] * arrow_width / d
    y1 = end[1] - end[1] * arrow_long / d + end[0] * arrow_width / d

    line.start = [x1, y1]
    line.end = end
    line.draw()

    # line.start = [10, 20]
    # line.end = end
    # line.draw()


a = Arrow(win, 'black', [20, 0], [60, 0], 20, 20)
a.set_auto_draw(True)
win.flip()
a.set_auto_draw(False)
win.flip()
win.getMovieFrame()
psychopy.event.waitKeys()
