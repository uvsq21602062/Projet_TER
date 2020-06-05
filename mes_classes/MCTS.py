
from random import *
import copy
import random
import math




class Node():
	profondeurAParcourir = 10 # 5 etape pour chaque joueur
	constanceC=math.sqrt(2.0)

	def __init__(self, parent=None, nbTour=profondeurAParcourir):
		self.value=0
		self.nbTour=0
		self.visits=1
		self.children=[]
		self.parent=parent

	def next_node(self): 
		"faire une etape aleatoir pour le joueur"	###############################

		next=Node(self, self.nbTour-1)		# son parent et le noeud lui meme, et le nb de tour est nbTour-1
		return next


	def add_child(self,newChild):
		child=Node(self, profondeurAParcourir) #parent , profondeur
		self.children.append(child)
`

	def terminal(self):					
		if self.nbTour == 0:
			return True
		return False

	def getValue(self):
		r=0
		"r = calculer la valeur jusqu'a ce noeud" ############################
		return r



def ConstruirArbre(nb_essaye,root):					# a chaque tour du jeu, on verifie "nb_essaye" choix possibles, et pour chacun on verifie jusqu'a la fin du jeu
	for iter in range(int(nb_essaye)):
		head=Selection(root)
		value=Simulation(head)
		BackPropagation(head,value)
	
	return MeilleurChoix(root,0)




def Selection(node):

	while node.terminal()==False:
		
		if len(node.children)==0:					# la premier tour 
			return Expantion(node)
		
		elif random.uniform(0,1)<.5:				# soit continue a verifier les fils de ce noeud, 
			node=MeilleurChoix(node,constanceC)
		
		else:
			return Expantion(node)					# soit verifie les autres noeuds
	return node



def Expantion(node):		# choisir le prochain tour aleatoirement
	next_move=node.next_node()
	node.add_child(next_move)
	return node.children[-1]


def Simulation(state):
	while state.terminal()==False:
		state=state.next_node()
	return state.getValue()


def MeilleurChoix(node,constanceC):
	bestScore=0.0
	bestMove=None #Node
	
	for child in node.children:
		score= (child.value/child.visits) + constanceC*math.sqrt(math.log(node.visits)/float(c.visits))
		if score>bestScore:
			bestMove=child
			bestScore=score

	if bestScore > 0:
		return bestMove
	return next_node			# pas de noeud optimal


def BackPropagation(node,value):
	while node!=None:		# jusqu'a la racine de l'arbre
		node.visits+=1
		node.value+=value
		node=node.parent
	return

