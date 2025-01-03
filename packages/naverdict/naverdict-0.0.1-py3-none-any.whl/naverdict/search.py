from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from naverdict.constants import NAVER_ENDIC_URL
from naverdict.exceptions import NaverDictConnectionError


def search(search_word: str, headless: bool = True) -> list[str]:
    """Search Naver Dictionary for all the 'Meanings'

    Args:
        search_word (str): the single word in Korean or English
        headless (bool, optional): Don't show the Webdriver window opening. Defaults to True.

    Returns:
        list[str]: all the meanings the word can have.
    """
    naver_endic_url = insert_search_word(search_word)
    response = webdriver_response_naver_endic_url(naver_endic_url, headless=headless)
    word_meaning = get_word_translation(response)

    return word_meaning


def insert_search_word(search_word: str) -> str:
    """Insert the search word into the endic URL.

    Args:
        search_word (str): the search word

    Returns:
        str: the url with the search word in it.
    """
    naver_endic_url = NAVER_ENDIC_URL.format(
        search_word=search_word,
    )
    return naver_endic_url


def webdriver_response_naver_endic_url(
    naver_endic_url: str, headless: bool = True
) -> str:
    """Get the Naver Dictionary response based on your chosen word.

    Args:
        naver_endic_url (str): the specific url for the chosen word.
        headless (bool, optional): Don't show the Webdriver window opening. Defaults to True.

    Raises:
        NaverdicConnectionError: Show this error if something goes wrong.

    Returns:
        str: the whole unfiltered response from Naver Dictionary
    """
    # Set up the Chrome browser in headless mode
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")

    # Install and set up ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(naver_endic_url)

        # wait for element to appear instead of doing a static sleep
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#searchPage_mean > div > div > div.origin > a")
            )
        )

        # Get the rendered HTML
        return driver.page_source
    except Exception:
        raise NaverDictConnectionError()
    finally:
        driver.quit()


def get_word_translation(response: str) -> list[str]:
    """Filter the response from Naver Dictionary such that we only have the meanings
    as stated in the Naver Dictionary (and not its integrations with other websites).

    Args:
        response (str): the Naver Dictionary full response

    Returns:
        list[str]: all the meanings as defined by Naver Dictionary.
    """
    soup = BeautifulSoup(response, "html.parser")

    # Get all <a> elements
    anchors = soup.select("#searchPage_mean > div > div > div.origin > a")

    results = []
    for a in anchors:
        # Remove the <sup class="num"> from each anchor
        for sup in a.find_all("sup", class_="num"):
            sup.decompose()

        # Get the remaining text
        text = a.get_text(strip=True)
        results.append(text)

    return results
