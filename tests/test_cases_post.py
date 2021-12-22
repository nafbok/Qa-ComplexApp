import pytest

from conftest import BaseTest


class TestPostPage(BaseTest):

    @pytest.fixture(scope="function")
    def main_page(self, start_page, random_user):
        """Register user and return data"""
        # Fill email, login and password fields
        main_page = start_page.register_user(random_user)
        return main_page

    def test_add_new_post(self, main_page, random_user):
        """
        Pre-conditions:
            - Register user
        Add new post:
            - Go to the Create Post
            - Fill Title and Body
            - Click in Save post button
            - Verify New post added message success
        """

        # Go to the Create Post
        create_new_post = main_page.header.transition_to_create_post_page()

        # Add new post
        title_post_value = self.title_post()
        body_post_value = self.body_post()
        post_page = create_new_post.adding_new_post(title_post_value, body_post_value)

        # Verify New post added message success
        post_page.verify_adding_post()

    def test_remove_post(self, main_page):
        """
        Pre-conditions:
            - Register user
        Steps:
            - Go to Create Post page
            - Fill Title and Body
            - Click in Save post button
            - Verify New post added message success
            - Click on Delete post
            - Verify New post deleted message success"""

        # Go to the Create Post
        create_new_post = main_page.header.transition_to_create_post_page()

        # Add new post
        title_post_value = self.title_post()
        body_post_value = self.body_post()
        post_page = create_new_post.adding_new_post(title_post_value, body_post_value)

        # Verify New post added message success
        post_page.verify_adding_post()

        # Delete Post
        my_profile = post_page.delete_created_post()

        # Verify Post was deleted successfully
        my_profile.verify_message_deleted_post()
