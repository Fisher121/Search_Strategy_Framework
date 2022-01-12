from SSF import SSF
from problems.ClassicGraphSearchProblem import ClassicGraphSearchProblem
from problems.RiverCrossing import RiverCrossing, Stare
from strategies.uninformed.BDS import BDS
from strategies.uninformed.BFS import BFS
from strategies.uninformed.Backtracking import Backtracking
from strategies.uninformed.DFS import DFS
from strategies.uninformed.IDS import IDS
from strategies.uninformed.Random import Random
from strategies.uninformed.UCS import UCS


problem = ClassicGraphSearchProblem()
number = 0
rcProblem = RiverCrossing()
rcProblem.GetAllStates()

bk = DFS()
framework = SSF()
sol = framework.SolveUninformed(problem, bk)
for i in sol:
    print(i)
