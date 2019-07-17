import webbrowser

urls = [
    "https://www.ticketsatwork.local/tickets/index.php",
    "https://www.plumbenefits.local/",
    "https://www.workingadvantage.local/",
    "https://memberdeals.local/nycgov/index.php",
    "https://sams.samsclub.com/",
]


def start_browser():
    for url in urls:
        webbrowser.open(url, new=2)


if __name__ == "__main__":
    start_browser()
