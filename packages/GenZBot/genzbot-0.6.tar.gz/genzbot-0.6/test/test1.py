from GenZBot.chatbot import ChatBot

bot = ChatBot(llm='openai',api_key='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',template_design='galaxy')

bot.CreateProject()

bot.run()