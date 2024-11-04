
from pymilvus import MilvusClient

from xbrain.utils.openai_utils import generate_embedding

client = MilvusClient("./.vsdb/xbrain_milvus.db")

def retrieve_action(query: str):
    query_embedding = generate_embedding(query)

    # 从数据库中检索嵌入
    results = client.search(
        data=[query_embedding],
        collection_name="collection",
        limit=5,
        output_fields=["content"]
    )
    for result in results[0]:
        print(f"Content: {result.entity.get('content')}, Similarity score: {result.score}")

    return results[0]

if __name__ == "__main__":
    retrieve_action("你好")
