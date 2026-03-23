'''
Han Pate
CSCI 332 Spring 2026
Programming Assignment | Convex Hull Jarvis
I acknowledge that I have worked on this assignment independently, except
where explicitly noted and referenced. Any collaboration or use of external
resources has been properly cited. I am fully aware of the consequences of
academic dishonesty and agree to abide by the university's academic integrity
policy. I understand the importance the consequences of plagiarism.
'''

import unittest
from main import convex_hull_jarvis

class TestConvexHull(unittest.TestCase):
    def test_class_example(self): #testing the class example
        points = [(0,3), (2,2), (1,1), (2,1), (3,0), (0,0), (3,3)]
        result = convex_hull_jarvis(points)
        self.assertEqual(result, [(0, 0), (0, 3), (3, 3), (3, 0)])
    def test_triangle(self):
        points = [(0, 0), (1, 2), (2, 0)]
        result = convex_hull_jarvis(points)
        self.assertEqual(result, [(0, 0), (1, 2), (2, 0)])
    def test_interior_points(self):
        points = [(0, 0), (0, 3), (3, 3), (3, 0), (1, 1)]
        result = convex_hull_jarvis(points)
        self.assertEqual(result,[(0, 0), (0, 3), (3, 3), (3, 0)])
    def test_not_enough(self):
        points = [(0, 0), (1, 1)]
        result = convex_hull_jarvis(points)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
