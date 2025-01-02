from typing import Union

from parselite import parse

from .searcher import RealTimeGoogleSearchProvider

import sys


def check_os_sys():
    if sys.platform.startswith('win'):
        return "Windows"
    elif sys.platform.startswith('linux'):
        return "Linux"
    else:
        return "Other OS"


def bing(query: list | str, max_urls=50, animation=False,
         chromedriver_path=None,
         search_provider="bing"):
    return google(
        query=query,
        max_urls=max_urls,
        animation=animation,
        chromedriver_path=chromedriver_path,
        search_provider=search_provider
    )


def google(query: list | str, max_urls=50, animation=False,
           chromedriver_path=None,
           search_provider="google"):
    if chromedriver_path is None:
        cur_sys = check_os_sys()
        chromedriver_path = "/usr/local/bin/chromedriver" if cur_sys == 'Linux' else r"C:\Users\chromedriver-win64\chromedriver.exe"

    search = RealTimeGoogleSearchProvider(animation=animation,
                                          chromedriver_path=chromedriver_path,
                                          search_provider=search_provider
                                          )

    if isinstance(query, list):
        import threading
        results = []

        def search_query(q):
            results.append(search.search(q, max_urls=max_urls))

        threads = [threading.Thread(target=search_query, args=(q,)) for q in query]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        return results
    else:
        return search.search(query, max_urls=max_urls)


def browse(query: list | str, max_urls=50, animation=False,
           chromedriver_path=None,
           search_provider="google", return_urls: Union[int, bool] = False):
    urls = google(
        query=query,
        max_urls=max_urls,
        animation=animation,
        chromedriver_path=chromedriver_path,
        search_provider=search_provider
    )
    if return_urls:
        return urls if isinstance(return_urls, bool) else urls[:return_urls]
    return urls[0] if urls else ""


def web(query: list | str, k: int = 1, max_urls=50, animation=False,
        chromedriver_path=None,
        search_provider="google", return_tags: Union[int, bool] = False, ):
    urls = google(
        query=query,
        max_urls=max_urls,
        animation=animation,
        chromedriver_path=chromedriver_path,
        search_provider=search_provider
    )
    contents = parse(urls=urls)
    contents = [c for c in contents if c.content]
    contents = contents[:k]

    if return_tags:
        text = "".join([(f"<URL_START>{c.url}<URL_END>"
                         f"<CONTENT_START>{c.content}<CONTENT_END>") for c in contents])
    else:
        text = "\n".join([c.content for c in contents])
    return text

# def google(query,max_urls=50,animation=False,
#            chromedriver_path=None):
#     if chromedriver_path is None:
#         cur_sys = check_os_sys()
#         chromedriver_path = "/usr/local/bin/chromedriver" if cur_sys == 'Linux' else r"C:\Users\chromedriver-win64\chromedriver.exe"
#
#     search = RealTimeGoogleSearchProvider(animation=animation,
#                                           chromedriver_path=chromedriver_path)
#     return search.search(query,max_urls=max_urls)
#
#
# def bing(query,max_urls=50,animation=False,
#          chromedriver_path=None):
#     if chromedriver_path is None:
#         cur_sys = check_os_sys()
#         chromedriver_path = "/usr/local/bin/chromedriver" if cur_sys=='Linux' else r"C:\Users\chromedriver-win64\chromedriver.exe"
#     search = RealTimeGoogleSearchProvider(search_provider="bing",
#                                           animation=animation,
#                                           chromedriver_path=chromedriver_path)
#     return search.search(query, max_urls=max_urls)
