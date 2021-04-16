# 一个拿来练手的Nyahentai每日本子下载

## 功能和特性
- 爬取 Nyahentai 并获取首页上的所有本子的链接
- 内置 requests 和 aria2 两种可选的下载方式
- 内置更加简单易用的 aria2 配置文件
- 新增check功能，可以检查本子下载的完整性

## 使用入门

### Windows

下载 `aria2.exe` 文件并放置在项目根目录下，并在项目的根目录下运行 `main.py` 即可

### Linux

这里仅列举Ubuntu的使用方法，其他系统同理

```bash
git clone https://github.com/xiao-gy/daily_bz.git
sudo apt install aria2 -y
python3-pip install -r requirements.txt
python3 main.py
```

### mac

使用方法与windows同理，自行尝试即可