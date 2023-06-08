import numpy as np
import glob
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.kernel_ridge import KernelRidge

#faire un fichier utils.py pour trier les données : ordre croissant des coordonnées x

class Atom:
    def __init__(self, name, x, y, z):
        self.name = name
        self.x = x
        self.y = y
        self.z = z

class Molecule:
    def __init__(self):
        self.atoms = []

    def add_atom(self, atom):
        self.atoms.append(atom)

    def get_num_atoms(self):
        return len(self.atoms)

    def print_atoms(self):
        for atom in self.atoms:
            print("Atom:", atom.name)
            print("Position (x, y, z):", atom.x, atom.y, atom.z)
            
    def sort_atoms(self):
        self.atoms.sort(key=lambda atom: (atom.x, atom.y, atom.z))
    
    def Translational_symmetry(self,b):
        for atom in self.atoms:
            atom.x += b
            atom.y += b
            atom.z += b
            
    def Rotational_symmetry(self,U):
        for atom in self.atoms:
            atom.x *= U
            atom.y *= U
            atom.z *= U
            
    def Permutation_symmetry(self,sigma): #à refaire
        loc=0
        temp=self.atoms
        for Permutation in sigma:
            self.atoms[loc]=temp[Permutation]
            self.atoms[Permutation]=self.atoms[loc]
            loc+=1
            
            
            
#molecule.Translational_symmetry(2) 
#molecule.Rotational_symmetry(2)
#print('Avant permutation')
#molecule.print_atoms()
#molecule.Permutation_symmetry([3,2,1,0])
#print('Apres permutation')
#molecule.print_atoms()

# import the data from the file 'Atoms/train' 

molecule = Molecule()

molecules = [] # list of molecules

file_pattern = 'data/Atoms/train/*.xyz'
file_names = glob.glob(file_pattern)

for file_name in file_names:
    molecule = Molecule()
    
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines[2:]:  # skip the first two lines
            atom_info = line.strip().split() # remove whitespace and split on comma
            name = atom_info[0] 
            x = float(atom_info[1])
            y = float(atom_info[2])
            z = float(atom_info[3])
            atom = Atom(name, x, y, z) 
            molecule.add_atom(atom) 

    # Add the molecule to the list
    molecules.append(molecule)
    
for molecule in molecules:
    molecule.sort_atoms()
    
#molecules[0].print_atoms()
#molecules[0].atoms[0].x      # coordinate x exemple



    
    