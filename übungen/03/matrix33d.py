from pydantic import BaseModel
from vector2d import Vector2D
import math

class Matrix33D(BaseModel):
    ''' 3x3-Matrix mit Gleitkommazahlen
    '''
    a11: float
    a12: float
    a13: float
    a21: float
    a22: float
    a23: float
    a31: float
    a32: float
    a33: float

    @staticmethod
    def init_zero():
        ''' Erzeugt eine Nullmatrix
        '''
        return Matrix33D(
            a11=0, a12=0, a13=0,
            a21=0, a22=0, a23=0,
            a31=0, a32=0, a33=0,
        )
    
    @staticmethod
    def init_identity():
        ''' Erzeugt die Einheitsmatrix
        '''
        return Matrix33D(
            a11=1, a12=0, a13=0,
            a21=0, a22=1, a23=0,
            a31=0, a32=0, a33=1,
        )
    
    @staticmethod
    def init_values(a11, a12, a13, a21, a22, a23, a31, a32, a33):
        ''' Erzeugt eine Matrix mit den gegebenen Values
        '''
        return Matrix33D(
            a11=a11, a12=a12, a13=a13,
            a21=a21, a22=a22, a23=a23,
            a31=a31, a32=a32, a33=a33,
        )

    @staticmethod
    def init_rotation_x(angle):
        ''' Erzeugt eine Rotationsmatrix um die x-Achse
        '''
        return Matrix33D(
            a11=math.cos(math.radians(angle)), a12=-math.sin(math.radians(angle)), a13=0,
            a21=math.sin(math.radians(angle)), a22=math.cos(math.radians(angle)), a23=0,
            a31=0, a32=0, a33=1,
        )
    
    @staticmethod
    def init_translation(dx: float, dy: float):
        ''' Erzeugt eine Translationsmatrix
        '''
        return Matrix33D(
            a11=1, a12=0, a13=dx,
            a21=0, a22=1, a23=dy,
            a31=0, a32=0, a33=1,
        )

    def matrix_mul(self, other):
        ''' Matrix-Multiplikation
        '''
        return Matrix33D(
            a11=self.a11 * other.a11 + self.a12 * other.a21 + self.a13 * other.a31,
            a12=self.a11 * other.a12 + self.a12 * other.a22 + self.a13 * other.a32,
            a13=self.a11 * other.a13 + self.a12 * other.a23 + self.a13 * other.a33,
            a21=self.a21 * other.a11 + self.a22 * other.a21 + self.a23 * other.a31,
            a22=self.a21 * other.a12 + self.a22 * other.a22 + self.a23 * other.a32,
            a23=self.a21 * other.a13 + self.a22 * other.a23 + self.a23 * other.a33,
            a31=self.a31 * other.a11 + self.a32 * other.a21 + self.a33 * other.a31,
            a32=self.a31 * other.a12 + self.a32 * other.a22 + self.a33 * other.a32,
            a33=self.a31 * other.a13 + self.a32 * other.a23 + self.a33 * other.a33,
        )
    
    def vector_mul(self, vector: Vector2D):
        ''' Vektor-Multiplikation
        '''
        return Vector2D(
            x=self.a11 * vector.x + self.a12 * vector.y + self.a13,
            y=self.a21 * vector.x + self.a22 * vector.y + self.a23,
        )
