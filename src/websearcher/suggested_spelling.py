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
    if fprsl is None:
        return None

    fprsl_b_i_string = fprsl.b.i.string

    if len(fprsl_b_i_string) == 0:
        return None
    else:
        return fprsl_b_i_string


def spelling_did_you_mean(taw_soup):
    """ If argument contains "Did you mean:" returns the proposed search term

    Example
    -------
    search swoft
    google returns "did you mean" and "swift"

    Parameters
    ----------
    taw_soup : beautiful soup object
        A partially parsed Google search response

    Returns
    -------
    string if found, else return None
    """
    taw_soup_a = taw_soup.a
    if taw_soup_a is None:
        return None

    taw_soup_a_b = taw_soup_a.b
    if taw_soup_a_b is None:
        return None

    taw_soup_a_b_i = taw_soup_a_b.i

    taw_soup_a_b_i_string = taw_soup_a_b_i.string

    if len(taw_soup_a_b_i_string) == 0:
        return None
    else:
        return taw_soup_a_b_i_string


if __name__ == "__main__":

    result = suggested_spelling("omplain")
    print(result)
