# signin
python自动签到

1. 先抓包找到cookie 填到ser_cookies.json文件相应的地方
2. signin.py里设置定时
3. 后台运行脚本python -u query_lost_phone.py &
# 可能用到的命令：
1. 带日志：nohup python -u query_lost_phone.py > log.log 2>&1 &
2. 查看任务：ps -e | grep python
3. 结束任务：kill xxxx（查出来的ID）
