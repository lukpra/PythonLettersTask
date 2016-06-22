from task import rewrite
import unittest

INPUT_FILE = "in.txt"
PANT_FILE = "pant.txt"
OUTPUT_FILE = "out.txt"

class KnownValues(unittest.TestCase):

    known_values = (("", "[]"),
                    ("L", "L[1]"),
                    ("Li", "Li[1, 2]"),
                    ("lI", "Li[1, 2]"),
                    ("LI", "Li[1, 2]"),
                    ("jadę na euro!", "jadę na euro![9, 20, 38, 52, 0, 14, 34, 0, 27, 110, 39, 5, 6]"),
                    ("Python", "python[118, 12, 3, 604, 5, 14]"),
                    ("ooooo", "oOooo[5, 8, 15, 18, 40]"),
                    ("ABCDEFGH", "abcdeFgh[20, 58, 10, 38, 27, 736, 67, 604]"),
                    ("aBCDefGh", "abcdeFgh[20, 58, 10, 38, 27, 736, 67, 604]"),
                    ("ABcdEFGH", "abcdeFgh[20, 58, 10, 38, 27, 736, 67, 604]")
                    )
    error_code_one = ["xyz",
                      "xxxxyyyz",
                      "xyyyzzzzyyy",
                      "zzyyyxx",
                      "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                      +"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                      +"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                      +"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                      +"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                      +"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                      +"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                      +"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                      +"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                      +"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                      +"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                      +"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                      +"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                      +"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                      +"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                      +"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                      ]


    def test_rewrite_known_values(self):
        self.test_rewrite_sys_exit()
        for input_string, output_string in self.known_values:
            self.prepare_in(input_string)
            rewrite(['', INPUT_FILE, PANT_FILE])  # first argument is file name of the script, we can skip it
            result = self.get_result()
            self.assertEqual(output_string, result)

    def prepare_in(self, input_string):
        with open(INPUT_FILE, mode='w', encoding='utf-8') as input_file:
            input_file.write(input_string)

    def get_result(self):
        with open(OUTPUT_FILE, mode='r', encoding='utf-8') as output_file:
            output_from_file = output_file.read().replace('\n', '')  # there are two empty lines between string and array
        return output_from_file


    def test_rewrite_sys_exit(self):
        for error_code_string in self.error_code_one:
            self.prepare_in(error_code_string)
            with self.assertRaises(SystemExit) as exit_output:
                rewrite(['', INPUT_FILE, PANT_FILE])
            self.assertEqual(exit_output.exception.code, 1)

if __name__ == '__main__':
    unittest.main()