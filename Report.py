import roman

from Document import Document

class Report(Document):

    def __init__(self, company_name, project_name, document_description, date, maverick, document_name, footer_roman_start, footer_roman_finish, file_path_original, file_path_modified):
        super().__init__(company_name, project_name, document_description, date, maverick, document_name, file_path_original, file_path_modified)
        self.footer_roman_start = footer_roman_start
        self.footer_roman_finish = footer_roman_finish

    def footer_roman_range(self):
        return range(self.footer_roman_start, self.footer_roman_finish + 1)

    def footer_normal_range(self):
        return range(self.footer_roman_finish + 1, self.doc.page_count + 1)

    def header_range(self):
        return range(self.footer_roman_start, self.doc.page_count + 1)

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

            # Report roman numeral footer
            if i in self.footer_roman_range():
                roman_num = roman.toRoman((i + 1) - self.footer_roman_start).lower()
                footer_roman_length = self.font.text_length(roman_num, fontsize=Document.FONT_SIZE)
                page.insert_text(((page_width/2) - (footer_roman_length/2), (page_height - self.BOTTOM_MARGIN)), roman_num, fontsize=Document.FONT_SIZE, fontname=Document.FONT_NAME, color=Document.FONT_COLOR)

            # Report footer
            if i in self.footer_normal_range():
                page_num = str((i + 1) - self.footer_normal_range()[0])
                footer_length = self.font.text_length(page_num, fontsize=Document.FONT_SIZE)
                page.insert_text(((page_width/2) - (footer_length/2), (page_height - self.BOTTOM_MARGIN)), page_num, fontsize=Document.FONT_SIZE, fontname=Document.FONT_NAME, color=Document.FONT_COLOR)