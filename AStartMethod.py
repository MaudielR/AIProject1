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




#A start search 
  def Asearch(matrix, startPoint,EndPoint):
    startParent = Node(0,startPoint)
    startchild.Distance = 0
    startchild.goal = 0
    startchild.cost=0 
    endnode = Node(0,end)
    end.Distance=0
    end.goal=0
    end.count = 0

    openlist = []
    closedlist = []

    openlist.append(startnode)

    #loop list until EndPoint found 
    while len(openlist) > 0:

      newcurrent = openlist[0]
      nodeindex = 0
      
      #find current node 
      for newindex, i in enumerate(openlist):
        if i.count < newcurrent.count:
          newcurrent=i
          nodeindex= newindex
      openlist.pop(nodeindex)
      closedlist.append(newcurrent)
      # if current node = endnode, path found 
      if newcurrent ==endnode: 
        Pathfound = []
        currentnode = newcurrent
        while currentnode != 0: 
          Pathfound.append(currentnode.positon)
          currentnode = currentnode.parentNode 
        #reversed path
        return Pathfound[::-1] 

    newChildren []
    #check all positons, in range, not == 1
    for allPossiblePositons in [(1,1),(-1,-1),(0,-1),(-1,0),(1,-1),(-1,1),(0,1),(1,0)]
      allPossiblePositons =(newcurrent.positon[0]+allPossiblePositons[0], newcurrent.positon[1]+ allPossiblePositons[1])
      
      #check length and -1 areas 

      nextnode = Node(newcurrent,allPossiblePositons)
      newChildren.append(nextnode)
    
    for xelems in newChildren:
      for yelems in closedlist:
        if xelems ==closedlist:
          continue
    
      xelems.Distance = newcurrent.Distance + 1
      xelems.goal =
      xelems.count
