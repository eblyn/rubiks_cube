from copy import deepcopy

from constants import *


class RubiksCube:

    '''
    A class to represent a Rubik's Cube.
    The initial state of the cube is solved.
    The cube is represented as a list of the 6 faces.
    Each face is represented as a list of 9 colors.
    The colors are defined in the order of the faces, following the position of the center of the face.
    {'U': 'Up', 'B': 'Back', 'L': 'Left', 'F': 'Front', 'R': 'Right', 'D': 'Down'}
    '''
    def __init__(self, colors=COLORS):
        '''
        Initializes the cube.
        '''
        self.cube = [[i]*9 for i in range(6)]
        self.colors = colors

    def rotate(self, face, direction):
        '''
        Rotates the face in the given direction.
        face: 'U', 'B', 'L', 'F', 'R', 'D'
        direction: 'CW', 'CCW'
        '''
        self._rotate_face(face, direction)
        self._rotate_side(face, direction)
        
    def _rotate_face(self, face, direction):
        '''
        Rotates the face in the given direction.
        '''
        face_index = self._get_face_index(face)
        self.cube[face_index] = [self.cube[face_index][i] for i in ROTATE_FACE[direction]]

    def _rotate_side(self, face, direction):
        '''
        Rotates the side of the face clockwise.
        '''
        sides = SIDES[face]
        face_sides = sides.keys() if direction == 'CW' else reversed(sides.keys())
        face_sides = list(face_sides)
        cube = deepcopy(self.cube)
        for i in range(len(face_sides)):
            face_side = face_sides[i]
            side_index = self._get_face_index(face_side)
            next_face = face_sides[(i+1)%len(face_sides)]
            next_side_index = self._get_face_index(next_face)
            for j in range(3):
                self.cube[side_index][sides[face_side][j]] = cube[next_side_index][sides[next_face][j]]
        
    def _get_face_index(self, face):
        '''
        Returns the index of the face.
        '''
        return FACES.index(face)

    def print(self):
        for i in range(3):
            print(' '*12, end='')
            self._print_row(i, 0)
            print()
        for i in range(3):
            for f in [1, 2, 3, 4]:
                self._print_row(i, f)
            print()
        for i in range(3):
            print(' '*12, end='')
            self._print_row(i, 5)
            print()
        
    def _print_row(self, i, face):
        for j in range(3):
            # print(i*3+j, end=' ')
            print(self.colors[self.cube[face][i*3+j]][0], end=' ')



cube = RubiksCube()
cube.rotate('D', 'CW')
cube.rotate('R', 'CW')

cube.print()