from bs4 import BeautifulSoup
import lxml.etree as ET


class new_crawl():

    def __init__(self, new_html):
        self.new_html = new_html
        

    def get_xpath_by_name(self, text_want2find):
        # 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(self.new_html, 'html.parser')
        
        # 尋找包含特定文字的所有標籤
        target_element = soup.find(string=lambda text: text and text_want2find in text)
        
        if not target_element:
            return None

        # 找到包含目標文字的標籤元素
        target_element = target_element.parent

        # 轉換成 lxml 尋找 XPath
        dom = ET.HTML(str(soup))
        element = dom.xpath(f"//*[contains(text(), '{text_want2find}')]" )
        
        if element:
            tree = ET.ElementTree(dom)
            return tree.getpath(element[0])
        else:
            return None
