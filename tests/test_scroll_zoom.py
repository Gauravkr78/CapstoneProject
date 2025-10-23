# tests/test_scroll_zoom.py

from pages.scroll_zoom_page import ScrollZoomPage


def test_scroll_and_zoom():
    """Test case for scrolling and zooming actions"""
    url = "https://automationexercise.com/"
    browser = "chrome"  # or "edge"

    page = ScrollZoomPage(browser)
    page.open_website(url)

    # Perform scrolling actions
    page.scroll_down()
    page.scroll_to_bottom()
    page.scroll_up()

    # Perform zoom actions
    page.zoom_in(150)
    page.zoom_out(80)
    page.reset_zoom()

    # Close browser
    page.close_browser()
