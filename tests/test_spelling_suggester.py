#!/usr/bin/env python3

import unittest

# tried putting tests in a "test" directory at same level as websearcher
# relative import didn't work
from websearcher import spelling_suggester


class TestSpellingSuggester(unittest.TestCase):

    def setUp(self):
        pass

    # Apparently Python unittest runs tests in alphabetical order
    def test_suggested_spelling_astma(self):
        suggester = spelling_suggester.SpellingSuggester("@./websearcher_data/inputs/spelling_suggester_args.txt")
        self.assertEqual("asthma", suggester.suggested_spelling("astma"), '')

    def test_suggested_spelling_asthma(self):
        suggester = spelling_suggester.SpellingSuggester("@./websearcher_data/inputs/spelling_suggester_args.txt")
        self.assertEqual("", suggester.suggested_spelling("asthma"), '')

    def test_suggested_spellings(self):
        suggester = spelling_suggester.SpellingSuggester("@./websearcher_data/inputs/spelling_suggester_args.txt")
        actual = suggester.suggested_spellings(["astma", "asthma", "bercitis", "mildmuscle"])
        expected = ["asthma", "", "bursitis", "mild muscle"]
        self.assertEqual(expected, actual, '')

if __name__ == "__main__":
    unittest.main()
