# -*- coding: utf-8 -*-
""" Playwright サンプル"""
import re
import pytest
from playwright.sync_api import Page, expect

def test_playwright(page: Page):
    print("Playwright test is running", flush=True)
    page.goto("http://127.0.0.1:8000/")
    # expect(page).to_have_title(re.compile("FastAPI"))
    page.screenshot(path="screenshot.png")
    assert page.get_by_text('{"Path":"root"}').is_visible(), "Expected text not found on the page"
