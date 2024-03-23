import random, os, time

##### 设置区 #####

# ★ 是否自动复制 (True/False)
enable_copy = False
# 是否启用已开字母大写 (True/False)
enable_upper = True
# 是否显示答案 (True/False)
enable_answer = True
# 错误提示持续时间 (秒)
sleep_time = 0.5
# 掩码符号 (字符)
star_char = "*"

if enable_copy: from pyperclip import copy

def prints(text, dur):
    print(text)
    time.sleep(dur)

while True:
    os.system("cls")
    print("Guebbb | v1.4")
    print("需要加载曲库, 无需.txt后缀, 仅限同级目录.")
    print("留空并回车来手动导入曲子.")
    
    f = input("载入文件: ")
    song_list = []
    opened_letters = []
    if f != "":
        try:
            with open(f"{f}.txt", "r", encoding="utf-8") as f:
                song_list.extend(f.read().splitlines())
        except:
            prints("文件不存在或无法读取", sleep_time)
            continue
        
        print(f"当前曲库共有 {len(song_list)} 首曲子.")
        
        try:
            song_count = int(input("曲目数量: "))
            songname_list = random.sample(song_list, song_count)
            songstatus_list = [0 for _ in songname_list]
            break
        except:
            prints("输入应小于等于曲库曲目数量", sleep_time)
            continue
    else:
        songname_list = []
        songstatus_list = []
        prints("手动导入模式开启", 0.75)
        break

while True:
    os.system("cls")
    
    # 显示答案
    if enable_answer:
        for i, song in enumerate(songname_list):
            print(f"{i + 1}= {song}")
        print("-----------")
        
    # 主要页面
    main_page: str = ""
    main_page += f"Guessed: {"".join(opened_letters)}\n"
    maskedsong_list = ["".join(char if (char == " " or (char.upper() if enable_upper else char.lower()) in opened_letters) else star_char for char in song) for song in songname_list]
    for i, masked_song in enumerate(maskedsong_list):
        # 如果字母已经全开则判断为揭晓状态
        if songname_list[i] == masked_song:
            songstatus_list[i] = 1
            
        # 如果曲目已揭晓显示曲名，否则显示掩码
        if songstatus_list[i] == 1:
            main_page += f"{i + 1}= {songname_list[i]}\n"
        else:
            main_page += f"{i + 1}. {masked_song}\n"
    main_page = main_page[:-1]
    print(main_page)
    if enable_copy: copy(main_page)
    
    # 处理输入
    try:
        user_input = input(">")

        if len(user_input) == 1:
            # 输入单个字母，解锁该字母
            user_input_case = user_input.upper() if enable_upper else user_input.lower()
            if user_input_case not in opened_letters:
                opened_letters.append(user_input_case)
            
        elif user_input.startswith("d") and user_input[1:].isdigit():
            ## 输入d加数字删曲
            songname_list.pop(int(user_input[1:]) - 1)
            songstatus_list.pop(int(user_input[1:]) - 1)
            
        elif user_input.startswith("o") and user_input[1:].isdigit():
            # 输入o加数字揭晓对应行的曲名
            songstatus_list[int(user_input[1:]) - 1] = 1
        
        elif user_input.startswith("^") and user_input[1:] != None:
            # 输入^加曲名新增曲目 支持多个曲目用^分隔
            new_songs = user_input[1:].split("^")
            songname_list.extend(new_songs)
            songstatus_list.extend([0 for _ in new_songs])
        
        else: prints("无效输入", sleep_time)
    except:
        prints("检查你的输入", sleep_time)
        continue
