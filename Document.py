class Document:

    FONT_SIZE = 12
    FONT_NAME = "BA" # Stands for Book Antiqua, which is the default header font used by MAS
    FONT_FILE = "/content/drive/MyDrive/PDF Headers/Book Antiqua Font Files/BKANT.TTF" # Font file for Book Antiqua
    FONT_COLOR = (0,0,0) # (0,0,0) is the color black

    # Default margins (margins seen below are in points, not inches. Where 1 in. = 72 points)
    LEFT_MARGIN = 61
    TOP_MARGIN_1 = 45
    TOP_MARGIN_2 = 60
    TOP_MARGIN_3 = 75
    BOTTOM_MARGIN = 35

    def __init__(self, company_name, project_name, document_description, date, maverick, document_name, file_path_original, file_path_modified):
        self.company_name = company_name
        self.project_name = project_name
        self.document_description = document_description
        self.date = date
        self.maverick = maverick
        self.document_name = document_name
        self.file_path_original = file_path_original
        self.file_path_modified = file_path_modified
        # Open document (requires fitz module)
        self.doc = fitz.open(self.file_path_original)
        # Initialize font
        self.font = fitz.Font(fontname=self.FONT_NAME, fontfile=self.FONT_FILE)

    @classmethod
    def set_margings(cls, left_margin, top_margin_1, top_margin_2, top_margin_3, bottom_margin):
        cls.LEFT_MARGIN = left_margin
        cls.TOP_MARGIN_1 = top_margin_1
        cls.TOP_MARGIN_2 = top_margin_2
        cls.TOP_MARGIN_3 = top_margin_3
        cls.BOTTOM_MARGIN = bottom_margin

    @classmethod
    def set_font_size(cls, font_size):
        cls.FONT_SIZE = font_size

    @classmethod
    def set_font_name(cls, font_name):
        cls.FONT_NAME = font_name

    @classmethod
    def set_font_file(cls, font_file):
        cls.FONT_FILE = font_file

    @classmethod
    def set_top_margin_1(cls, top_margin_1):
        cls.TOP_MARGIN_1 = top_margin_1

    @classmethod
    def set_top_margin_2(cls, top_margin_2):
        cls.TOP_MARGIN_2 = top_margin_2

    @classmethod
    def set_top_margin_3(cls, top_margin_3):
        cls.TOP_MARGIN_3 = top_margin_3

    @classmethod
    def set_bottom_margin(cls, bottom_margin):
        cls.BOTTOM_MARGIN = bottom_margin

    @staticmethod
    def points_to_inches(points):
        return points / 72

    @staticmethod
    def inches_to_points(inches):
        return inches * 72

    def get_page_width(self):
        return self.doc[0].rect.width

    def get_page_height(self):
        return self.doc[0].rect.height