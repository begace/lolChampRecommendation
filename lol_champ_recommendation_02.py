# 크롤링한 파일 합치기
import os

directory_path = "G:\\aiProject\\lol_project\\inven_champ_url\\"
output_file = "champ_repl.txt"

# 해당 디렉터리에 있는 파일 리스트를 가져옵니다.
file_list = os.listdir(directory_path)

# 파일 이름이 000_name_repl.txt 형식인 파일만 선택합니다.
selected_files = [f for f in file_list if f.endswith("_repl.txt") and f.split('_')[0].isdigit() and len(f.split('_')[0]) == 3]

with open(output_file, 'w', encoding='utf-8') as out_file:
    for file_name in selected_files:
        champ_name = file_name.split('_')[1]
        with open(directory_path + file_name, 'r', encoding='utf-8') as in_file:
            content = in_file.read().replace('\n', ', ')
            print(f"{champ_name}, {content[:10]}")
            out_file.write(f"{champ_name}, {content.replace(',', ' ')}\n")
