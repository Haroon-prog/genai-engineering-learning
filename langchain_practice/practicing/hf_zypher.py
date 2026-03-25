from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()

client = InferenceClient(
    model="HuggingFaceH4/zephyr-7b-beta",
    token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
)

result = client.chat_completion(
    messages=[
        {"role": "user", "content": "what are the things skills or technologies that a AI engineer should have?"}
    ]
)

print(result.choices[0].message.content)