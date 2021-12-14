from constants.create_post import CreatePostConstants
from pages.base import BasePage


class CreatePost(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CreatePostConstants()

    def create_post_is_opened(self):
        """Verify create post page is opened"""
        new_post = self.wait_until_element_enabled(value=self.constants.TITLE_POST_XPATH)
        assert new_post.text == 'Title'
