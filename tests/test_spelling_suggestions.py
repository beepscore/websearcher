#!/usr/bin/env python3

import unittest

# tried putting tests in a "test" directory at same level as websearcher
# relative import didn't work
from websearcher import spelling_suggestions


class TestSpellingSuggester(unittest.TestCase):

    def setUp(self):
        pass

    # Apparently Python unittest runs tests in alphabetical order
    def test_suggested_spelling_pyethon(self):
        suggester = spelling_suggestions.SpellingSuggester("@./websearcher_data/inputs/spelling_suggester_args.txt")
        self.assertEqual("python", suggester.suggested_spelling("pyethon"), '')

    def test_suggested_spelling_python(self):
        suggester = spelling_suggestions.SpellingSuggester("@./websearcher_data/inputs/spelling_suggester_args.txt")
        self.assertEqual("", suggester.suggested_spelling("python"), '')

    def test_suggested_spellings(self):
        suggester = spelling_suggestions.SpellingSuggester("@./websearcher_data/inputs/spelling_suggester_args.txt")
        actual = suggester.suggested_spellings(["pyethon", "python", "javascwipt", "swoft"])
        expected = ["python", "", "javascript", "swift"]
        self.assertEqual(expected, actual, '')

if __name__ == "__main__":
    unittest.main()
