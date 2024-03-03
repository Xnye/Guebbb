**Guebbb** - 音游开字母辅助工具『自用』

支持开中日韩文等全角字符 支持答案显示/已开字母大小写/自动复制 *（使用记事本等软件编辑main.py设置区）（自动复制需要安装`pyperclip`第三方库）*

「食用方法」

文件名输入p就从p.txt里面抽曲子 *（无需".txt"后缀，仅限同级目录，一行一首曲）*

输入 **单字母** → 解该字母

输入 **o加序号** → 揭晓对应行曲名

输入 **d加序号** → 删曲

输入 **^加曲名** → 新增曲目 *（多曲目用^分隔）*

「运行环境」

需要 **Python3** 环境 *（下载 → <https://python.org>）*

使用自动复制功能需要第三方库 pyperclip *（下载 → Win+R运行cmd打开终端输入`pip install pyperclip`）*

「文件说明」

① **main.py** = 主程序 ② **ab.txt** = Arcaea 5.2 仅Beyond曲 ③ **af.txt** = Arcaea 5.2 全曲 ④ **p.txt** = Phigros 3.5 全曲

「演示」

初始化页面

``` 
Guebbb | v1.4
需要加载曲库, 无需.txt后缀, 仅限同级目录.
留空并回车来手动导入曲子.
载入文件: ab
当前曲库共有 39 首曲子.
曲目数量: 5
``` 

猜曲页面
``` 
1= Pentiment
2= Heavensdoor
3= trappola bewitching
4= Testify
5= Arcana Eden
-----------
Guessed: ABの.DEOI
1. *e**i*e**
2= Heavensdoor
3. **a**o*a be*i***i**
4. *e**i**
5= Arcana Eden
>
```

「Todo」

内置词库 中日文屏蔽 已猜曲目隐藏 ......

便捷功能使用说明等内容正在完善中