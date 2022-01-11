from SSF import SSF
from problems.ClassicGraphSearchProblem import ClassicGraphSearchProblem
from strategies.uninformed.BDS import BDS
from strategies.uninformed.BFS import BFS
from strategies.uninformed.Backtracking import Backtracking
from strategies.uninformed.DFS import DFS
from strategies.uninformed.IDS import IDS
from strategies.uninformed.Random import Random
from strategies.uninformed.UCS import UCS

problem = ClassicGraphSearchProblem()
number = 0
bk = IDS()
framework = SSF()
print(framework.SolveUninformed(problem, bk))
