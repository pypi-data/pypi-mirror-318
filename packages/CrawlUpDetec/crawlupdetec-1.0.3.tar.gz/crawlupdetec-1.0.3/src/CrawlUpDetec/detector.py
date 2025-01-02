import json 

from .diff_detect import diff_dect
from .new_crawler import new_crawl


def crawler_detect(ori_parse_text, new_html_file, old_html_file, azure_endpoint, azure_model, azure_key, azure_api_version):
    """
    1. detect whether "new_html" and "old_html" have different text:
    2. if text has been change, check whether "changed text" is related to what we parsed before:
            2.a. if "changed text" is related to what we parsed before:
                    [get new text's Xpath]
            2.b. if "changed text" is not related to what we parsed before: 
                    [get original text's Xpath]

    3. if text not change, means only ODM change. Then we get new Xpath for original parse text

    """
    
    dif_dect = diff_dect(new_html_file, 
                         old_html_file, 
                         azure_endpoint, 
                         azure_model, 
                         azure_key, 
                         azure_api_version)
    
    craw_result = new_crawl(new_html_file)

    # detect if html text change or not
    diff_list = dif_dect.compare_text()
    print('different text list: ' + str(diff_list))


    # if text has been change, check if changed text related to what we parsed before
    if diff_list:
        compare_result = dif_dect.GPT_text_meaning_compare(ori_parse_text, diff_list)
        print('compare_result: ' + compare_result)

        try:
            update_text = json.loads(compare_result)['result']

        except json.JSONDecodeError as e:
            print('GPT API parsing response Type Error! Try Again!!')
            print(f"JSON decode error: {e}")
            result = None
        

        # if changed text is related to what we parsed before, get new text's Xpath
        if update_text:
            print('different_detect! Parse by name')

            new_Xpath = craw_result.get_xpath_by_name(update_text)
            print('update Xpath: ' + new_Xpath)
            
            return new_Xpath

        # if changed text is not related to what we parsed before, don't need to update Xpath
        else:
            print("Don't need to parse new data! GPT thinks that the change of the texts does not related to what we want to parse.")

            ori_Xpath = craw_result.get_xpath_by_name(ori_parse_text)

            print('Original Xpath: ' + str(ori_Xpath))
            return ori_Xpath



    # if text not change, means only ODM change. Then we get new Xpath for original text
    else:
        print('Only ODM Change! Parse by name!')
        new_Xpath = craw_result.get_xpath_by_name(ori_parse_text)

        print('new Xpath: ' + str(new_Xpath))
        return new_Xpath


