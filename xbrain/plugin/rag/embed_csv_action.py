from pydantic import BaseModel, Field
from typing import ClassVar
from xbrain.core import xbrain_tool
from xbrain.utils.file_utils import extract_text, split_text
from xbrain.utils.translations import _
from xbrain.utils.openai_utils import generate_embedding
import os
import logging
import pandas as pd
logger = logging.getLogger(__name__)

# Create the collection with the specified schema


class XBrainEmbed(BaseModel):
    '''Stores embedding of text into vectorstore database'''
    description: ClassVar[str] = _("Stores embedding of text into vectorstore database")
    
    path: str = Field(
        description="path to file or directory of files that needs to be embedded and stored."
    )

@xbrain_tool.Tool(model=XBrainEmbed)
def embedding_csv_action(path: str):
    # 创建一个csv
    pd.DataFrame(columns=['ada_embedding', 'data']).to_csv('./.embedded.csv', index=False)
    
    text_data = extract_text(path)
    chunks = split_text(text_data.get('content'))
    df = pd.read_csv("./.embedded.csv")
    df['data'] = chunks
    embeddings = []
    for chunk in chunks:
        # 使用 loc 方法添加新行
        embeddings.append(generate_embedding(chunk))
    df['ada_embedding'] = embeddings
    df.to_csv('./.embedded.csv', index=False)


