# 一个拿来练手的Nyahentai每日本子下载

## 功能和特性
- 支持 `Github Actions` 每日运行，并自动上传 `cowtransfer` 以取回
- 爬取 Nyahentai 并获取首页上的所有本子的链接
- 内置 requests 和 aria2 两种可选的下载方式
- 内置更加简单易用的 aria2 配置文件
- 内置 manager ，对新手更加友好
- 新增 check 功能，可以检查本子下载的完整性
- 新增 screen 功能，可以筛选指定的 tag

## 使用入门

### Github Actions

fork本项目后对 `readme.md` 进行修改后，即可在每日的指定时间自动运行,可以从 `Upload bz` 中获取 `cowtransfer` 的下载链接

或者可以手动push来运行本项目

注：
- 本项目运行时间不稳定，从1~5小时不等，请耐心等待。
- `Github Actions` 下载的文件不一定完整，可在本地运行本项目进行补充

### Windows

下载 `aria2.exe` 文件并放置在项目根目录下，并在项目的根目录下运行 `manager.py` 即可

### Linux

这里仅列举 Ubuntu 的使用方法，其他系统同理

``` bash
git clone https://github.com/xiao-gy/daily_bz.git
sudo apt install aria2 -y
python3-pip install -r requirements.txt
python3 manager.py
```

### mac

使用方法与 windows 同理，自行尝试即可