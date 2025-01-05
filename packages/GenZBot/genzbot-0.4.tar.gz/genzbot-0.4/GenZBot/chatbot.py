import os
import shutil
from zipfile import ZipFile
from .utils_list.AIModels import response
from .utils_list.backend import flask_app
from .utils_list.Images_list import *



class ChatBot:
    def __init__(self,llm='gemini',api_key = None,template_design='Plain',BotBehaviour=None,BotName="AI-BOT"):
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
            flask_code = flask_app.backendCode_gemini
        elif self.llm.lower() == 'llama':
            ai_response = response.Groq_Response(model=self.llm.lower(),system_instruction=self.BotBehaviour)
            flask_code = flask_app.backendCode_llama
        elif self.llm.lower() == 'gemma':
            ai_response = response.Groq_Response(model=self.llm.lower(),system_instruction=self.BotBehaviour)
            flask_code = flask_app.backendCode_gemma
        elif self.llm.lower() == 'mixtral':
            ai_response = response.Groq_Response(model=self.llm.lower(),system_instruction=self.BotBehaviour)
            flask_code = flask_app.backendCode_mixtral
        else:
            raise ValueError(f"Invalid model '{self.llm.lower()}'. Valid options are: 'openai','gemini','llama', 'gemma', 'mixtral'.")
        
        
        
        if self.template_design.lower()=='plain':
            from .utils_list.templates_list.design1 import index,style,script
        elif self.template_design.lower()=='galaxy':
            from .utils_list.templates_list.design2 import index,style,script
        else:
            raise ValueError("Invalid template designs. Valid options are Plain, Galaxy")
        
        
        folders = [
                f"{self.base_dir}/AI_Service",
                f"{self.base_dir}/Backend",
                f"{self.base_dir}/Frontend/static",
                f"{self.base_dir}/Frontend/templates",
            ]
        files = {
                f"{self.base_dir}/AI_Service/AIResponse.py": ai_response,
                f"{self.base_dir}/Backend/app.py": flask_code(),
                f"{self.base_dir}/Frontend/static/style.css": style.getStyle(),
                f"{self.base_dir}/Frontend/static/script.js": script.getScript(),
                f"{self.base_dir}/Frontend/templates/index.html": index.getHtml(self.BotName),
                f"{self.base_dir}/.env": "",  
                f"{self.base_dir}/requirements.txt": "",
            }
        
        
        if self.template_design.lower() == 'galaxy':
            project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
            

            source = os.path.join(project_root,'GenZBot', 'utils_list', 'Images_list', 'galaxy_img.png')
            destination = os.path.join(self.base_dir, 'Frontend', 'static', 'galaxy_img.png')


            if os.path.exists(source):
                os.makedirs(os.path.dirname(destination), exist_ok=True)
                shutil.copy(source, destination)
            else:
                raise ValueError('Internal Error')
            
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
        
        elif self.llm.lower() in ["llama","gemma","mixtral"]:
            if self.llm.lower() == "llama":
                key_name = 'LLAMA_API_KEY'
            elif self.llm.lower() == "gemma":
                key_name = 'GEMMA_API_KEY'
            elif self.llm.lower() == "mixtral":
                key_name = 'MIXTRAL_API_KEY'
            
            env_file = os.path.join(self.base_dir, ".env")
            with open(env_file, "w",encoding='utf-8') as f:
                   f.write(f'{key_name}="{self.api_key}"\n')
            print("Customized .env file with the API key.")
            
            requirement_file = os.path.join(self.base_dir, "requirements.txt")
            with open(requirement_file, "w",encoding='utf-8') as f:
                   f.write("flask\npython-dotenv\ngroq\ngunicorn==20.1.0")
            print("Customized requirements.txt file with required packages.")