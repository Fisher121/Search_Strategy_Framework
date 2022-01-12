from SSF import SSF
from problems.ClassicGraphSearchProblem import ClassicGraphSearchProblem
from problems.GridProblem import Grid
from strategies.uninformed.BDS import BDS
from strategies.uninformed.BFS import BFS
from strategies.uninformed.Backtracking import Backtracking
from strategies.uninformed.DFS import DFS
from strategies.uninformed.IDS import IDS
from strategies.uninformed.Random import Random
from strategies.uninformed.UCS import UCS
from strategies.informed.AStar import A_Star
from strategies.informed.GBF import GBF

problem = ClassicGraphSearchProblem()

print("Rezultat BFS")
method = BFS()
framework = SSF()
print(framework.SolveUninformed(problem, method))

print("Rezultat DFS")
method = DFS()
framework = SSF()
print(framework.SolveUninformed(problem, method))

print("Rezultat IDS")
method = IDS()
framework = SSF()
print(framework.SolveUninformed(problem, method))

print("Rezultat UCS")
method = UCS()
framework = SSF()
print(framework.SolveUninformed(problem, method))

print("Rezultat Random")
method = Random()
framework = SSF()
print(framework.SolveUninformed(problem, method))

print("Rezultat Backtracking")
method = Backtracking()
framework = SSF()
print(framework.SolveUninformed(problem, method))

print("Rezultat BDS")
method = BDS()
framework = SSF()
print(framework.SolveUninformed(problem, method))


#Problemele de tip informed nu functioneaza GBF/A*
#print("Rezultat GBF")
#problem = GridProblem()
#method = GBF()
#framework = SSF()
#print(framework.SolveInformed(problem, method))