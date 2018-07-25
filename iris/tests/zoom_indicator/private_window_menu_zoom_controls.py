# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from iris.test_case import *


class Test(BaseTest):

    def __init__(self, app):
        BaseTest.__init__(self, app)
        self.meta = 'This is a test case that checks the zoom level in private window when applying the Firefox Menu ' \
                    'Zoom Controls.'

    def run(self):
        url = LocalWeb.FIREFOX_TEST_SITE
        url_bar_default_zoom_level = 'url_bar_default_zoom_level.png'
        url_bar_90_zoom_level = 'url_bar_90_zoom_level.png'
        url_bar_110_zoom_level = 'url_bar_110_zoom_level.png'
        zoom_control_toolbar_increase = 'zoom_control_toolbar_increase.png'
        zoom_control_toolbar_decrease = 'zoom_control_toolbar_decrease.png'
        hamburger_menu = 'hamburger_menu.png'

        new_private_window()

        navigate(url)

        expected = exists(LocalWeb.FIREFOX_LOGO, 10)
        assert_true(self, expected, 'Page successfully loaded, firefox logo found.')

        region = create_region_for_url_bar()

        expected = region.exists(url_bar_default_zoom_level, 10)
        assert_true(self, expected, 'Zoom level not displayed by default in the url bar.')

        new_region = create_region_for_hamburger_menu()

        expected = new_region.exists('100%', 10)
        assert_true(self, expected, 'Zoom level is 100% by default in hamburger menu.')

        click(zoom_control_toolbar_increase)

        new_reg = create_region_for_url_bar()

        expected = new_region.exists('110%', 10)
        assert_true(self, expected, 'Zoom level successfully increased in hamburger menu.')

        # Click the hamburger menu to close it.
        click(hamburger_menu)

        expected = new_reg.exists(url_bar_110_zoom_level, 10)
        assert_true(self, expected, 'Zoom level increased and correctly displayed in the url bar.')

        # Click the hamburger menu to open it.
        click(hamburger_menu)

        click(zoom_control_toolbar_decrease)
        click(zoom_control_toolbar_decrease)

        expected = new_region.exists('90%', 10)
        assert_true(self, expected, 'Zoom level successfully increased in hamburger menu.')

        # Click the hamburger menu to close it.
        click(hamburger_menu)

        expected = new_reg.exists(url_bar_90_zoom_level, 10)
        assert_true(self, expected, 'Zoom level decreased and correctly displayed in the url bar.')
