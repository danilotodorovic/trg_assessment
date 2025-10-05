import re
from models.navigation import Navigation
from models.base_page import BasePage
from playwright.sync_api import expect
from models.life_at_trg import LifeAtTrg
import os

def test_navigate_to_careers(page, base_url):
    # Define classes
    navigation = Navigation(page)
    base_page = BasePage(page)
    context = page.context

    # Navigate to home page and make sure we are on the correct page
    base_page.visitPage(base_url)
    expect(page).to_have_url(re.compile("trgint"))

    # Navigate to careers page by hovering over who we are and clicking on careers
    base_page.hoverOverElement(navigation.who_we_are)
    # Open new page and make sure we are on the correct page
    with context.expect_page() as new_page_info:
        base_page.clickOnElement(navigation.careers)
    new_page = new_page_info.value
    expect(new_page).to_have_url(re.compile("careers.trgint"))

    # Define classes for new page
    navigation_careers = Navigation(new_page)
    life_at_trg = LifeAtTrg(new_page)

    # Navigate to life at trg page and make sure we are on the correct page
    navigation_careers.life_at_trg.click()
    expect(new_page).to_have_url(re.compile("life-at-trg"))

    # Scroll to section
    core_section = life_at_trg.core_values_section
    core_section.scroll_into_view_if_needed()

    # Get all headline and description from core values section
    titles, descriptions = life_at_trg.getCoreValues()

    # Number of ! characters
    exclamations_count = life_at_trg.getExclamationsCount()
    assert exclamations_count == 2
    
    # Create data folder if it doesn't exist for images and core_values.json
    os.makedirs("data/images", exist_ok=True)

    # Save core values to JSON
    life_at_trg.saveCoreValuesToJson(titles, descriptions)

    # Download images
    life_at_trg.downloadCoreValuesImages(titles, new_page)