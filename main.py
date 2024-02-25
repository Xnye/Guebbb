import random, os, time

##### 设置区 #####

# 是否启用已开字母大写
enable_upper = True
# 是否显示答案
display_answer = True
# 错误提示持续时间 (秒)
sleep_time = 0.5

def prints(text, dur):
    print(text)
    time.sleep(dur)

while True:
    os.system("cls")
    print("Guebbb | v1.2")
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
        selected_songs = random.sample(song_list, song_count)
        break
    except:
        prints("输入应小于等于曲库曲目数量", sleep_time)
        continue

masked_songs = ["".join("*" if c != " " else c for c in song) for song in selected_songs]

while True:
    os.system("cls")
    
    # 显示答案
    if display_answer:
        for i, song in enumerate(selected_songs):
            print(f"{i + 1}= {song}")
        print("-----------")
        
    # 主要页面
    print(f"Guessed: {''.join(opened_letters)}")
    for i, masked_song in enumerate(masked_songs):
        print(f"{i + 1}. {masked_song}")
    
    # 处理输入
    try:
        user_input = input(">")

        if len(user_input) == 1:
            # 输入单个字母，解锁该字母
            for i, song in enumerate(selected_songs):
                masked_songs[i] = "".join(c if c.lower() == user_input.lower() else m for (c, m) in zip(song, masked_songs[i]))
            user_input_case = user_input.upper() if enable_upper else user_input.lower()
            if user_input_case not in opened_letters:
                opened_letters.append(user_input_case)
            
        elif user_input.startswith("d") and user_input[1:].isdigit():
            ## 输入d加数字删曲
            try:
                masked_songs.remove(masked_songs[int(user_input[1:]) - 1])
                selected_songs.remove(selected_songs[int(user_input[1:]) - 1])
            except IndexError: prints("无效行号", sleep_time)
            
        elif user_input.startswith("o") and user_input[1:].isdigit():
            # 输入o加数字揭晓对应行的曲名
            index = int(user_input[1:]) - 1
            if 0 <= index < song_count:
                masked_songs[index] = selected_songs[index]
            else: prints("无效行号", sleep_time)
        
        elif user_input.startswith("^") and user_input[1:] != None:
            # 输入^加曲名新增曲目 支持多个曲目用^分隔
            new_songs = user_input[1:].split("^")
            selected_songs.extend(new_songs)
            masked_songs.extend(["".join(c if (c.upper() if enable_upper else c.lower()) in opened_letters else "*" for c in song) for song in new_songs])
        
        else: prints("无效输入", sleep_time)
    except:
        prints("检查你的输入", sleep_time)
        continue