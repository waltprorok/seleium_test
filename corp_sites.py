import webbrowser

urls = [
    "https://www.ticketsatwork.local/tickets/index.php",
    "https://memberdeals.local/aaa/?login=tripleaaa",
    "https://www.plumbenefits.local/",
    "https://sams.samsclub.com/",
    "https://www.workingadvantage.local/",
    "https://test.ticketmonster.com/"
]


def start_browser():
    for url in urls:
        webbrowser.open(url, new=2)


if __name__ == "__main__":
    start_browser()
