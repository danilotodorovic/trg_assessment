class BasePage:
    def __init__(self, page):
        self.page = page

    def clickOnElement(self, element):
        element.click()

    def hoverOverElement(self, element):
        element.hover()

    def visitPage(self, url):
        self.page.goto(url, wait_until="networkidle")