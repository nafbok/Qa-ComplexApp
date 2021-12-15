class CreatePostConstants:
    TITLE_POST_XPATH = ".//*[contains(text(), 'Title')]"
    TITLE_INPUT_XPATH = ".//input[@id='post-title']"
    BODY_CONTENT_XPATH = ".//*[@id='post-body']"
    BUTTON_SAVE_NEW_POST_XPATH = ".//*[text()='Save New Post']"
    MESSAGE_NEW_POST_CREATED_XPATH = ".//*[text()='New post successfully created.']"
