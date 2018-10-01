import psychopy
import numpy as np


class Arrow:
    def __init__(self, win, color, start, end, arrow_long, arrow_width):
        self.line1 = psychopy.visual.Line(win=win, units="pix", lineColor=color)
        self.line2 = psychopy.visual.Line(win=win, units="pix", lineColor=color)
        self.line3 = psychopy.visual.Line(win=win, units="pix", lineColor=color)

        x = end[0] - start[0]
        y = end[1] - start[1]
        d = np.sqrt(x ** 2 + y ** 2)

        # main line
        self.line1.start = start
        self.line1.end = end

        x1 = end[0] - x * arrow_long / d + y * arrow_width / d
        y1 = end[1] - y * arrow_long / d - x * arrow_width / d

        self.line2.start = [x1, y1]
        self.line2.end = end

        x1 = end[0] - x * arrow_long / d - y * arrow_width / d
        y1 = end[1] - y * arrow_long / d + x * arrow_width / d

        self.line3.start = [x1, y1]
        self.line3.end = end

    def setAutoDraw(self, draw):
        for stim in [self.line1, self.line2, self.line3]:
            stim.setAutoDraw(draw)
