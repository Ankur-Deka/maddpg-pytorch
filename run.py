# -------- import GridSearch and define/import the compile function -------- #
import sys
sys.path.append('SIGS-Grid-Search')
from grid_search import GridSearch

# -------- main file to run -------- #
main_file = 'main.py'
num_process = 6
# -------- define dictionary of arguments for grid search -------- #
args = {'env_id': ['simple', 'simple_tag', 'simple_adversary'],
		'model_name': ['exp_1'],
		'n_episodes': [1000]}

# -------- create GridSearch object and run -------- #
myGridSearch = GridSearch(main_file, args, num_process=num_process)
myGridSearch.run()