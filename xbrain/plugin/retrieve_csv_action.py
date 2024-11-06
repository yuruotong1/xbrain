import numpy as np
from xbrain.utils.openai_utils import generate_embedding
import pandas as pd
from pydantic import BaseModel, Field
from typing import ClassVar, Optional, List, Dict
from xbrain.core import xbrain_tool
from xbrain.utils.translations import _
import logging

logger = logging.getLogger(__name__)

def cosine_similarity(a, b):
    # 计算两个向量的点积
    dot_product = np.dot(a, b)
    # 计算每个向量的L2范数（即向量的长度）
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    # 计算余弦相似度
    epsilon = 1e-10
    return dot_product / (norm_a * norm_b + epsilon)


class XBrainRetrieve(BaseModel):
    '''Return top 3 matched text results based on query embedding'''
    description: ClassVar[str] = _("Return top 3 matched text results based on query embedding")
    
    query: str = Field(
        description="User query text. Always default to this tool if other tools are not suitable."
    )


@xbrain_tool.Tool(model=XBrainRetrieve)
def retrieve_action(query: str) -> Optional[list]:
    df = pd.read_csv('./.embedded.csv')
    df['ada_embedding'] = df.ada_embedding.apply(eval).apply(np.array)
    embedding = generate_embedding(query)
    df['similarities'] = df.ada_embedding.apply(lambda x: cosine_similarity(x, embedding))
    res = df.sort_values('similarities', ascending=False).head(3)
    logger.info(res['text'].tolist())
    return res['text'].tolist()


