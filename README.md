# Joint Chance-constrained Game for Coordinating Microgrids in Energy and Reserve Markets

Authors: Yifu Ding (MIT), Benjamin Hobbs (Johns Hopkins University)


This repository is the supplement material for the submission of IEEE transactions on smart grid; The fold (Results) include all the game results in the case study, which allows reproducing the result charts.


Four kinds of csv files are presented. They are named by "type of results + number of players + scenarios". For example, the 'optimization10c1.csv' file presents the game optimization results in the 10-player game for scenario c1. 

These four types of results in the 'csv' files are:

- 'optimization': the summary of game results include the energy and reserve bids of each player (i.e., microgrid). The positive value means microgrids procure energy and reserve services, and the negative value means microgrids sells energy and reserve services.

- 'profits': the summary of profits/costs of each player (i.e., microgrid). The last row is the cost of ISO.

- 'reserve': the summary of the under-delivered reserve of each player (i.e., microgrid) in 150 out-of-sample tests.

- 'violation': the summary of violation rates for 50 repeated experiments (each experiment includes 150 out-of-sample tests).

The Final_plot.py in the folder allows reproducing the results charts.





