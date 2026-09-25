from pages.file_upload_page import FileUploadPage


def test_file_upload(driver, tmp_path):
    file_path = tmp_path / "sample_upload.txt"
    file_path.write_text("This is a test file for Selenium file upload testing.")

    upload_page = FileUploadPage(driver)
    upload_page.load()
    upload_page.upload_file(str(file_path))

    uploaded_filename = upload_page.get_uploaded_filename()
    assert uploaded_filename == "sample_upload.txt"