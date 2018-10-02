import numpy as np
from psychopy import visual
from os.path import join

from sources.parameters import FIGURES
from sources.arrow import Arrow


class Matrix:
    def __init__(self, name, n_relations=2, n_figures=4):
        self.n_relations = n_relations
        self.n_figures = n_figures
        self.figures = []
        self.relations = []
        self.name = name
        self.stimulus = []

    def choose_figures(self):
        self.figures = list(np.random.choice(FIGURES, self.n_figures, replace=False))

    def create_relations(self):
        while len(self.relations) < self.n_relations:
            pair = list(np.random.choice(self.figures, 2, replace=False))
            if (pair not in self.relations) and (pair[::-1] not in self.relations):
                self.relations.append(pair)
        if self.n_relations > 1 and len(set([item for sublist in self.relations for item in sublist])) < self.n_figures:
            self.relations = []
            self.create_relations()

    def change_relation(self, n):
        rel_to_change = np.random.choice(range(self.n_relations), n)
        for rel in rel_to_change:
            self.relations[rel] = self.relations[rel][::-1]

    def prepare_draw(self, win, fig_size, fig_offset, center_pos, arrow_long, arrow_width, arrow_color='black'):
        for idx, figure in enumerate(self.figures):
            x = center_pos[0] - fig_offset / 2.0 + (idx % 2) * fig_offset
            y = center_pos[1] + fig_offset / 2.0 - (idx // 2) * fig_offset
            fig = visual.ImageStim(win=win, image=join('images', figure), interpolate=True,
                                   size=fig_size, pos=(x, y))
            self.stimulus.append(fig)

        for relation in self.relations:
            pos_1 = self.figures.index(relation[0])
            pos_2 = self.figures.index(relation[1])

            start = [0, 0]
            end = [0, 0]

            # higher horizontal lines
            if pos_1 == 0 and pos_2 == 1:
                start_x = center_pos[0] - fig_offset / 2.0 + fig_size/2.0
                start_y = center_pos[1] + fig_offset / 2.0
                end_x = center_pos[0] + fig_offset / 2.0 - fig_size/2.0
                end_y = center_pos[1] + fig_offset / 2.0
                start = [start_x, start_y]
                end = [end_x, end_y]

            elif pos_1 == 1 and pos_2 == 0:
                start_x = center_pos[0] + fig_offset / 2.0 - fig_size / 2.0
                start_y = center_pos[1] + fig_offset / 2.0
                end_x = center_pos[0] - fig_offset / 2.0 + fig_size / 2.0
                end_y = center_pos[1] + fig_offset / 2.0
                start = [start_x, start_y]
                end = [end_x, end_y]

            # lower horizontal lines
            elif pos_1 == 2 and pos_2 == 3:
                start_x = center_pos[0] - fig_offset / 2.0 + fig_size / 2.0
                start_y = center_pos[1] - fig_offset / 2.0
                end_x = center_pos[0] + fig_offset / 2.0 - fig_size / 2.0
                end_y = center_pos[1] - fig_offset / 2.0
                start = [start_x, start_y]
                end = [end_x, end_y]

            elif pos_1 == 3 and pos_2 == 2:
                start_x = center_pos[0] + fig_offset / 2.0 - fig_size / 2.0
                start_y = center_pos[1] - fig_offset / 2.0
                end_x = center_pos[0] - fig_offset / 2.0 + fig_size / 2.0
                end_y = center_pos[1] - fig_offset / 2.0
                start = [start_x, start_y]
                end = [end_x, end_y]

            # Left vertical lines
            elif pos_1 == 0 and pos_2 == 2:
                start_x = center_pos[0] - fig_offset / 2.0
                start_y = center_pos[1] + fig_offset / 2.0 - fig_size / 2.0
                end_x = center_pos[0] - fig_offset / 2.0
                end_y = center_pos[1] - fig_offset / 2.0 + fig_size / 2.0
                start = [start_x, start_y]
                end = [end_x, end_y]

            elif pos_1 == 2 and pos_2 == 0:
                start_x = center_pos[0] - fig_offset / 2.0
                start_y = center_pos[1] - fig_offset / 2.0 + fig_size / 2.0
                end_x = center_pos[0] - fig_offset / 2.0
                end_y = center_pos[1] + fig_offset / 2.0 - fig_size / 2.0
                start = [start_x, start_y]
                end = [end_x, end_y]

            # Right vertical lines
            elif pos_1 == 1 and pos_2 == 3:
                start_x = center_pos[0] + fig_offset / 2.0
                start_y = center_pos[1] + fig_offset / 2.0 - fig_size / 2.0
                end_x = center_pos[0] + fig_offset / 2.0
                end_y = center_pos[1] - fig_offset / 2.0 + fig_size / 2.0
                start = [start_x, start_y]
                end = [end_x, end_y]

            elif pos_1 == 3 and pos_2 == 1:
                start_x = center_pos[0] + fig_offset / 2.0
                start_y = center_pos[1] - fig_offset / 2.0 + fig_size / 2.0
                end_x = center_pos[0] + fig_offset / 2.0
                end_y = center_pos[1] + fig_offset / 2.0 - fig_size / 2.0
                start = [start_x, start_y]
                end = [end_x, end_y]

            # Diagonal lines
            elif pos_1 == 0 and pos_2 == 3:
                start_x = center_pos[0] - fig_offset / 2.0 + fig_size / 2.0
                start_y = center_pos[1] + fig_offset / 2.0 - fig_size / 2.0
                end_x = center_pos[0] + fig_offset / 2.0 - fig_size / 2.0
                end_y = center_pos[1] - fig_offset / 2.0 + fig_size / 2.0
                start = [start_x, start_y]
                end = [end_x, end_y]

            elif pos_1 == 3 and pos_2 == 0:
                start_x = center_pos[0] + fig_offset / 2.0 - fig_size / 2.0
                start_y = center_pos[1] - fig_offset / 2.0 + fig_size / 2.0
                end_x = center_pos[0] - fig_offset / 2.0 + fig_size / 2.0
                end_y = center_pos[1] + fig_offset / 2.0 - fig_size / 2.0
                start = [start_x, start_y]
                end = [end_x, end_y]

            elif pos_1 == 1 and pos_2 == 2:
                start_x = center_pos[0] + fig_offset / 2.0 - fig_size / 2.0
                start_y = center_pos[1] + fig_offset / 2.0 - fig_size / 2.0
                end_x = center_pos[0] - fig_offset / 2.0 + fig_size / 2.0
                end_y = center_pos[1] - fig_offset / 2.0 + fig_size / 2.0
                start = [start_x, start_y]
                end = [end_x, end_y]

            elif pos_1 == 2 and pos_2 == 1:
                start_x = center_pos[0] - fig_offset / 2.0 + fig_size / 2.0
                start_y = center_pos[1] - fig_offset / 2.0 + fig_size / 2.0
                end_x = center_pos[0] + fig_offset / 2.0 - fig_size / 2.0
                end_y = center_pos[1] + fig_offset / 2.0 - fig_size / 2.0
                start = [start_x, start_y]
                end = [end_x, end_y]
            if self.n_relations == 1 and self.name == 'wrong_2':
                arrow = Arrow(win, arrow_color, start, end, 0, 0)
            else:
                arrow = Arrow(win, arrow_color, start, end, arrow_long, arrow_width)
            self.stimulus.append(arrow)

    def set_auto_draw(self, draw):
        for stim in self.stimulus:
            stim.setAutoDraw(draw)

    def get_info(self):
        info = {
            'n_relations': self.n_relations,
            'n_figures': self.n_figures,
            'figures': self.figures,
            'relations': self.relations,
            'name': self.name}
        return info
