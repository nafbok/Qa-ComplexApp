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
        """Add new post:
            - Go to the Create Post
            - Add new post
            - Verify New post added message success"""
        title_post_value = self.title_post()
        body_post_value = self.body_post()

        # Go to the Create Post
        create_new_post = main_page.header.transition_to_create_post_page()

        # Add new post
        post_page = create_new_post.adding_new_post(title_post_value, body_post_value)

        # Verify New post added message success
        post_page.verify_adding_post()

    def test_remove_post(self, main_page):
        """Remove created post:
            Steps:
                - Go to Create Post page
                - Create post
                - Verify New post added message success
                - Delete post
                - Verify New post deleted message success"""

        title_post_value = self.title_post()
        body_post_value = self.body_post()

        # Go to the Create Post
        create_new_post = main_page.header.transition_to_create_post_page()
        # Add new post
        post_page = create_new_post.adding_new_post(title_post_value, body_post_value)

        # Verify New post added message success"""
        post_page.verify_adding_post()

        # Delete Post
        my_profile = create_new_post.delete_created_post()

        # Verify Post was deleted successfully
        my_profile.verify_message_deleted_post()
