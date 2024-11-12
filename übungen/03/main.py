from matrix33d import Matrix33D
from vector2d import Vector2D
from rich import print

def test_matrix():
    print(
        'Test Matrix-Multiplikation',
        Matrix33D.init_values(
            a11=1, a12=2, a13=0,
            a21=4, a22=3, a23=1,
            a31=-1, a32=-5, a33=1,
        ).matrix_mul(
            other=Matrix33D.init_identity(),
        )
    )

def task_2_a():
    rotation_matrix = Matrix33D.init_rotation_x(
        angle=30,
    )

    translation_matrix = Matrix33D.init_translation(
        dx=-5,
        dy=-3,
    )

    print(
        'Aufgabe 2 a)',
        translation_matrix.matrix_mul(
            other=rotation_matrix,
        ),
    )

def task_2_b():
    rotation_matrix = Matrix33D.init_rotation_x(
        angle=30,
    )

    translation_matrix = Matrix33D.init_translation(
        dx=-5,
        dy=-3,
    )

    point = Vector2D(
        x=3,
        y=2,
    )

    import math

    print(
        'Aufgabe 2 b)',
        translation_matrix.matrix_mul(
            other=rotation_matrix,
        ).vector_mul(
            vector=point,
        ),
    )

if __name__ == "__main__":
    test_matrix()
    task_2_a()
    task_2_b()
