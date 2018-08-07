# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from iris.test_case import *


class Test(BaseTest):

    def __init__(self, app):
        BaseTest.__init__(self, app)
        self.meta = 'This test case checks that one-off searches are displayed in the awesome bar.'

    def run(self):
        url = LocalWeb.FIREFOX_TEST_SITE
        search_settings = 'search_settings.png'
        amazon_one_off_button = 'amazon_one_off_button.png'
        bing_one_off_button = 'bing_one_off_button.png'
        duck_duck_go_one_off_button = 'duck_duck_go_one_off_button.png'
        ebay_one_off_button = 'ebay_one_off_button.png'
        google_one_off_button = 'google_one_off_button.png'
        twitter_one_off_button = 'twitter_one_off_button.png'
        wikipedia_one_off_button = 'wikipedia_one_off_button.png'
        moz = 'moz.png'

        region = Region(0, 0, SCREEN_WIDTH, 2 * SCREEN_HEIGHT / 3)

        navigate(url)

        expected = exists(LocalWeb.FIREFOX_LOGO, 10)
        assert_true(self, expected, 'Page successfully loaded, firefox logo found.')

        select_location_bar()
        paste('moz')

        expected = region.exists(moz, 10)
        assert_true(self, expected, 'Searched string found at the bottom of the drop-down list.')

        expected = region.exists(search_settings, 10)
        assert_true(self, expected, 'The \'Search settings\' button is displayed in the awesome bar.')

        expected = region.exists(amazon_one_off_button, 10)
        assert_true(self, expected, 'The \'Amazon\' one-off button found.')

        expected = region.exists(bing_one_off_button, 10)
        assert_true(self, expected, 'The \'Bing\' one-off button found.')

        expected = region.exists(duck_duck_go_one_off_button, 10)
        assert_true(self, expected, 'The \'DuckDuckGo\' one-off button found.')

        expected = region.exists(ebay_one_off_button, 10)
        assert_true(self, expected, 'The \'Ebay\' one-off button found.')

        expected = region.exists(google_one_off_button, 10)
        assert_true(self, expected, 'The \'Google\' one-off button found.')

        expected = region.exists(twitter_one_off_button, 10)
        assert_true(self, expected, 'The \'Twitter\' one-off button found.')

        expected = region.exists(wikipedia_one_off_button, 10)
        assert_true(self, expected, 'The \'Wikipedia\' one-off button found.')