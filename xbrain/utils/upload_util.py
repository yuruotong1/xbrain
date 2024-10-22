'''
OpenAI API提供了assistant模式，可以直接上传文件。详见：
    https://medium.com/@erik-kokalj/effectively-analyze-pdfs-with-gpt-4o-api-378bd0f6be03
但是OpenAI Next暂时还没有
    2024/10/22 23:53:49 httpx _client.py 
    HTTP Request: POST https://api.openai-next.com/v1/files "HTTP/1.1 503 Service Unavailable"
自己动手，把文件转成文字
'''

import os
import json

def process_file(file_path):
    '''
    检查是否是受支持的格式
    根据格式调用工具进行处理
    生成文本喂给大模型
        入参：文件路径
        返回：描述文件内容的字符串
    '''
    plain_text_files = [
        'txt',      # Plain text
        'csv',      # Comma-separated values (structured plain text)
        'json',     # JSON files (structured but still plain text)
        'md',       # Markdown files
        'log',      # Log files (plain text)
        # Programming language files
        'py',       # Python scripts
        'java',     # Java source code
        'js',       # JavaScript files
        'c',        # C source code
        'cpp',      # C++ source code
        'rb',       # Ruby scripts
        'go',       # Go source code
        'rs',       # Rust source code
        'html',     # HTML files (could be in both plain-text or XML-based depending on use)
        'css',      # CSS files (styling for HTML)
        'xml'       # XML (common for data and config files)
    ]

    xml_based_files = [
        'docx',     # Microsoft Word (XML structure inside ZIP container)
        'xlsx',     # Microsoft Excel (XML structure inside ZIP container)
        'pptx',     # Microsoft PowerPoint (XML structure inside ZIP container)
        'pdf'       # When processed as XML (via libraries like pdfminer for structured content)
    ]

    image_files = [
        'jpg',      # JPEG images
        'png',      # PNG images
        'jpeg',     # Same as JPG
        'bmp',      # Bitmap images
    ]

    file_extension = os.path.splitext(file_path)[-1].lower().strip('.')

    if file_extension in plain_text_files:
        return _handle_text(file_path)
    elif file_extension in xml_based_files:
        # 这几个XML还都不一样
        # import各自的库
        return _handle_xml(file_path, file_extension)
    elif file_extension in image_files:
        return _handle_image(file_path)
    else:
        # 把其他格式一揽子按照纯文本试一下
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return _handle_text(file_path) # 行的话也没有文件格式提示了
        except (UnicodeDecodeError, FileNotFoundError, IsADirectoryError):
            return 'Unsupported file type'
        
def _handle_text(file_path):
    '''Handles text-based files.'''
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return f"{file_path}: {content}"

def _handle_xml(file_path, file_extension):
    '''Handles XML-based files.'''
    if file_extension == 'docx':
        return _handle_docx(file_path)
    elif file_extension == 'xlsx':
        return _handle_xlsx(file_path)
    elif file_extension == 'pptx':
        return _handle_pptx(file_path)
    elif file_extension == 'pdf':
        return _handle_pdf(file_path)
    
def _handle_docx(file_path):
    '''Handles DOCX files.'''
    # TODO: 看一下这个，具体读出多少信息是否要进行调整？ 
    # 输出的是个JSON，python3 -m unittest tests.test_handle_file 可以看
    try:
        from docx import Document
        # 自己装python-docx，我不敢动requirements.txt
        from docx.shared import Pt
        from docx.oxml.ns import qn
        doc = Document(file_path)
        doc_data = {
            'paragraphs': [],
            'page_size': None,
            'line_spacing': None,
            'margins': None
        }
        # Extract page size and margins
        sections = doc.sections
        if sections:
            first_section = sections[0]
            doc_data['page_size'] = {
                'width': first_section.page_width.pt if first_section.page_width else None,
                'height': first_section.page_height.pt if first_section.page_height else None
            }
            doc_data['margins'] = {
                'top_margin': first_section.top_margin.pt if first_section.top_margin else None,
                'bottom_margin': first_section.bottom_margin.pt if first_section.bottom_margin else None,
                'left_margin': first_section.left_margin.pt if first_section.left_margin else None,
                'right_margin': first_section.right_margin.pt if first_section.right_margin else None
            }
        # Extract paragraphs with formatting details
        for para in doc.paragraphs:
            para_data = {
                'text': para.text,
                'font': [run.font.name for run in para.runs if run.font],
                'font_size': [run.font.size.pt if run.font.size else None for run in para.runs],
                'bold': [run.bold for run in para.runs],
                'italic': [run.italic for run in para.runs],
                'underline': [run.underline for run in para.runs],
                'line_spacing': para.paragraph_format.line_spacing if para.paragraph_format.line_spacing else None
            }
            doc_data['paragraphs'].append(para_data)
        return json.dumps(doc_data, ensure_ascii=False, indent=4)
    except ImportError:
        return 'Missing required library for DOCX handling'
    except Exception as e:
        return f'Error processing DOCX: {str(e)}'


def _handle_xlsx(file_path):
    '''Handles XLSX files.'''
    pass
    
def _handle_pptx(file_path):
    '''Handles PPTX files.'''
    # 文字PPT和图片PPT
    # 详见图片处理
    pass

def _handle_pdf(file_path):
    '''Handles PDF files.'''
    # 文字PDF和图片PDF
    # 详见图片处理
    pass


def _handle_image(file_path):
    '''Handles image-based files.'''
    # 先用CLIP CLIP出来判断是文字还是图片
    # 文字交给OCR，就用CLIP的文本匹配
    pass

    


