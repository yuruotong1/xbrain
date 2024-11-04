import os
import re
import logging

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
    sentences = re.split(r'(?<=[。！？.!?])\s*', text)

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
