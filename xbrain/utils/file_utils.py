import os
import re
import logging

import zhon

logger = logging.getLogger(__name__)

def extract_text(file_path):
    '''Handles text-based files.'''
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        file_name = os.path.basename(file_path)
        text_data = {
            'filename': file_name,
            'content': content
        }
        logger.info(text_data)
        return text_data
    except (UnicodeDecodeError, FileNotFoundError, IsADirectoryError):
        return {'error': 'Unsupported file type'}
    
def cut_sent(para):
    para = re.sub('([。！？\?])([^”’])', r"\1\n\2", para)  # 单字符断句符
    para = re.sub('(\.{6})([^”’])', r"\1\n\2", para)  # 英文省略号
    para = re.sub('(\…{2})([^”’])', r"\1\n\2", para)  # 中文省略号
    para = re.sub('([。！？\?][”’])([^，。！？\?])', r'\1\n\2', para)
    # 如果双引号前有终止符，那么双引号才是句子的终点，把分句符\n放到双引号后，注意前面的几句都小心保留了双引号
    para = para.rstrip()  # 段尾如果有多余的\n就去掉它
    # 很多规则中会考虑分号;，但是这里我把它忽略不计，破折号、英文双引号等同样忽略，需要的再做些简单调整即可。
    return para.split("\n")

def split_text(text, max_chars=800, overlap=0.2):
    """
    Splits a given text into chunks of max_chars, preserving sentence boundaries
    and adding overlap between chunks.

    Parameters:
    - text (str): The input text to be chunked.
    - max_chars (int): Maximum characters per chunk.
    - overlap (float): Overlap fraction between chunks (0.0 to 1.0).

    Returns:
    - List[str]: List of text chunks.
    """
    # Split the text into sentences
    sentences = cut_sent(text)
    chunks = []
    current_chunk = ""
    overlap_chars = int(max_chars * overlap)

    for sentence in sentences:
        # Check if adding the sentence would exceed the character limit for the current chunk
        if len(current_chunk) + len(sentence) > max_chars:
            # Add the current chunk to the list of chunks
            chunks.append(current_chunk.strip())
            # Prepare for the next chunk with overlap
            current_chunk = current_chunk[-overlap_chars:] if len(current_chunk) > overlap_chars else ""
        # Add the current sentence to the chunk
        current_chunk += " " + sentence

    # Add the last chunk
    if current_chunk:
        chunks.append(current_chunk.strip())
        logger.info(current_chunk.strip)
    
    return chunks
