from pydantic import BaseModel
import math 

class Vector2D(BaseModel):
    ''' 2D-Vektor mit Gleitkommazahlen
    '''
    x: float
    y: float

    @staticmethod
    def init_zero():
        ''' Erzeugt einen 0-Vektor
        '''
        return Vector2D(
            x=0,
            y=0,
        )

    @staticmethod
    def init_coordinates(x, y):
        ''' Erzeugt einen Vektor mit den gegebenen Koordinaten x und y
        '''
        return Vector2D(x=x, y=y)
    
    def scalar_mul(self, scalar):
        ''' Skalar-Multiplikation
        '''
        return Vector2D(
            x=self.x * scalar,
            y=self.y * scalar,
        )

    def scalar_product(self, other) -> float:
        ''' Skalarprodukt
        '''
        return self.x * other.x + self.y * other.y
    
    def vector_add(self, other):
        ''' Vektor-Addition
        '''
        return Vector2D(
            x=self.x + other.x,
            y=self.y + other.y,
        )
    
    def vector_sub(self, other):
        ''' Vektor-Subtraktion
        '''
        return Vector2D(
            x=self.x - other.x,
            y=self.y - other.y,
        )
    
    def negotation(self):
        ''' Negation
        '''
        return Vector2D(
            x=-self.x,
            y=-self.y,
        )
    
    def length(self) -> float:
        ''' Länge des Vektors
        '''
        return math.sqrt(self.x**2 + self.y**2)

    def equal(self, other) -> bool:
        ''' Gleichheit zweier Vektoren
        '''
        return self.x == other.x and self.y == other.y

    def perpendicular(self):
        ''' Senkrechter Vektor
        '''
        return Vector2D(
            x=-self.y,
            y=self.x,
        )
    
    def calculate_angle(self, other) -> float:
        ''' Winkel zwischen zwei Vektoren
        '''
        return math.acos(self.scalar_product(other) / (self.length() * other.length()))
