from Queue import PriorityQueue


"""
-Sstart denotes start vertex
-Sgoal denotes goal vertex
-C(s,s') cost of transiton between tow neighboring certices s,s'ES
-succ(s) the set of seccessors of vertex s in ES 

Step1- Generate a list - 
Step2- Store Children in Priority Queue based on distance to goal
Step3 Select Closest child and repeat from sptep 1

"""
class Node():

  def __init__(self, parentNode, positon):
    self.parentNode=parentNode
    self.positon = positon
    self.Distance = 0
    self.goal = 0
    self.cost=0


class Storing(object):
  def __init__(self,value,parent,start =0, goal =0):
    self.children= []

#A start search 
  def Asearch(matrix[][], startPoint,EndPoint):
    startnode = Node(0,startPoint)
    startParent = 
    endnode = Node(0,end)

    openlist = []
    closedlist = []

    openlist.append(startnode)

# the start point has to be specifically a corner of the graph that is not 1 top 20 rows or bottom 20 rows
  def StartPoint()

# the end point has to be specifically a corner of the graph that is not 1 away from startpoint left-most 20 columns or right-most 20 columns
  def EndPoint()

#priority queue that contains the vertices that A* considers to expand
  def fringe(list)
#inserts vertex s with key x into the priority queue fringe
  def fring.Insert(s,x):

#Removes vertex s from the priority queue fringe
  def fring.Remove(s):

#removes a vertex with the smallest key from priority queue fringe and returns it
  def fring.Pop():
    return val

# Set of vertices that A* has expanded and ensures that A* expands every vertex at most once.
  def closedlIst():