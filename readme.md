# Nhentai每日本子下载

[![GitHub Stars](https://img.shields.io/github/stars/xiao-gy/daily-bz.svg?style=flat-square&label=Stars&logo=github)](https://github.com/xiao-gy/daily-bz/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/xiao-gy/daily-bz.svg?style=flat-square&label=Forks&logo=github)](https://github.com/xiao-gy/daily-bz/fork)

## 提示
由于近期 `Nyahentai` 及其镜像站关停，现转为爬取 `Nhentai` 之内容，原先代码可在 `nyahentai` 分支下使用。

本程序暂未直接代理，需要本地运行者可以到 `get.py` 文件自己取消相关代码注释。

## 运行状态
[![Getting daily bz](https://github.com/xiao-gy/daily-bz/actions/workflows/daily-bz.yml/badge.svg)](https://github.com/xiao-gy/daily-bz/actions/workflows/daily-bz.yml)

## 功能和特性
- 支持 `Github Actions` 每日运行，并自动上传阿里云盘
- 爬取 Nhentai 并获取首页上的所有本子的链接
- ~~内置 requests 和 aria2 两种可选的下载方式~~
- 内置更加简单易用的 aria2 配置文件
- 内置 manager ，对新手更加友好
- 新增 check 功能，可以检查本子下载的完整性
- 新增 screen 功能，可以筛选指定的 tag

## 使用入门

### Github Actions

fork本项目后对 `readme.md` 进行修改后，即可在每日的指定时间自动运行。会自动上传至阿里网盘，所以请在设置内配置阿里网盘的 `REFRESH_TOKEN` ，并将其命名为 `ALIYUNPAN_TOKEN`。

<details>
<summary>设置方法</summary>
<br>

![image.png](https://s2.loli.net/2022/04/09/Vil9qXL45GWmdr1.png)

![image.png](https://s2.loli.net/2022/04/09/GLFCQ14OHnt2eTx.png)

不知道怎么获取 `REFRESH_TOKEN` ? 前往 [tickstep/aliyunpan](https://github.com/tickstep/aliyunpan#1-%E5%A6%82%E4%BD%95%E8%8E%B7%E5%8F%96RefreshToken) 了解

</details>

你可以手动 push 来运行本项目

注：
- 本项目运行时间不稳定，从0~5小时不等，请耐心等待
- `Github Actions` 下载的文件不一定完整 ~~基本就没完整过~~ ，可在本地运行本项目进行补全

### Windows

``` bash
pip install -r requirements.txt
python3 manager.py
```

请执行以上命令安装依赖，然后下载 `aria2.exe` 文件并放置在项目根目录下，并在项目根目录下运行 `manager.py` 即可


### Linux

这里仅列举 Ubuntu系统 下的使用方法，其他系统同理

``` bash
git clone https://github.com/xiao-gy/daily-bz.git && cd ./daily_bz
sudo apt install aria2 -y
python3-pip install -r requirements.txt
python3 manager.py
```

### mac

使用方法与以上两个系统同理，自行尝试即可

## 鸣谢

- [ P3TERX/aria2.conf ](https://github.com/P3TERX/aria2.conf) 
采用了此项目的aria2配置脚本，并根据需要进行了修改

- [ tickstep/aliyunpan ](https://github.com/tickstep/aliyunpan)
采用了此项目作为Action的上传脚本，感谢开发者

## 最后的话

~~还请各位务必节制一点~~
