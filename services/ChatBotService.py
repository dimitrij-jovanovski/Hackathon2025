import openai

client = openai.OpenAI(api_key="my_openai_secret_key") #key is private, use your own

class ChatBotService:
    @staticmethod
    def AskTheChatBot(prompt):

        IntroString = "giving the bot character" #change
       
        print(prompt)

        odgovor = IntroString + prompt

        response = client.chat.completions.create(
             model="gpt-4o-mini",
             messages=[{"role": "user", "content": odgovor}]
         ).model_dump()

        return response['choices'][0]['message']['content']
