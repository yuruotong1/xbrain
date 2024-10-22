'''
OpenAI API提供了assistant模式，可以直接上传文件。详见：
    https://medium.com/@erik-kokalj/effectively-analyze-pdfs-with-gpt-4o-api-378bd0f6be03
但是OpenAI Next暂时还没有
    2024/10/22 23:53:49 httpx _client.py 
    HTTP Request: POST https://api.openai-next.com/v1/files "HTTP/1.1 503 Service Unavailable"
自己动手，把文件转成文字
也许这个文件应该放在util那边
'''

import os

def upload_file(file_path):
    '''
    检查是否是受支持的格式
    根据格式调用工具进行处理
    生成文本喂给大模型
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

    # Read file extension
    file_extension = os.path.splitext(file_path)[-1].lower().strip('.')

    # Determine file type and handle accordingly
    if file_extension in plain_text_files:
        return _handle_text(file_path, file_extension)
    elif file_extension in xml_based_files:
        return _handle_xml(file_path, file_extension)
    elif file_extension in image_files:
        return _handle_image(file_path)
    else:
        # Try to read as text
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return _handle_text(file_path)
        except (UnicodeDecodeError, FileNotFoundError, IsADirectoryError):
            return 'Unsupported file type'
        
def _handle_text(file_path):
    '''Handles text-based files.'''
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def _handle_xml(file_path, file_extension):
    '''Handles XML-based files.'''
    # Example implementation for handling XML-based files
    try:
        import xml.etree.ElementTree as ET
        tree = ET.parse(file_path)
        root = tree.getroot()
        return ET.tostring(root, encoding='utf-8').decode('utf-8')
    except ImportError:
        return 'Missing required library for XML handling'
    except ET.ParseError:
        return 'Invalid XML format'

def _handle_image(file_path):
    '''Handles image-based files.'''
    try:
        from PIL import Image
        import pytesseract
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
        return text
    except ImportError:
        return 'Missing required library for image handling'
    except FileNotFoundError:
        return 'File not found'
    except Exception as e:
        return f'Error processing image: {str(e)}'

    


