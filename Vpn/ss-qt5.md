# [shadowsocks项目主页](https://github.com/shadowsocks)
## 安装依赖
	
> $ sudo apt-get install qt5-qmake qtbase5-dev libqrencode-dev libappindicator-dev libzbar-dev libbotan1.10-dev

## [安装libQtShadowsocks](https://github.com/shadowsocks/libQtShadowsocks)
### shadowsocks-qt5依赖于libQtShadowsocks,所以先安装libQtShadowsocks。

### 下载或clone libQtShadowsocks,项目根目录下执行:
	
> $ dpkg-buildpackage -uc -us -b

### 在上一级目录中生成三个deb包:
	
> libqtshadowsocks_1.8.0-1_amd64.deb  
> libqtshadowsocks-dev_1.8.0-1_amd64.deb  
> shadowsocks-libqtshadowsocks_1.8.0-1_amd64.deb

### 安装前两个即可
	
> $ sudo dpkg -i libqtshadowsocks_1.8.0-1_amd64.deb 
> $ sudo dpkg -i libqtshadowsocks-dev_1.8.0-1_amd64.deb 

## [安装shadowsocks-qt5](https://github.com/shadowsocks/shadowsocks-qt5)
### 下载或clone shadowsocks-qt5，项目根目录下执行:
	
> $ dpkg-buildpackage -uc -us -b

### 在上一级目录中生成：
	
> shadowsocks-qt5_2.6.0-1_amd64.deb

### 安装deb包
	
> $ sudo dpkg -i shadowsocks-qt5_2.6.0-1_amd64.deb

##安装完成。

# 全局代理配置
## 在.bashrc 中配置：
> export http_proxy=http://username:password@127.0.0.1:1080
## 刷新
> source .bashrc