import openai

openai.api_key = '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'

messages = [ {"role": "system", "content": 
              "You are a intelligent assistant."} ]
while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="text-davinci-002", messages=messages
        )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})