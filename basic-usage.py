from openai import OpenAI
import json

# Initialize OpenAI client that points to the local LM Studio server
client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
)

# Define the conversation with the AI
messages = [
    {"role": "system", "content": "You are a helpful AI assistant."},
]

while True:
    try:
        msg = input("User> ")
    except KeyboardInterrupt:
        break
    messages.append(dict(role="user","content":msg.strip()))

# Get response from AI
    response = client.chat.completions.create(
        model="your-model",
        messages=messages,
    )

    # Parse and display the results
    results = json.loads(response.choices[0].message.content)
    print(json.dumps(results, indent=2))
    messages.append(dict(role="assistant","content":result.strip()))