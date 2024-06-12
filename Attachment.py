from Document import Document

class Attachment(Document):

    def __init__(self, company_name, project_name, document_description, date, maverick, document_name, attachment_letter, file_path_original, file_path_modified, has_cover_page, attachment_center_header_top_margin_decrease):
        super().__init__(company_name, project_name, document_description, date, maverick, document_name, file_path_original, file_path_modified)
        self.attachment_letter = attachment_letter
        self.has_cover_page = has_cover_page
        self.attachment_name = f"Attachment - {self.attachment_letter}"
        self.attachment_footer = f"{self.attachment_letter} - "
        self.attachment_center_header_top_margin_decrease = attachment_center_header_top_margin_decrease

    def header_range(self):
        if self.has_cover_page:
            return range(2, self.doc.page_count + 1)
        else:
            return range(1, self.doc.page_count + 1)

    def save_pdf(self):
        self.doc.save(self.file_path_modified)
        print(f"Header added. File saved as '{self.file_path_modified}'")

    def add_headers_and_footers(self):

        # Get width and height of first page, which should be the same as all other pages
        page_width = self.get_page_width()
        page_height = self.get_page_height()

        # Get length of text to be written on right side of the page
        date_length = self.font.text_length(self.date, fontsize=Document.FONT_SIZE)
        maverick_length = self.font.text_length(self.maverick, fontsize=Document.FONT_SIZE)
        doc_name_length = self.font.text_length(self.document_name, fontsize=Document.FONT_SIZE)
        attachment_name_length = self.font.text_length(self.attachment_name, fontsize=Document.FONT_SIZE)

        # Loop through document pages and add headers
        for i, page in enumerate(self.doc, start=1):
            # Load Book Antiqua font file
            page.insert_font(fontfile=Document.FONT_FILE, fontname=Document.FONT_NAME)

            # Write headers to page
            if i in self.header_range():
                # Headers on left of page
                page.insert_text((self.LEFT_MARGIN, self.TOP_MARGIN_1), self.company_name, fontsize=Document.FONT_SIZE, fontname=Document.FONT_NAME, color=Document.FONT_COLOR)
                page.insert_text((self.LEFT_MARGIN, self.TOP_MARGIN_2), self.project_name, fontsize=Document.FONT_SIZE, fontname=Document.FONT_NAME, color=Document.FONT_COLOR)
                page.insert_text((self.LEFT_MARGIN, self.TOP_MARGIN_3), self.document_description, fontsize=Document.FONT_SIZE, fontname=Document.FONT_NAME, color=Document.FONT_COLOR)
                # Headers on right of page
                page.insert_text((page_width - (self.LEFT_MARGIN + date_length), self.TOP_MARGIN_1), self.date, fontsize=Document.FONT_SIZE, fontname=Document.FONT_NAME, color=Document.FONT_COLOR)
                page.insert_text((page_width - (self.LEFT_MARGIN + maverick_length), self.TOP_MARGIN_2), self.maverick, fontsize=Document.FONT_SIZE, fontname=Document.FONT_NAME, color=Document.FONT_COLOR)
                page.insert_text((page_width - (self.LEFT_MARGIN + doc_name_length), self.TOP_MARGIN_3), self.document_name, fontsize=Document.FONT_SIZE, fontname=Document.FONT_NAME, color=Document.FONT_COLOR)
                # Header on center of page (attachment name header)
                page.insert_text(((page_width/2) - (attachment_name_length/2), self.TOP_MARGIN_1 - self.attachment_center_header_top_margin_decrease), self.attachment_name, fontsize=Document.FONT_SIZE, fontname=Document.FONT_NAME, color=Document.FONT_COLOR)
                # Attachment footer
                attachment_num = str((i + 1) - self.header_range()[0])
                attachment_footer_length = self.font.text_length((self.attachment_footer + attachment_num), fontsize=Document.FONT_SIZE)
                page.insert_text(((page_width/2) - (attachment_footer_length/2), (page_height - self.BOTTOM_MARGIN)), f'{self.attachment_footer}{(i + 1) -  self.header_range()[0]}', fontsize=Document.FONT_SIZE, fontname=Document.FONT_NAME, color=Document.FONT_COLOR)