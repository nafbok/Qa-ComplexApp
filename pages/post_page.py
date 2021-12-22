
from constants.post_page import PostPageConstants
from pages.base import BasePage
from pages.header import Header
from pages.my_profile import MyProfile
from pages.utils import log_decorator


class PostPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = PostPageConstants()
        self.header = Header(self.driver)

    @log_decorator
    def delete_created_post(self):
        """Remove created post"""
        delete_post = self.wait_until_find_element(value=self.constants.REMOVE_ICON_XPATH)
        delete_post.click()
        self.log.info("Post was deleted")
        return MyProfile(self.driver)

    @log_decorator
    def verify_adding_post(self):
        """Verify new post was added successfully"""
        message_added_post = self.wait_until_find_element(value=self.constants.MESSAGE_NEW_POST_CREATED_XPATH)
        assert message_added_post.text == 'New post successfully created.'

