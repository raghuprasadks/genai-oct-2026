import cohere

co = cohere.ClientV2(api_key="5XDbMDADmdBFDPd1rxKDiYXREjhJ084bNSEFameN")

response = co.chat(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assitant"
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "who are you"
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": "Hello there! I'm Command, a Cohere-built AI assistant. I'm designed to offer in-depth and accurate responses to your questions. How can I be of service today?"
                }
            ]
        }
    ],
    thinking={
          "type": "enabled"
        },
    temperature=0.6,
    model="command-a-plus-05-2026",
)

print(response)