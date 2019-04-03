# Optical-Chemical-Structure-Recognition
Input- hand-drawn image of molecule... Output- SMILES format molecule name

Node Recognition - identifies regions of interest, line interesects, letters, etc. that correspond to atoms
  - harris coner detection
  - agglomerative clustering ( simple )
  
Node Identificiation - classifies the interest regions as C, N, O, NH3, etc.
  - Neural Network

Bond Recognition - Determines what nodes are connected to what other nodes
  - very simple hough transform
  
Bond Identification - classifies the bond as single, double, triple, wedged, or dashed
  - histogram of oriented gradients as input to support vector machine
  
  
