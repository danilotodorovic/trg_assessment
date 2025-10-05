class Navigation:
    def __init__(self, page):
        self.page = page
        self.home = page.locator('a[href="https://www.trgint.com/"]')
        self.who_we_are = page.locator('a[href="https://www.trgint.com/who-we-are/"]').nth(0)
        self.careers = page.locator('a[href="https://www.careers.trgint.com/"]').nth(0)
        self.life_at_trg = page.locator('a[href="https://www.careers.trgint.com/life-at-trg"]').nth(0)
