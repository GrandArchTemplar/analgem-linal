import unittest

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


if __name__ == '__main__':
    unittest.main()
