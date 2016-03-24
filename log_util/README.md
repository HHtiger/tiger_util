筛选项目后台日志sql语句，还原sql
select * from xxx where id = ?
[1]
==>
select * from xxx where id = 1

step1:将控制台日志copy至log文件内
step2:执行:python log_filter.py
step3:在res内查看sql语句_ 