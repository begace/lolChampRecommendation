import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import time
import math
import sys


def process_urls(url_chunk, start_index):
    print('프로세스 번호 ',start_index)
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-media-source")
    options.add_argument("--blink-settings=imagesEnabled=false")
    options.add_argument("--disable-javascript")
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    for url in url_chunk:
        champion_name = url.split("champions/")[1].split("/build")[0]
        driver.get(url)
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, button_xpath)))
        time.sleep(5)
        driver.execute_script("var elems = document.querySelectorAll('.primisslate, .vm-placement'); for (var i = 0; i < elems.length; i++) { elems[i].remove(); }")

        button_xpath = "//button[@type='button' and @class='css-5e1aqy e1nhwouu1']"
        current_last_comment = 0
        
        while True:
            try:
                # 예외가 발생하면 최대 3번까지 다시 시도
                for _ in range(3):
                    try:
                        try:
                            button_xpath = f'/html/body/div[1]/div[5]/div/main/div[6]/div/div/div/div/div[2]/button'
                            button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
                        except:
                            button_xpath = f'/html/body/div[1]/div[5]/div/main/div[7]/div/div/div/div/div[2]/button'
                            button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
                        driver.execute_script("arguments[0].click();", button)
                        break
                    except StaleElementReferenceException:
                        time.sleep(0.5)
                        continue
                for i in range(current_last_comment + 10, current_last_comment, -1):
                    try:
                        try:
                            try:
                                comment_xpath = f'//*[@id="content-container"]/main/div[6]/div/div/div/div/div[2]/ul/li[{i}]/div[2]/p'
                                driver.find_element(By.XPATH, comment_xpath)
                            except:
                                comment_xpath = f'//*[@id="content-container"]/main/div[7]/div/div/div/div/div[2]/ul/li[{i}]/div[2]/p'
                                driver.find_element(By.XPATH, comment_xpath)
                        except:
                            print(f"{champion_name} {i}번째 댓글 읽다가 오류남 ㅋ")
                            break
                            #sys.exit()
                        current_last_comment = i
                        break
                    except NoSuchElementException:
                        continue
            except TimeoutException:
                break
            except StaleElementReferenceException:
                continue

        texts = []
        for i in range(1, current_last_comment + 1):
            try:
                try:
                    try:
                        comment_xpath = f'//*[@id="content-container"]/main/div[6]/div/div/div/div/div[2]/ul/li[{i}]/div[2]/p'
                        element = driver.find_element(By.XPATH, comment_xpath)
                    except:
                        comment_xpath = f'//*[@id="content-container"]/main/div[7]/div/div/div/div/div[2]/ul/li[{i}]/div[2]/p'
                        element = driver.find_element(By.XPATH, comment_xpath)
                except:
                    print(f"{champion_name} 텍스트 읽는 과정 중 {i}번째 댓글 읽다가 오류남 ㅋ")
                    break
                    #sys.exit()
                #print(element.text)
                texts.append(element.text.replace('\n', ' '))
            except NoSuchElementException:
                break

        file_path = f"./opgg_champ_url/{start_index + url_chunk.index(url):03}_{champion_name}_repl.txt"
        with open(file_path, 'w', encoding='utf-8') as file:
            for text in texts:
                file.write(text + ' ')

    driver.quit()

if __name__ == "__main__":
    # 파일 경로에서 모든 파일 리스트를 가져옵니다.
    files_in_directory = os.listdir("./opgg_champ_url/")
    # 세자리숫자_캐릭터이름_repl.txt 형식을 가진 파일들만 필터링합니다.
    filtered_files = [file for file in files_in_directory if file.endswith("_repl.txt") and file.split("_")[0].isdigit() and len(file.split("_")[0]) == 3]

    # 번호들을 추출합니다.
    existing_indices = [int(file.split("_")[0]) for file in filtered_files]

    with open("./opgg_champ_url/lol_addresses.txt", "r") as file:
        urls = [url.strip() for url in file.readlines()]

    # 빈 번호들을 확인합니다.
    missing_indices = [i for i in range(len(urls)) if i not in existing_indices]
    print(f'빈 번호 {missing_indices}')

    # 빈 번호에 해당하는 URL만을 가져옵니다.
    missing_urls = [urls[i] for i in missing_indices]

    num_threads = 5
    chunk_size = math.ceil(len(missing_urls) / num_threads)

    # 빈 번호에 해당하는 URL 목록을 동일한 크기의 청크로 분할
    url_chunks = [missing_urls[i:i + chunk_size] for i in range(0, len(missing_urls), chunk_size)]
    
    print('프로세스 시작')
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        for index, chunk in enumerate(url_chunks):
            # 각 청크의 시작 인덱스는 빈 번호의 시작 인덱스입니다.
            executor.submit(process_urls, chunk, missing_indices[index * chunk_size])

    print(f"Program finished at {datetime.now()}")