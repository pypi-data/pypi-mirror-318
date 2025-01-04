# Deployer code here
from cryptography.fernet import Fernet
import base64
from huggingface_hub import HfApi, create_repo, upload_file, add_space_variable

class AgentDeployer:
    def __init__(self, license_key):
        self.key = base64.b64encode(license_key.encode())
        self.cipher = Fernet(self.key)
        
    def deploy(self, config, tools, hf_token):
        space_id = f"{config['HF_USERNAME']}/{config['SPACE_NAME']}"
        api = HfApi(token=hf_token)
        
        # Create space
        create_repo(space_id, repo_type="space", space_sdk="streamlit", token=hf_token)
        
        # Add secrets
        for key, value in config.get('secrets', {}).items():
            add_space_variable(repo_id=space_id, key=key, value=value, token=hf_token)
            
        # Upload files
        for name, content in {'app.py': config['APP_CONTENT'], 
                            'config.py': config['CONFIG'],
                            'tools.py': tools}.items():
            with open(name, 'w') as f:
                f.write(content)
            api.upload_file(path_or_fileobj=name,
                          path_in_repo=name,
                          repo_id=space_id,
                          repo_type="space")
                          
        return f"https://huggingface.co/spaces/{space_id}"