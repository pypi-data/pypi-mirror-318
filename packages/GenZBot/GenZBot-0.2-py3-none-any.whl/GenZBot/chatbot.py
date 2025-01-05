import os
import shutil
from zipfile import ZipFile
from utils_list.AIModels import response
from utils_list.backend import flask_app



class ChatBot:
    def __init__(self,llm='gemini',api_key = None,template_design='design1',BotBehaviour=None,BotName="AI-BOT"):
        self.llm = llm
        self.api_key = api_key
        self.template_design = template_design
        self.BotBehaviour = BotBehaviour
        self.BotName = BotName
        self.base_dir = 'Chatbot_Project'
        
        
    def CreateProject(self):
        if not self.api_key:
            raise ValueError("API key is required to create the project.")
        
        print(f"Creating project with LLM: {self.llm}, Template: {self.template_design}")
        
        self._create_structure()
        
        self._customize_files()
        
        # self._zip_project()
        
        print(f"Project created and saved as {self.base_dir}")
    
    def _create_structure(self):
        if self.llm.lower() == 'gemini':
            ai_response = response.Gemini_Response(system_instruction=self.BotBehaviour)
        if self.template_design.lower()=='design1':
            from utils_list.templates_list.design1 import index,style,script
        folders = [
                f"{self.base_dir}/AI_Service",
                f"{self.base_dir}/Backend",
                f"{self.base_dir}/Frontend/static",
                f"{self.base_dir}/Frontend/templates",
            ]
        files = {
                f"{self.base_dir}/AI_Service/AIResponse.py": ai_response,
                f"{self.base_dir}/Backend/app.py": flask_app.backendCode(),
                f"{self.base_dir}/Frontend/static/style.css": style.getStyle(),
                f"{self.base_dir}/Frontend/static/script.js": script.getScript(),
                f"{self.base_dir}/Frontend/templates/index.html": index.getHtml(self.BotName),
                f"{self.base_dir}/.env": "",  
                f"{self.base_dir}/requirements.txt": "",
            }
        
        for folder in folders:
            os.makedirs(folder, exist_ok=True)
        
        for file_path, content in files.items():
            with open(file_path, "w",encoding='utf-8') as f:
                f.write(content)
    
    def  _customize_files(self):
        if self.llm.lower()=="gemini":
            env_file = os.path.join(self.base_dir, ".env")
            with open(env_file, "w",encoding='utf-8') as f:
                   f.write(f'GOOGLE_API_KEY="{self.api_key}"\n')
            print("Customized .env file with the API key.")
            
            requirement_file = os.path.join(self.base_dir, "requirements.txt")
            with open(requirement_file, "w",encoding='utf-8') as f:
                   f.write("flask\npython-dotenv\ngoogle-generativeai\ngunicorn==20.1.0")
            print("Customized requirements.txt file with required packages.")