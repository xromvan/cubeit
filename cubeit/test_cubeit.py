from playwright.sync_api import Page, expect
import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "http://localhost:8001/"
def test_cube_it(page: Page):
    """Test the CubeIt app."""
    # Open the CubeIt app
    page.goto(BASE_URL)
    # Wait for the app to load
    input_field = page.locator("input[type='number']") 
    input_field.fill("10")

    cube_button = page.locator("button:has-text('Cube')")
    cube_button.click()

    result = page.locator("p#result")
    # Wait for the result to be displayed   

    expect(result).to_contain_text("1000")


def test_cubeit_invalid_input(page: Page):
    """Test the CubeIt app with invalid input."""
    # Open the CubeIt app
    page.goto(BASE_URL)
    # Wait for the app to load
    input_field = page.locator("input[type='number']") 
    input_field.fill("")

    cube_button = page.locator("button:has-text('Cube')")
    cube_button.click()

    result = page.locator("p#result")
    # Wait for the result to be displayed   
    expect(result).to_contain_text("Enter something!")   
