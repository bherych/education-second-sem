import unittest
import os

from src.solver import solve_govern

class TestGovern(unittest.TestCase):
    def setUp(self):
        self.input_file = "govern.in"
        self.output_file = "govern.out"

    def tearDown(self):
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def write_input(self, lines):
        with open(self.input_file, 'w') as f:
            for line in lines:
                f.write(line + '\n')

    def read_output(self):
        with open(self.output_file, 'r') as f:
            return [line.strip() for line in f.readlines()]

    def test_simple(self):
        self.write_input([
            "visa foreignpassport"
        ])
        solve_govern()
        output = self.read_output()
        self.assertEqual(output, ['foreignpassport', 'visa'])

    def test_example(self):
        self.write_input([
            "visa foreignpassport",
            "visa hotel",
            "visa bankstatement",
            "bankstatement nationalpassport",
            "hotel creditcard",
            "creditcard nationalpassport",
            "nationalpassport birthcertificate",
            "foreignpassport nationalpassport",
            "foreignpassport militarycertificate",
            "militarycertificate nationalpassport"
        ])
        solve_govern()
        output = self.read_output()
        self.assertTrue(output.index("birthcertificate") < output.index("nationalpassport"))
        self.assertTrue(output.index("nationalpassport") < output.index("militarycertificate"))
        self.assertTrue(output.index("militarycertificate") < output.index("foreignpassport"))
        self.assertTrue(output.index("foreignpassport") < output.index("visa"))

if __name__ == '__main__':
    unittest.main()
