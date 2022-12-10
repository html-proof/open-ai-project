
import openai
import json

openai.api_key =""

while True:
    prompt =input("input any item to search :")
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=0.5,
      max_tokens=150,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )

    json_object = json.loads(str(response))
    print(json_object['choices'][0]['text'])
