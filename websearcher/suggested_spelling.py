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

    # hit = top_hit.top_hit(search_string)
    # if hit is not None:
    #     print("returning top_hit")
    #     return hit

    print("returning empty string")
    return ""


def spelling_showing_results_for(taw_soup):
    """ If argument contains "Showing results for" or "including results for". returns the proposed search term

    Examples
    --------
    search benaz
    google response contains "including results for" with "a" tag and no class

    search javascwipt
    google response
    <p class="sp_cnt card-section">
    <span class="spell">Showing results for</span>
    <a class="spell" href="/search?/search?biw=1280&bih=423&q=javascwipt&spell=1&sa=X&ved=0ahUKEwjMyeG30oPNAhVMz2MKHRw5D10QvwUIGSgA">
    <b>
    <i>javascript</i>
    </b>
    </a>
    method returns "javascript"

    Parameters
    ----------
    taw_soup : beautiful soup object
        A partially parsed Google search response

    Returns
    -------
    string if found, else return None
    """

    # https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class
    sp_cnt_card_section_list = taw_soup.select("p.sp_cnt.card-section")

    if len(sp_cnt_card_section_list) == 0:
        return None
    else:
        sp_cnt_card_section = sp_cnt_card_section_list[0]
        # print(sp_cnt_card_section.prettify())

        # e.g. <b><i>javascwipt</i></b>
        spell_elem = sp_cnt_card_section.select("a")[0]

        # e.g. javascript
        return spell_elem.i.contents[0]


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
