import unittest

from Statistics.Statistics import Statistics
import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        random.seed(0)
        randomData = []
        i = 1
        while i < 90:
            randomData.append(random.randint(1, 100))
            self.testData = randomData
            self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_Mean_calculator(self):
        mean = self.statistics.mean(self, testData)
        self.assertEqual(mean, 1.5)


if __name__ == '__main__':
    unittest.main()
