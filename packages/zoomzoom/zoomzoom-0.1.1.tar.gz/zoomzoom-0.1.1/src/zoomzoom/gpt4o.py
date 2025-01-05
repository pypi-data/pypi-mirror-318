import configparser
import os
import json
import requests

def get_config():
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.expanduser("~"), ".zoomzoom", "config.ini")
    if not config.read(config_path, encoding='utf-8'):
        raise Exception("无法加载配置文件")
    return config

def ask(messages):
    """调用OpenAI API进行对话"""
    try:
        config = get_config()
        api_key = config['GenAI']['openai_token']
        api_url = config['GenAI']['openai_chat_url']
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        
        data = {
            'model': 'gpt-4',
            'messages': messages,
            'temperature': 0.7
        }
        
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()
        
        return response.json()['choices'][0]['message']['content']
        
    except Exception as e:
        raise Exception(f"OpenAI API调用失败: {str(e)}")
