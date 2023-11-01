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
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-media-source")
    options.add_argument("--blink-settings=imagesEnabled=false")
    options.add_argument("--disable-javascript")
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    for url in url_chunk:
        driver.get(url.strip())
        champion = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="champInfo"]/div/div[1]/div[3]'))
        )
        champion_name = champion.text
        champion_name = str(champion_name).split(',')[0]

        print('챔피언 이름 : ', end='')
        print(champion_name)
        
        driver.execute_script("var elems = document.querySelectorAll('.primisslate, .vm-placement'); for (var i = 0; i < elems.length; i++) { elems[i].remove(); }")

        button_xpath = "/html/body/div[4]/div[1]/section/article/section[2]/div[2]/div/div/div[3]/div[2]/div[3]/span/span[3]/a"
        current_last_comment = 40
        texts = []
        continueable = True

        counter = 0
        j = 0

        while continueable:
            for i in range(1, current_last_comment + 1):
                try:
                    time.sleep(0.1)
                    comment_xpath = f'/html/body/div[4]/div[1]/section/article/section[2]/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[{i}]/td[2]/span/span'
                    element = driver.find_element(By.XPATH, comment_xpath)
                    texts.append(str(element.text).replace('\n', ' '))
                except NoSuchElementException:
                    break
            j=j+i
            try:
                counter += 1
                # 버튼 클릭 시도
                button = driver.find_element(By.XPATH, button_xpath)
                if not button.get_attribute("href"):  # 버튼의 href 속성이 없으면 다음 페이지로 이동할 수 없음
                    continueable = False
                else:
                    button.click()
                    time.sleep(2)  # 버튼 클릭 후 페이지 로딩 대기
            except NoSuchElementException:
                # 버튼이 없으면 다음 페이지로 이동할 수 없으므로 반복 종료
                print(f'{champion_name} click counter = {counter} / 댓글 : {j}')
                continueable = False
            
        # 댓글 수집이 끝난 후, 파일에 저장
        file_path = f"C:\\anaconda\\aiProject\\lol_project\\inven_champ_url\\{start_index + url_chunk.index(url):03}_{champion_name}_repl.txt"
        with open(file_path, 'w', encoding='utf-8') as file:
            for text in texts:
                file.write(text + ' ')

    driver.quit()

if __name__ == "__main__":
    # 파일 경로에서 모든 파일 리스트를 가져옵니다.
    files_in_directory = os.listdir("C:\\anaconda\\aiProject\\lol_project\\opgg_champ_url\\")
    # 세자리숫자_캐릭터이름_repl.txt 형식을 가진 파일들만 필터링합니다.
    filtered_files = [file for file in files_in_directory if file.endswith("_repl.txt") and file.split("_")[0].isdigit() and len(file.split("_")[0]) == 3]

    # 번호들을 추출합니다.
    existing_indices = [int(file.split("_")[0]) for file in filtered_files]

    with open("C:\\anaconda\\aiProject\\lol_project\\opgg_champ_url\\lol_addresses.txt", "r") as file:
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
