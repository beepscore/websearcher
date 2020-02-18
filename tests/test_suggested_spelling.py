#!/usr/bin/env python3

import unittest
from bs4 import BeautifulSoup
from websearcher.suggested_spelling import spelling_showing_results_for
from websearcher.suggested_spelling import spelling_did_you_mean

# tried putting tests in a "test" directory at same level as websearcher
# relative import didn't work
from websearcher import suggested_spelling


class TestSpellingSuggester(unittest.TestCase):

    def setUp(self):
        pass

    # Apparently Python unittest runs tests in alphabetical order

    # search for a word similar to "python" that google will suggest "python"
    # previously test searched for "pyethon", but now Google returns result for "pyethon"
    def test_suggested_spelling_pythan(self):
        self.assertEqual("python", suggested_spelling.suggested_spelling("pythan"), '')

    def test_suggested_spelling_python(self):
        self.assertEqual("", suggested_spelling.suggested_spelling("python"), '')

    def test_spelling_showing_results_for(self):
        # search for 'pythan'

        taw_html = """
  <div id="taw">
    <div style="padding:0 16px">
      <div class="med">
        <p class="p64x9c card-section" aria-level="3" role="heading" id="fprs"><span class="gL9Hy">Showing results for</span> <a id="fprsl" class="gL9Hy" href="/search?q=python&amp;spell=1&amp;sa=X&amp;ved=2ahUKEwjFzvyRj9rnAhUOv54KHUvnDSwQkeECKAB6BAgPECY" data-ved="2ahUKEwjFzvyRj9rnAhUOv54KHUvnDSwQkeECKAB6BAgPECY" name="fprsl"><b><i>python</i></b></a><script nonce="CAcuXfH41DpQwoWVjEfrfw==" type="text/javascript">
(function(){var q='python';var fprsl=document.getElementById('fprsl');fprsl.onclick = function(e){if(google.ac&&google.ac.ou){google.ac.ou(q);}else{document.getElementsByName('q')[0].value=q;} document.getElementById("fprs").outerHTML='';google.log('','&ved='+fprsl.dataset['ved'],'',fprsl);e.preventDefault();};})();
        </script><br>
        <span class="spell_orig">Search instead for</span> <a class="spell_orig" href="/search?q=pythan&amp;nfpr=1&amp;sa=X&amp;ved=2ahUKEwjFzvyRj9rnAhUOv54KHUvnDSwQvgUoAXoECA8QJw">pythan</a><br></p>

        <div class="card" id="msg_box" style="display:none">
          <p class="card-section w4VK3c"><span><span class="gL9Hy" id="srfm"></span>&nbsp;<a class="gL9Hy" id="srfl" name="srfl"></a><br></span><span id="sif"><span class="spell_orig" id="sifm"></span>&nbsp;<a class="spell_orig" id="sifl" name="sifl"></a><br></span></p>
        </div>
      </div>
    </div>

    <div id="tvcap"></div>
  </div>
  """
        taw_soup = BeautifulSoup(taw_html, 'html.parser')
        actual = spelling_showing_results_for(taw_soup)
        self.assertEqual('python', actual)

    def test_spelling_did_you_mean(self):
        # search for 'javascwipt'

        taw_html = """
          <div id="taw">
    <div style="padding:0 16px">
      <div class="med">
        <p class="gqLncc card-section" aria-level="3" role="heading"><span class="gL9Hy d2IKib">Did you mean:</span> <a class="gL9Hy" href="/search?q=javascript&amp;spell=1&amp;sa=X&amp;ved=2ahUKEwjpi7qApdrnAhWSFTQIHXjnAXkQBSgAegQICxAm"><b><i>javascript</i></b></a></p>

        <div class="card" id="msg_box" style="display:none">
          <p class="card-section w4VK3c"><span><span class="gL9Hy" id="srfm"></span>&nbsp;<a class="gL9Hy" id="srfl" name="srfl"></a><br></span><span id="sif"><span class="spell_orig" id="sifm"></span>&nbsp;<a class="spell_orig" id="sifl" name="sifl"></a><br></span></p>
        </div>
      </div>
    </div>

    <div id="tvcap"></div>
  </div>
  """
        taw_soup = BeautifulSoup(taw_html, 'html.parser')
        actual = spelling_did_you_mean(taw_soup)
        self.assertEqual('javascript', actual)


if __name__ == "__main__":
    unittest.main()
