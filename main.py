import random, os

song_list = []

print("Guebbb | v1.0")
f = input("载入文件: ")

with open(f"{f}.txt", "r", encoding="utf-8") as f:
    song_list.extend(f.read().splitlines())

# 选择的曲目数
song_count = int(input("曲目数量: "))

opened_letters = []
selected_songs = random.sample(song_list, song_count)
masked_songs = ["".join("*" if c != " " else c for c in song) for song in selected_songs]

while True:
    os.system("cls")
    
    for idx, song in enumerate(selected_songs):
        print(f"{idx + 1}= {song}")
    print("-----------")
    
    print(f"Guessed: {''.join(opened_letters)}")
    for idx, masked_song in enumerate(masked_songs):
        print(f"{idx + 1}. {masked_song}")

    user_input = input(">")

    if len(user_input) == 1:
        # 输入单个字母，解锁该字母
        for idx, song in enumerate(selected_songs):
            masked_songs[idx] = "".join(c if c.lower() == user_input.lower() else m for c, m in zip(song, masked_songs[idx]))
        if user_input.upper() not in opened_letters:
            opened_letters.append(user_input.upper())
        
    elif user_input.startswith("d"):
        ## 输入d加数字删曲
        masked_songs.remove(masked_songs[int(user_input[1:]) - 1])
        selected_songs.remove(selected_songs[int(user_input[1:]) - 1])
        
    elif user_input.startswith("o") and user_input[1:].isdigit():
        # 输入o加数字揭晓对应行的曲名
        index = int(user_input[1:]) - 1
        if 0 <= index < song_count:
            masked_songs[index] = selected_songs[index]
        else:
            print("无效的行号，请重新输入。")
    else:
        print("无效输入，请重新输入。")
