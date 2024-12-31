import os
import glob
import re
import difflib
import configparser

from datetime import datetime
from bs4 import BeautifulSoup
from openai import AzureOpenAI  



class diff_dect():
    
    def __init__(self, 
                 new_html_file, 
                 old_html_file, 
                 azure_endpoint, 
                 azure_model, 
                 azure_key, 
                 azure_api_version):
        
        self.new_html_file = new_html_file
        self.old_html_file = old_html_file
        self.azure_endpoint = azure_endpoint
        self.azure_model =azure_model
        self.azure_key = azure_key
        self.azure_api_version = azure_api_version


    def extract_contents(self, text):
        # 使用正則表達式提取所有符合的中文標題（例如：[新聞] 黃國昌問與聯合再生有何關係?）
        pattern = r'[^\s][^\n]*[^\s]'  # 假設標題是 [類型] 標題內容
        visible_text = re.findall(pattern, text)
        return visible_text
    

    def update_html(self, new_html):

        # 確保資料夾存在
        os.makedirs("data", exist_ok=True)

        # 刪除 data/ 資料夾內所有 .html 檔案
        html_files = glob.glob("data/*.html")
        for file in html_files:
            os.remove(file)

        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"html_file_{current_time}.html"
        file_path = os.path.join('data', file_name)

        # 寫入文字到 .txt 檔案
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_html)

        print(f"save html to : {file_path}")


    def compare_text(self):

        soup_new = BeautifulSoup(self.new_html_file, 'html.parser').get_text()
        soup_new_text = self.extract_contents(soup_new)

        soup_old = BeautifulSoup(self.old_html_file, 'html.parser').get_text()
        soup_old_text = self.extract_contents(soup_old)


        if soup_new_text != soup_old_text:
            # 使用 difflib 顯示差異
            diff = difflib.unified_diff(soup_new_text, soup_old_text, fromfile='page1.txt', tofile='page2.txt', lineterm='')
            diff_list = [line for line in diff if line.startswith('-') or line.startswith('+')]
            
            return diff_list
        else:
            return None


    def GPT_text_meaning_compare(self, ori_txt: str, new_txt_list: list):

        prompt_content = f"""
            請幫我判斷下面的list中的每個值，是否有"{ori_txt}"的 升級版本？
            如果有，請回傳list中升級版本的名稱。如果都沒有，請回傳null。

            list如下：  
            {new_txt_list}

            回答格式如下：
            {{"result": "升級版本"}}
            """

        endpoint = os.getenv("ENDPOINT_URL", self.azure_endpoint)  
        deployment = os.getenv("DEPLOYMENT_NAME", self.azure_model) 
        client = AzureOpenAI(  
            azure_endpoint = endpoint,  
            api_key = self.azure_key,
            api_version = self.azure_api_version,  
        )  

        chat_prompt = [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "您是協助比對資料的 AI 助理。"
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt_content
                    }
                ]
            }
        ] 

        messages = chat_prompt 

        completion = client.chat.completions.create(  
            model=deployment,  
            messages=messages,
            max_tokens=100,  
            temperature=0.7,  
            top_p=0.95,  
            frequency_penalty=0,  
            presence_penalty=0,  
            stop=None,  
            stream=False  
        )  

        GPT_compare_result = completion.choices[0].message.content

        
        print(GPT_compare_result)
        return GPT_compare_result