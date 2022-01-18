import unittest
import src.parser as parser


class TestParser(unittest.TestCase):
    def test_parser_init(self):
        p = parser.Parser()
        p.portfolio_data
