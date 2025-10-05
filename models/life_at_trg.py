import json
import re

class LifeAtTrg:
    def __init__(self, page):
        self.page = page
        self.core_values_section = page.locator('#comp-lopj2yq04')
        self.core_values_title = self.core_values_section.locator('h5')
        self.core_values_description = self.core_values_section.locator('p')
        self.core_values_images = self.core_values_section.locator('img')

    def getCoreValues(self):
        titles = self.core_values_title.all_text_contents()
        descriptions = self.core_values_description.all_text_contents()
        return titles, descriptions

    def getExclamationsCount(self):
        titles, descriptions = self.getCoreValues()
        return sum(exclamation.count("!") for exclamation in (titles + descriptions))

    def saveCoreValuesToJson(self, titles, descriptions):
        core_values = [{"headline": t, "description": d} for t, d in zip(titles, descriptions)]
        with open("data/core_values.json", "w", encoding="utf-8") as f:
            json.dump(core_values, f, indent=4, ensure_ascii=False)

    def downloadCoreValuesImages(self, titles, page):
        images = self.core_values_images
        for i in range(images.count()):
            img_src = images.nth(i).get_attribute("src")
            headline = titles[i].replace(" ", "_")
            headline = re.sub(r"[^\w_]", "", headline)
            file_path = f"data/images/{headline}.png"

            # Download image
            content = page.request.get(img_src)
            with open(file_path, "wb") as f:
                f.write(content.body())