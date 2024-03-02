import random, os, time

##### 设置区 #####

# 是否启用已开字母大写 (True/False)
enable_upper = True
# 是否显示答案 (True/False)
display_answer = True
# 错误提示持续时间 (秒)
sleep_time = 0.5
# 屏蔽符号 (字符)
star_char = "*"

def prints(text, dur):
    print(text)
    time.sleep(dur)

while True:
    os.system("cls")
    print("Guebbb | v1.3")
    f = input("载入文件: ")
    song_list = []
    try:
        with open(f"{f}.txt", "r", encoding="utf-8") as f:
            song_list.extend(f.read().splitlines())
    except:
        prints("文件不存在或无法读取", sleep_time)
        continue

    try:
        song_count = int(input("曲目数量: "))
        opened_letters = []
        songname_list = random.sample(song_list, song_count)
        songstatus_list = [0 for _ in songname_list]
        break
    except:
        prints("输入应小于等于曲库曲目数量", sleep_time)
        continue

while True:
    os.system("cls")
    
    # 显示答案
    if display_answer:
        for i, song in enumerate(songname_list):
            print(f"{i + 1}= {song}")
        print("-----------")
        
    # 主要页面
    print(f"Guessed: {"".join(opened_letters)}")
    maskedsong_list = ["".join(char if (char == " " or (char.upper() if enable_upper else char.lower()) in opened_letters) else star_char for char in song) for song in songname_list]
    for i, masked_song in enumerate(maskedsong_list):
        # 如果字母已经全开则判断为揭晓状态
        if songname_list[i] == masked_song:
            songstatus_list[i] = 1
            
        # 如果曲目已揭晓显示曲名，否则显示掩码
        if songstatus_list[i] == 1:
            print(f"{i + 1}= {songname_list[i]}")
        else:
            print(f"{i + 1}. {masked_song}")
    
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