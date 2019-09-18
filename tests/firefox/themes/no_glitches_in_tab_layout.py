# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from targets.firefox.fx_testcase import *


class Test(FirefoxTest):

    @pytest.mark.details(
        description='There are no glitches in tab layout.',
        locale=['en-US'],
        test_case_id='15268',
        test_suite_id='494'
    )
    def run(self, firefox):
        mozilla_tab_not_focused = Pattern('mozilla_tab_not_focused.png')
        mozilla_tab_not_focused_light_theme = Pattern('mozilla_tab_not_focused_light_theme.png')
        mozilla_hover = Pattern('mozilla_hover.png')
        mozilla_hover_dark_theme = Pattern('mozilla_hover_dark_theme.png')
        close_tab_button = Pattern('close_tab_button.png')
        close_tab_button_dark_theme = Pattern('close_tab_button_dark_theme.png')
        close_tab_hover = Pattern('close_tab_hover.png')
        close_tab_hover_dark_theme = Pattern('close_tab_hover_dark_theme.png')

        home_width, home_height = NavBar.HOME_BUTTON.get_size()
        tabs_region = Region(0, 0, Screen.SCREEN_WIDTH, home_height * 6)

        open_addons()
        previous_tab()
        close_tab()

        expected = exists(AboutAddons.THEMES, 10)
        assert expected, 'Add-ons page successfully loaded.'

        click(AboutAddons.THEMES)

        expected = exists(AboutAddons.Themes.DARK_THEME, 10)
        assert expected, 'Dark theme option found in the page.'

        expected = exists(AboutAddons.Themes.LIGHT_THEME, 10)
        assert expected, 'Light theme option found in the page.'

        expected = exists(AboutAddons.Themes.DEFAULT_THEME, 10)
        assert expected, 'Default theme option found in the page.'

        # DEFAULT theme.
        click(AboutAddons.Themes.DEFAULT_THEME)

        expected = not exists(AboutAddons.Themes.ENABLE_BUTTON, 5)
        assert expected, 'ENABLE button NOT found in the page.'

        # Open at least 10 tabs and load pages in each one.
        for i in range(10):
            new_tab()
            navigate(LocalWeb.MOZILLA_TEST_SITE)
            expected = exists(LocalWeb.MOZILLA_LOGO, 120)
            assert expected, 'Mozilla page loaded successfully.'

        max_attempts = 9

        while max_attempts > 0:
            expected = exists(mozilla_tab_not_focused, 3)

            if expected:
                inactive_tab_location = find(mozilla_tab_not_focused)

                hover(inactive_tab_location)

                expected = exists(mozilla_hover, 10, region=tabs_region)
                assert expected, 'Mozilla page is hovered.'

                click(inactive_tab_location)

                time.sleep(Settings.DEFAULT_UI_DELAY_LONG)

                expected = exists(close_tab_button, 10, region=tabs_region)
                assert expected, 'Close tab button is visible.'

                close_width, close_height = close_tab_button.get_size()

                close_tab_button_location = find(close_tab_button, tabs_region)
                close_click_location = Location(close_tab_button_location.x + close_width / 2,
                                                close_tab_button_location.y + close_width / 2)

                hover(close_click_location)

                expected = exists(close_tab_hover, 10, tabs_region)
                assert expected, 'Close button is hovered.'

                click(close_click_location)

                time.sleep(Settings.DEFAULT_UI_DELAY)

                max_attempts -= 1
            else:
                max_attempts = 0

        open_addons()
        previous_tab()
        close_tab()

        # LIGHT theme.
        expected = exists(AboutAddons.THEMES, 10)
        assert expected, 'Add-ons page is in focus.'

        navigate_back()

        expected = exists(AboutAddons.Themes.LIGHT_THEME, 10)
        assert expected, 'Light theme option found in the page.'

        click(AboutAddons.Themes.LIGHT_THEME)

        action_can_be_performed = exists(AboutAddons.Themes.ACTION_BUTTON)
        assert action_can_be_performed, 'Theme can be enabled/disabled.'
        click(AboutAddons.Themes.ACTION_BUTTON)

        expected = exists(AboutAddons.Themes.ENABLE_BUTTON, 5)
        assert expected, 'ENABLE button found in the page.'

        click(AboutAddons.Themes.ENABLE_BUTTON)

        action_can_be_performed = exists(AboutAddons.Themes.ACTION_BUTTON)
        assert action_can_be_performed, 'Theme can be enabled/disabled.'
        click(AboutAddons.Themes.ACTION_BUTTON)

        expected = exists(AboutAddons.Themes.DISABLE_BUTTON, 10)
        assert expected, 'DISABLE button found in the page.'

        # Open at least 10 tabs and load pages in each one.
        for i in range(10):
            new_tab()
            navigate(LocalWeb.MOZILLA_TEST_SITE)
            expected = exists(LocalWeb.MOZILLA_LOGO, 120)
            assert expected, 'Mozilla page loaded successfully.'

        max_attempts = 9

        while max_attempts > 0:
            expected = exists(mozilla_tab_not_focused_light_theme, 3)

            if expected:
                inactive_tab_location = find(mozilla_tab_not_focused_light_theme)

                hover(inactive_tab_location)

                expected = exists(mozilla_hover, 10, region=tabs_region)
                assert expected, 'Mozilla page is hovered.'

                click(inactive_tab_location)

                time.sleep(Settings.DEFAULT_UI_DELAY_LONG)

                expected = exists(close_tab_button, 10, region=tabs_region)
                assert expected, 'Close tab button is visible.'

                close_tab_button_location = find(close_tab_button, tabs_region)

                close_width, close_height = close_tab_button.get_size()

                close_click_location = Location(close_tab_button_location.x + close_width / 2,
                                                close_tab_button_location.y + close_width / 2)

                hover(close_click_location)

                expected = exists(close_tab_hover, 10, tabs_region)
                assert expected, 'Close button is hovered.'

                click(close_click_location)

                time.sleep(Settings.DEFAULT_UI_DELAY)

                max_attempts -= 1
            else:
                max_attempts = 0

        open_addons()
        previous_tab()
        close_tab()

        # DARK theme.
        expected = exists(AboutAddons.THEMES, 10)
        assert expected, 'Add-ons page is in focus.'

        navigate_back()

        expected = exists(AboutAddons.Themes.DARK_THEME, 10)
        assert expected, 'Dark theme option found in the page.'

        click(AboutAddons.Themes.DARK_THEME)

        action_can_be_performed = exists(AboutAddons.Themes.ACTION_BUTTON)
        assert action_can_be_performed, 'Theme can be enabled/disabled.'
        click(AboutAddons.Themes.ACTION_BUTTON)

        expected = exists(AboutAddons.Themes.ENABLE_BUTTON, 10)
        assert expected, 'ENABLE button found in the page.'

        click(AboutAddons.Themes.ENABLE_BUTTON)

        action_can_be_performed = exists(AboutAddons.Themes.ACTION_BUTTON)
        assert action_can_be_performed, 'Theme can be enabled/disabled.'
        click(AboutAddons.Themes.ACTION_BUTTON)

        expected = exists(AboutAddons.Themes.DISABLE_BUTTON, 10)
        assert expected, 'DISABLE button found in the page.'

        # Open at least 10 tabs and load pages in each one.
        for i in range(10):
            new_tab()
            navigate(LocalWeb.MOZILLA_TEST_SITE)
            expected = exists(LocalWeb.MOZILLA_LOGO, 120)
            assert expected, 'Mozilla page loaded successfully.'

        max_attempts = 9

        while max_attempts > 0:
            expected = exists(mozilla_tab_not_focused, 3)

            if expected:
                inactive_tab_location = find(mozilla_tab_not_focused)

                hover(inactive_tab_location)

                expected = exists(mozilla_hover_dark_theme, 10, region=tabs_region)
                assert expected, 'Mozilla page is hovered.'

                click(inactive_tab_location)

                time.sleep(Settings.DEFAULT_UI_DELAY_LONG)

                expected = exists(close_tab_button_dark_theme, 10, region=tabs_region)
                assert expected, 'Close tab button is visible.'

                close_tab_dark_button_location = find(close_tab_button_dark_theme, tabs_region)

                close_width, close_height = close_tab_button_dark_theme.get_size()

                close_dark_click_location = Location(close_tab_dark_button_location.x + close_width / 2,
                                                     close_tab_dark_button_location.y + close_width / 2)

                hover(close_dark_click_location)

                expected = exists(close_tab_hover_dark_theme, 10, tabs_region)
                assert expected, 'Close button is hovered.'

                click(close_dark_click_location)

                time.sleep(Settings.DEFAULT_UI_DELAY)

                max_attempts -= 1
            else:
                max_attempts = 0

        close_tab()
