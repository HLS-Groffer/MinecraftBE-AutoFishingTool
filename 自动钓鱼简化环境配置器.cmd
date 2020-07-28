@echo off
chcp 65001
echo 自动钓鱼简化环境配置器
title 自动钓鱼简化环境配置器 by HLS-Groffer
echo 临时使用清华镜像升级pip
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
echo 临时使用清华镜像下载pyautogui包
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyautogui
echo 如果没报错的话就是安装完成了
pause