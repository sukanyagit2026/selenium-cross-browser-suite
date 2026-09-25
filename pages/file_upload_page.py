from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FileUploadPage(BasePage):
    URL = "https://the-internet.herokuapp.com/upload"

    FILE_INPUT = (By.ID, "file-upload")
    UPLOAD_BUTTON = (By.ID, "file-submit")
    UPLOADED_FILENAME = (By.ID, "uploaded-files")

    def load(self):
        self.open(self.URL)

    def upload_file(self, file_path):
        file_input = self.find(self.FILE_INPUT)
        file_input.send_keys(file_path)
        self.click(self.UPLOAD_BUTTON)

    def get_uploaded_filename(self):
        return self.get_text(self.UPLOADED_FILENAME)