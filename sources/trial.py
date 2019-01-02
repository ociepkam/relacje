import numpy as np
from copy import deepcopy

from sources.matrix import Matrix


class Trial:
    def __init__(self, n_relations=2, n_figures=4):
        self.n_relations = n_relations
        self.n_figures = n_figures

        self.matrix_main = Matrix("main", n_relations, n_figures)
        self.matrix_main.choose_figures()
        self.matrix_main.create_relations()

        perm = [self.matrix_main.figures]

        while len(perm) < 5:
            p = list(np.random.permutation(self.matrix_main.figures))
            if p not in perm:
                perm.append(p)

        self.matrix_answer = deepcopy(self.matrix_main)
        self.matrix_answer.name = "answer"
        self.matrix_answer.figures = perm[1]

        self.matrix_wrong_1 = deepcopy(self.matrix_main)
        self.matrix_wrong_1.name = "wrong_1"
        self.matrix_wrong_1.figures = perm[2]
        self.matrix_wrong_1.change_relation(1)

        # while True:
        #     self.matrix_wrong_2 = deepcopy(self.matrix_main)
        #     self.matrix_wrong_2.name = "wrong_2"
        #     self.matrix_wrong_2.figures = perm[3]
        #     self.matrix_wrong_2.change_relation(1)
        #     if self.matrix_wrong_2.relations != self.matrix_wrong_1.relations:
        #         break

        self.matrix_wrong_3 = deepcopy(self.matrix_main)
        self.matrix_wrong_3.name = "wrong_2"
        self.matrix_wrong_3.figures = perm[4]
        self.matrix_wrong_3.change_relation(2)

        self.answers = [self.matrix_wrong_1, self.matrix_wrong_3, self.matrix_answer]
        np.random.shuffle(self.answers)

    def prepare_to_draw(self, win, main_fig_size, main_move_y, answers_fig_size, answers_pos, fig_offset,
                        arrow_long, arrow_width, arrow_color='black'):
        self.matrix_main.prepare_draw(win, main_fig_size, fig_offset, (0, main_move_y),
                                      arrow_long, arrow_width, arrow_color)
        for idx, matrix in enumerate(self.answers):
            matrix.prepare_draw(win, answers_fig_size, fig_offset, answers_pos[idx],
                                arrow_long, arrow_width, arrow_color)

    def set_auto_draw(self, draw=True):
        for matrix in [self.matrix_main, self.matrix_answer, self.matrix_wrong_1, self.matrix_wrong_3]:
            matrix.set_auto_draw(draw)

    def get_info(self):
        info = {
            'n_relations': self.n_relations,
            'n_figures': self.n_figures,
            'main_matrix': self.matrix_main.get_info(),
            'answers': [answer.get_info() for answer in self.answers]}
        return info
