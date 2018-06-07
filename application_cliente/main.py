import numpy as np
import requests
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
from donnees import getDonnees


class Graphique():
    def __init__(self,temp_londres,temp_paris):
        self.temp_londres=temp_londres
        self.temp_paris=temp_paris

    def dessiner(self):
        n_groups = 12

        fig, ax = plt.subplots()

        index = np.arange(n_groups)
        bar_width = 0.35

        opacity = 0.4
        error_config = {'ecolor': '0.3'}

        rects1 = ax.bar(index, temp_londres, bar_width,
                alpha=opacity, color='b',
                # yerr=std_men, error_kw=error_config,
                label='Londres')

        rects2 = ax.bar(index + bar_width, temp_paris, bar_width,
                alpha=opacity, color='r',
                # yerr=std_women, error_kw=error_config,
                label='Paris')

        ax.set_xlabel('Mois')
        ax.set_ylabel('Température')
        ax.set_title('Températures comparées')
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(('janvier', 'février', 'mars', 'avril', 'mai','juin','juillet','aout','septembre','octobre','novembre','décembre'),fontsize='small')
        ax.legend()

        fig.tight_layout()
        plt.show()


temp= getDonnees()

temp_londres=temp['Londres']
temp_paris = temp['Paris']

Graphique = Graphique(temp_londres,temp_paris)

Graphique.dessiner()



















