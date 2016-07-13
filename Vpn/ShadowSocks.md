使用root登陆ssh（工具putty.exe)后安装shadowsocks:

wget --no-check-certificate https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks-go.sh
chmod +x shadowsocks-go.sh
./shadowsocks-go.sh 2>&1 | tee shadowsocks-go.log
安装完成后，脚本提示如下：

Congratulations, shadowsocks-go install completed!
Your Server IP:your_server_ip
Your Server Port:your_server_port
Your Password:your_password
Your Local Port:1080
Your Encryption Method:aes-256-cfb
Welcome to visit:http://teddysun.com/392.html
Enjoy it!
安装完成后即已后台启动shadowsocks-go，运行：

/etc/init.d/shadowsocks status
可以查看 shadowsocks-go 进程是否已经启动。

卸载方法：

使用 root 用户登录，运行以下命令：

./shadowsocks-go.sh uninstall
本脚本安装完成后，已将 shadowsocks-go 加入开机自启动。

修改用户配置文件（/etc/shadowsocks/config.json）：
{
    "server":"0.0.0.0",
    "port_password":{
         "8989":"password0",
         "9001":"password1",
         "9002":"password2",
         "9003":"password3",
         "9004":"password4"
    },
    "method":"aes-256-cfb",
    "timeout":600
}

使用命令：

启动：/etc/init.d/shadowsocks start
停止：/etc/init.d/shadowsocks stop
重启：/etc/init.d/shadowsocks restart
状态：/etc/init.d/shadowsocks status