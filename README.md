# Optical-Chemical-Structure-Recognition
PHASES OF RECOGNITION
  Node Recognition - identifies regions of interest, line interesects, letters, etc. that correspond to atoms
  
  Node Identificiation - classifies the interest regions as C, N, O, NH3, etc.

  Bond Recognition - Determines what nodes are connected to what other nodes
  
  Bond Identification - classifies the bond as single, double, triple, wedged, or dashed
  
  

# Program Files Annotations

Chemical Strucutre Recogniton - master script that calls each module.
	
	imput prompt
	class creation
	output formating

Module 0 - [any image - standard format image] 

	Image resizing/ padding 
	Image preprocessing 

Module 1 - [Image -> list of node class] 

	Corner detection 
	Clustering 
	Class creation 

Module 2 - [list of nodes -> list of nodes with identification] 

	[Node classification] 

Module 3- [list of nodes + image -> list of connected nodes] 

	Edge detection 
	Bonding algorithm 

Module 4- [list of connected nodes -> list of connected nodes with identified edges] 

	[Edge classification] 

Module 5- [completed list -> SMILES string] 

	[Convert to SMILES] 
	[Check answer] 
