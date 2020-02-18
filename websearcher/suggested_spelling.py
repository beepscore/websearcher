#!/usr/bin/env python3

from bs4 import BeautifulSoup

from websearcher import browser_driver
# from websearcher import top_hit


def suggested_spelling(search_string):
    """
    Use browser to search for a term and return suggested spelling

    Parameters
    ----------
    search_string : String
        string to search for

    Returns
    -------
    "Showing results for" value if present
    else "Did you mean:" value if present
    else empty string
    """
    html = browser_driver.taw_html(search_string)

    taw_soup = BeautifulSoup(html, 'html.parser')

    showing_results_for = spelling_showing_results_for(taw_soup)
    if showing_results_for is not None:
        print("returning showing_results_for {0}".format(showing_results_for))
        return showing_results_for

    did_you_mean = spelling_did_you_mean(taw_soup)
    if did_you_mean is not None:
        print("returning did_you_mean {0}".format(did_you_mean))
        return did_you_mean

    # if word was spelled correctly, page will contain a line similar to
    # About 537, 000, 000 results(0.61 seconds)
    # ignore this

    # hit = top_hit.top_hit(search_string)
    # if hit is not None:
    #     print("returning top_hit")
    #     return hit

    print("returning empty string")
    return ""


def spelling_showing_results_for(taw_soup):
    """ If argument contains "Showing results for" or "including results for". returns the proposed search term
    Parameters
    ----------
    taw_soup : beautiful soup object
        A partially parsed Google search response

    Returns
    -------
    string if found, else return None
    """

    fprsl = taw_soup.find(id='fprsl')
    fprsl_b_i_string = fprsl.b.i.string

    if len(fprsl_b_i_string) == 0:
        return None
    else:
        return fprsl_b_i_string


def spelling_did_you_mean(taw_soup):
    """ If argument contains "Did you mean:" returns the proposed search term

    Example
    -------
    search javascwipt
    google returns "did you mean" with "a" tag and class spell

    <p class="ssp card-section">
    <span class="spell _uwb">Did you mean:</span>
    <a class="spell" href="/search?biw=1191&amp;bih=210&amp;q=javascwipt&amp;spell=1&amp;sa=X&amp;ved=0ahUKEwjXnPHU7Y7NAhUI0GMKHXERDJQQBQgZKAA">
    <b>
    <i>javascript</i></b>
    </a>

    Parameters
    ----------
    taw_soup : beautiful soup object
        A partially parsed Google search response

    Returns
    -------
    string if found, else return None
    """

    # https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class
    ssp_card_section_list = taw_soup.select("p.ssp.card-section")

    if len(ssp_card_section_list) == 0:
        return None
    else:
        ssp_card_section = ssp_card_section_list[0]
        # print(ssp_card_section.prettify())

        # e.g. <b><i>javascwipt</i></b>
        spell_elem = ssp_card_section.select("a.spell")[0]

        # e.g. javascript
        return spell_elem.i.contents[0]
