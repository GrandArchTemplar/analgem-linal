import unittest

from SquareMatrix import SquareMatrix
from MyMatrix import MyMatrix


class TestSumMatrix(unittest.TestCase):
    def assertMatrixEqual(self, first: MyMatrix, second: MyMatrix):
        self.assertEqual(second.size(), first.size())
        for i in range(len(first[0])):
            for j in range(len(first[1])):
                self.assertAlmostEqual(first[i][j], second[i][j])

    def testSimple(self):
        m1 = MyMatrix([[2, 5], [7, -3]])
        m2 = MyMatrix([[-3, 4], [8, 5]])
        ans = MyMatrix([[-1, 9], [15, 2]])
        self.assertMatrixEqual(ans, m1 + m2)


class TestMulMatrix(unittest.TestCase):
    def assertMatrixEqual(self, first: MyMatrix, second: MyMatrix):
        self.assertEqual(second.size(), first.size())
        for i in range(len(first[0])):
            for j in range(len(first[1])):
                self.assertAlmostEqual(first[i][j], second[i][j])

    def testSimple(self):
        m1 = MyMatrix([[2, 5], [7, -3]])
        m2 = MyMatrix([[-3, 4], [8, 5]])
        ans = MyMatrix([[34, 33], [-45, 13]])
        self.assertMatrixEqual(ans, m1 * m2)


class TestDetMatrix(unittest.TestCase):
    def testSimple(self):
        m1 = MyMatrix([[3, 5, 7, 8], [-1, 7, 0, 1], [0, 5, 3, 2], [1, -1, 7, 4]])
        self.assertEqual(122, m1.det())


class TestTransformMatrix(unittest.TestCase):
    def assertMatrixEqual(self, first: MyMatrix, second: MyMatrix):
        self.assertEqual(second.size(), first.size())
        for i in range(len(first[0])):
            for j in range(len(first[1])):
                self.assertAlmostEqual(first[i][j], second[i][j])

    def testSimple(self):
        m1 = MyMatrix([[2, 5, 4], [7, -3, 9]])
        ans = MyMatrix([[2, 7], [5, -3], [4, 9]])
        self.assertMatrixEqual(ans, m1.transpose())


class TestInvMatrix(unittest.TestCase):
    def assertMatrixEqual(self, first: MyMatrix, second: MyMatrix):
        self.assertEqual(second.size(), first.size())
        for i in range(len(first[0])):
            for j in range(len(first[1])):
                self.assertAlmostEqual(first[i][j], second[i][j])

    def testSimple(self):
        m1 = MyMatrix([[2, 3], [-1, 1]])
        ans = MyMatrix([[0.2, -0.6], [0.2, 0.4]])
        self.assertMatrixEqual(ans, m1.inv())


class TestCharacteristicPolynomialMatrix(unittest.TestCase):

    def testSimple(self):
        m1 = SquareMatrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        ans = [1, -3, 3, -1]
        self.assertListEqual(ans, m1.char_polynom().pl)

    def testTeach(self):
        m1 = SquareMatrix([[2, 2, 8],
                           [3, 2, 2],
                           [1, 0, 2]])
        ans = [-16, 2, 6, -1]
        self.assertListEqual(ans, m1.char_polynom().pl)


if __name__ == '__main__':
    unittest.main()
