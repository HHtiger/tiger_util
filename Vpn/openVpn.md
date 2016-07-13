安装配置参照基础流程，之后会出现vpn可以连接，但是却无法上网。纠结了一天。
原因是路由转发的问题：
就是把iptables的转发规则中的 -o eth0 去掉，即：
iptables -t nat -A POSTROUTING -s 10.8.0.0/24  -j MASQUERADE
然后
/etc/init.d/iptables save
还不行就清空所有规则
iptables -F , iptables -X iptables -Z, 然后iptables -t nat -A POSTROUTING -s 10.8.0.0/24  -j MASQUERADE, /etc/init.d/iptables save
搞定！
基本设置参照http://blog.csdn.net/liuyuyefz/article/details/47184425
你可以从 EPEL仓库获取OpenVPN. 如果你没有安装过这个支持，你需要先做如下步骤：

wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm  
rpm -Uvh epel-release-6*.rpm  

安装 OpenVPN:


yum -y install openvpn easy-rsa  
如果你上面步骤出错可以尝试如下方案之后再重新尝试安装：

运行命令来升级repo 以便可以使用 HTTP 而不是 HTTPS:
sudo sed -i "s/mirrorlist=https/mirrorlist=http/" /etc/yum.repos.d/epel.repo  

然后确认一下更新:
yum check-update  

找到文件夹 /etc/openvpn 创建一个 server.conf:
port 1194  
proto udp  
dev tun  
ca ca.crt  
cert server.crt  
key server.key  
dh dh2048.pem  
server 10.8.0.0 255.255.255.0  
ifconfig-pool-persist ipp.txt  
push "redirect-gateway def1 bypass-dhcp"  
push "dhcp-option DNS 8.8.8.8"  
push "dhcp-option DNS 8.8.4.4"  
keepalive 10 120  
comp-lzo  
max-clients 100  
user nobody  
group nobody  
persist-key  
persist-tun  
status /var/log/openvpn-status.log  
log-append /var/log/openvpn.log  
verb 3  

现在来创建一个服务器证书. 
mkdir -p /etc/openvpn/easy-rsa/keys  
cp -r /usr/share/easy-rsa/2.0/* /etc/openvpn/easy-rsa/  
cd /etc/openvpn/easy-rsa  
source ./vars  
./clean-all  
./build-ca  
./build-key-server server  
./build-dh  

所有的选项让它默认就好如果有出现 [y/n] 的询问就输入 y 然后回车.

下一步我们来做一个客户端的证书:

./build-key client1  

Everything is similar. If you want multiple clients, the operation is repeated several times, changing client1 on client2, client3 and so on.
如果你想做多个客户端认证参考这个步骤就好了比如想要做client2, client3 按照client1的步骤就可以。

拷贝所有的key:

cd keys/  
cp dh2048.pem ca.crt server.crt server.key /etc/openvpn  
修改一下 /etc/sysctl.conf 文件里面的IP Forwarding

net.ipv4.ip_forward = 0  
改为

net.ipv4.ip_forward = 1  
把设置好的东西提交一下:

sysctl -p  

编辑 Iptables, SERVER-IP 这边记住要替换成你自己的服务器 IP 地址.

iptables -t nat -A POSTROUTING -o venet0 -j SNAT --to SERVER-IP  
iptables -A FORWARD -i venet0 -o tun0 -m state --state RELATED,ESTABLISHED -j ACCEPT  
iptables -A FORWARD -i tun0 -o venet0 -j ACCEPT  
上面其实就完成了所有 VPS OpenVZ的设置, 但是要做一个独立运行OpenVPN服务器还需要一下步骤:

iptables -A FORWARD -s 10.8.0.0/24 -j ACCEPT  
iptables -A FORWARD -m state --state RELATED,ESTABLISHED -j ACCEPT  
iptables -t nat -A POSTROUTING -s 10.8.0.0/24 -o eth0 -j MASQUERADE  （有问题）

保存设置然后重启iptables: 

service iptables save  
service iptables restart  
开启OpenVPN 服务器 然后让它开机启动: 

service openvpn start  
chkconfig openvpn on  

以上服务端的设置就完成了，我们现在来配置客户端
你可以下载Openvpn的客户端软件再这里下载对应的版本就好了 the official site, 

然后从服务器上拷贝如下三个文件：

/etc/openvpn/ca.crt  
  
/etc/openvpn/easy-rsa/keys/client1.crt   
  
/etc/openvpn/easy-rsa/keys/client1.key  

到你本地的电脑上（window电脑在安装好OpenVPN软件后可以把如上证书拷贝到如下文件夹里C:\Program Files\OpenVPN\config ）
然后在这个文件夹创建一个 client.ovpn 文件内如如下, 其他不用改只要把SERVER-IP 改成你服务器的 IP  

client  
dev tun  
proto udp  
remote SERVER-IP 1194  
resolv-retry infinite  
nobind  
persist-key  
persist-tun  
ca ca.crt  
cert client1.crt  
key client1.key  
ns-cert-type server  
comp-lzo  
verb 3  
sndbuf 0  
rcvbuf 0  