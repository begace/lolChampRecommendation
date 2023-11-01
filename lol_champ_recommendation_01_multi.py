{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium import webdriver\n",
    "from selenium.webdriver.common.by import By\n",
    "from selenium.webdriver.support.ui import WebDriverWait\n",
    "from selenium.webdriver.support import expected_conditions as EC\n",
    "from selenium.common.exceptions import NoSuchElementException\n",
    "import time\n",
    "\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "from selenium.webdriver.chrome.service import Service as ChromeService\n",
    "import pandas as pd\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "ename": "ElementClickInterceptedException",
     "evalue": "Message: element click intercepted: Element <button type=\"button\" class=\"css-5e1aqy e1nhwouu1\">...</button> is not clickable at point (370, 845). Other element would receive the click: <div class=\"vm-footer-content\">...</div>\n  (Session info: chrome=118.0.5993.118)\nStacktrace:\n\tGetHandleVerifier [0x00E94DE3+43907]\n\t(No symbol) [0x00E20741]\n\t(No symbol) [0x00D133ED]\n\t(No symbol) [0x00D4B5B1]\n\t(No symbol) [0x00D4A0AF]\n\t(No symbol) [0x00D4869B]\n\t(No symbol) [0x00D47A35]\n\t(No symbol) [0x00D3FF9A]\n\t(No symbol) [0x00D62B5C]\n\t(No symbol) [0x00D3F9D6]\n\t(No symbol) [0x00D62DD4]\n\t(No symbol) [0x00D755CA]\n\t(No symbol) [0x00D62956]\n\t(No symbol) [0x00D3E17E]\n\t(No symbol) [0x00D3F32D]\n\tGetHandleVerifier [0x01145AF9+2865305]\n\tGetHandleVerifier [0x0118E78B+3163435]\n\tGetHandleVerifier [0x01188441+3138017]\n\tGetHandleVerifier [0x00F1E0F0+605840]\n\t(No symbol) [0x00E2A64C]\n\t(No symbol) [0x00E26638]\n\t(No symbol) [0x00E2675F]\n\t(No symbol) [0x00E18DB7]\n\tBaseThreadInitThunk [0x772BFCC9+25]\n\tRtlGetAppContainerNamedObjectPath [0x77B87C6E+286]\n\tRtlGetAppContainerNamedObjectPath [0x77B87C3E+238]\n",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mElementClickInterceptedException\u001b[0m          Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\ipykernel_20328\\463942313.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     26\u001b[0m     \u001b[1;31m# 버튼 클릭\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     27\u001b[0m     \u001b[0mbutton\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mWebDriverWait\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdriver\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m10\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0muntil\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mEC\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0melement_to_be_clickable\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mBy\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mXPATH\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mbutton_xpath\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 28\u001b[1;33m     \u001b[0mbutton\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mclick\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     29\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     30\u001b[0m     \u001b[1;31m# 새롭게 로딩된 마지막 댓글의 번호 검사\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\Users\\TFG266\\.conda\\envs\\movieRecommendation\\lib\\site-packages\\selenium\\webdriver\\remote\\webelement.py\u001b[0m in \u001b[0;36mclick\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m     92\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mclick\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m->\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     93\u001b[0m         \u001b[1;34m\"\"\"Clicks the element.\"\"\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 94\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_execute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mCLICK_ELEMENT\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     95\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     96\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0msubmit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\Users\\TFG266\\.conda\\envs\\movieRecommendation\\lib\\site-packages\\selenium\\webdriver\\remote\\webelement.py\u001b[0m in \u001b[0;36m_execute\u001b[1;34m(self, command, params)\u001b[0m\n\u001b[0;32m    393\u001b[0m             \u001b[0mparams\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m{\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    394\u001b[0m         \u001b[0mparams\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"id\"\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_id\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 395\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_parent\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcommand\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    396\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    397\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mfind_element\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mby\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mBy\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mID\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m->\u001b[0m \u001b[0mWebElement\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\Users\\TFG266\\.conda\\envs\\movieRecommendation\\lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[1;34m(self, driver_command, params)\u001b[0m\n\u001b[0;32m    343\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    344\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 345\u001b[1;33m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    346\u001b[0m             \u001b[0mresponse\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"value\"\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_unwrap_value\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"value\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    347\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\Users\\TFG266\\.conda\\envs\\movieRecommendation\\lib\\site-packages\\selenium\\webdriver\\remote\\errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[1;34m(self, response)\u001b[0m\n\u001b[0;32m    227\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"alert\"\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"text\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    228\u001b[0m             \u001b[1;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[1;33m)\u001b[0m  \u001b[1;31m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 229\u001b[1;33m         \u001b[1;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mElementClickInterceptedException\u001b[0m: Message: element click intercepted: Element <button type=\"button\" class=\"css-5e1aqy e1nhwouu1\">...</button> is not clickable at point (370, 845). Other element would receive the click: <div class=\"vm-footer-content\">...</div>\n  (Session info: chrome=118.0.5993.118)\nStacktrace:\n\tGetHandleVerifier [0x00E94DE3+43907]\n\t(No symbol) [0x00E20741]\n\t(No symbol) [0x00D133ED]\n\t(No symbol) [0x00D4B5B1]\n\t(No symbol) [0x00D4A0AF]\n\t(No symbol) [0x00D4869B]\n\t(No symbol) [0x00D47A35]\n\t(No symbol) [0x00D3FF9A]\n\t(No symbol) [0x00D62B5C]\n\t(No symbol) [0x00D3F9D6]\n\t(No symbol) [0x00D62DD4]\n\t(No symbol) [0x00D755CA]\n\t(No symbol) [0x00D62956]\n\t(No symbol) [0x00D3E17E]\n\t(No symbol) [0x00D3F32D]\n\tGetHandleVerifier [0x01145AF9+2865305]\n\tGetHandleVerifier [0x0118E78B+3163435]\n\tGetHandleVerifier [0x01188441+3138017]\n\tGetHandleVerifier [0x00F1E0F0+605840]\n\t(No symbol) [0x00E2A64C]\n\t(No symbol) [0x00E26638]\n\t(No symbol) [0x00E2675F]\n\t(No symbol) [0x00E18DB7]\n\tBaseThreadInitThunk [0x772BFCC9+25]\n\tRtlGetAppContainerNamedObjectPath [0x77B87C6E+286]\n\tRtlGetAppContainerNamedObjectPath [0x77B87C3E+238]\n"
     ]
    }
   ],
   "source": [
    "\n",
    "# ChromeOptions 객체를 생성\n",
    "options = webdriver.ChromeOptions()\n",
    "\n",
    "# 미디어 스트림과 이미지 로딩 비활성화\n",
    "options.add_argument(\"--disable-media-source\")\n",
    "options.add_argument(\"--blink-settings=imagesEnabled=false\")\n",
    "options.add_argument(\"--disable-javascript\")\n",
    "\n",
    "# WebDriver 설정\n",
    "service = ChromeService(executable_path=ChromeDriverManager().install())\n",
    "driver = webdriver.Chrome(service=service, options=options)\n",
    "\n",
    "# 웹 페이지 로드\n",
    "url = 'https://www.op.gg/champions/garen/build/top?region=global&tier=emerald_plus'\n",
    "driver.get(url)\n",
    "\n",
    "# 광고와 관련된 요소 제거\n",
    "driver.execute_script(\"var elems = document.querySelectorAll('.primisslate, .vm-placement'); for (var i = 0; i < elems.length; i++) { elems[i].remove(); }\")\n",
    "\n",
    "# 버튼 클릭을 위한 XPath\n",
    "button_xpath = '//*[@id=\"content-container\"]/main/div[6]/div/div/div/div/div[2]/button'\n",
    "\n",
    "# 현재 로딩된 마지막 댓글의 번호\n",
    "current_last_comment = 0\n",
    "while current_last_comment < 990:  # 최대 990번째 댓글까지 검사하면서 버튼 클릭\n",
    "    # 버튼 클릭\n",
    "    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))\n",
    "    button.click()\n",
    "    \n",
    "    # 새롭게 로딩된 마지막 댓글의 번호 검사\n",
    "    for i in range(current_last_comment + 10, current_last_comment, -1):\n",
    "        try:\n",
    "            # 댓글 요소 확인\n",
    "            comment_xpath = f'//*[@id=\"content-container\"]/main/div[6]/div/div/div/div/div[2]/ul/li[{i}]/div[2]/p'\n",
    "            driver.find_element(By.XPATH, comment_xpath)\n",
    "            current_last_comment = i\n",
    "            break\n",
    "        except NoSuchElementException:\n",
    "            continue\n",
    "\n",
    "# 1부터 1000까지의 텍스트 정보를 수집\n",
    "texts = []\n",
    "for i in range(1, 1001):\n",
    "    element_xpath = f'//*[@id=\"content-container\"]/main/div[6]/div/div/div/div/div[2]/ul/li[{i}]/div[2]/p'\n",
    "    element = driver.find_element(By.XPATH, element_xpath)\n",
    "    texts.append(element.text)\n",
    "\n",
    "# 드라이버 종료\n",
    "driver.quit()\n",
    "\n",
    "# 텍스트 정보를 파일로 저장\n",
    "file_path = \"/opgg_champ_url/garen_repl.txt\"\n",
    "with open(file_path, 'w', encoding='utf-8') as file:\n",
    "    for text in texts:\n",
    "        file.write(text + '\\n')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "movieRecommendation",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.16"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
