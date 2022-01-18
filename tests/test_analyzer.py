import unittest
import src.parser as parser
import src.analyzer as analyzer


class TestParser(unittest.TestCase):
    def test_parser_init(self):
        p = parser.Parser()
        a = analyzer.Analyzer(p.portfolio_data)
        a.analyze()
