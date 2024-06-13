from Document import Document
from Report import Report
from Attachment import Attachment

# Inputs
# Headers for all documents
company_name = "Darryl Engineering"
project_name = "IEM C-602A Column and Caustic Piping"
document_description = "Detailed Pipe Stess Analysis, Revision 1"
date = "June 7, 2024"
maverick = "Maverick Applied Science, Inc."
document_name = "MAS-233266-FPC-1016-501"

# Variables for report
footer_roman_start = 2 # Starting roman numeral page will always be 2, so this might be redundant
footer_roman_finish = 4
file_path_original_report = r"C:\Users\phpai\OneDrive\Desktop\Report Files\Original Files\MAS-243373-HAR-0321-0501 - Report_R0.pdf"
file_path_modified_report = r"C:\Users\phpai\OneDrive\Desktop\Report Files\Files with Headers\MAS-243373-HAR-0321-0501 - Report_R0.pdf"

# Variable for attachments center header
attachment_center_header_top_margin_decrease = 0 # This is to be used when the center header is interfering with the other header text. Default should be zero (0). Any positive value added will move center header up. Start with 5

# Variables for attachment A
attachment_letter_a = "A"
has_cover_page_a = False
file_path_original_attachment_a = r"C:\Users\phpai\OneDrive\Desktop\Report Files\Original Files\Attachment A - FEA Input Screenshots.pdf"
file_path_modified_attachment_a = r"C:\Users\phpai\OneDrive\Desktop\Report Files\Files with Headers\Attachment A - FEA Input Screenshots.pdf"

# # Variables for attachment B
# attachment_letter_b = "B"
# has_cover_page_b = False
# file_path_original_attachment_b = "/content/drive/MyDrive/PDF Headers/PDF wo Headers/TEST 3266 Attachment B.pdf"
# file_path_modified_attachment_b = "/content/drive/MyDrive/PDF Headers/PDF w Headers/TEST 3266 Attachment B.pdf"

# # Variables for attachment D
# attachment_letter_d = "D"
# has_cover_page_d = True
# file_path_original_attachment_d = "/content/drive/MyDrive/PDF Headers/PDF wo Headers/MAS-233266-FPC-1016-002-Attachment_D.pdf"
# file_path_modified_attachment_d = "/content/drive/MyDrive/PDF Headers/PDF w Headers/MAS-233266-FPC-1016-002-Attachment_D.pdf"

# # Variables for attachment E
# attachment_letter_e = "E"
# has_cover_page_e = True
# file_path_original_attachment_e = "/content/drive/MyDrive/PDF Headers/PDF wo Headers/MAS-233266-FPC-1016-003-Attachment_E.pdf"
# file_path_modified_attachment_e = "/content/drive/MyDrive/PDF Headers/PDF w Headers/MAS-233266-FPC-1016-003-Attachment_E.pdf"

# # Variables for attachment F
# attachment_letter_f = "F"
# has_cover_page_f = True
# file_path_original_attachment_f = "/content/drive/MyDrive/PDF Headers/PDF wo Headers/MAS-233266-FPC-1016-004-Attachment_F.pdf"
# file_path_modified_attachment_f = "/content/drive/MyDrive/PDF Headers/PDF w Headers/MAS-233266-FPC-1016-004-Attachment_F.pdf"

# # Variables for attachment G
# attachment_letter_g = "G"
# has_cover_page_g = True
# file_path_original_attachment_g = "/content/drive/MyDrive/PDF Headers/PDF wo Headers/MAS-233266-FPC-1016-005-Attachment_G.pdf"
# file_path_modified_attachment_g = "/content/drive/MyDrive/PDF Headers/PDF w Headers/MAS-233266-FPC-1016-005-Attachment_G.pdf"

# Report
report = Report(
    company_name=company_name,
    project_name=project_name,
    document_description=document_description,
    date=date,
    maverick=maverick,
    document_name=document_name,
    footer_roman_start=footer_roman_start,
    footer_roman_finish=footer_roman_finish,
    file_path_original=file_path_original_report,
    file_path_modified=file_path_modified_report
)

report.add_headers_and_footers()
report.save_pdf()

# Attachemnt A
attachment_a = Attachment(
    company_name=company_name,
    project_name=project_name,
    document_description=document_description,
    date=date,
    maverick=maverick,
    document_name=document_name,
    attachment_letter=attachment_letter_a,
    file_path_original=file_path_original_attachment_a,
    file_path_modified=file_path_modified_attachment_a,
    has_cover_page=has_cover_page_a,
    attachment_center_header_top_margin_decrease=attachment_center_header_top_margin_decrease
)

attachment_a.add_headers_and_footers()
attachment_a.save_pdf()

# # Attachment B
# attachment_b = Attachment(
#     company_name=company_name,
#     project_name=project_name,
#     document_description=document_description,
#     date=date,
#     maverick=maverick,
#     document_name=document_name,
#     attachment_letter=attachment_letter_b,
#     file_path_original=file_path_original_attachment_b,
#     file_path_modified=file_path_modified_attachment_b,
#     has_cover_page=has_cover_page_b,
#     attachment_center_header_top_margin_decrease=attachment_center_header_top_margin_decrease
# )

# attachment_b.add_headers_and_footers()
# attachment_b.save_pdf()

