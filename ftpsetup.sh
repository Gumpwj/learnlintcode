#!/bin/bash
# by liuhx 2013-Nov-04.
# 设置ftp环境的脚本。ftp的根目录为只读，其下的writable目录为可写

# 可自定义以下四项
# ftp用户名
userName="test"
# ftp密码
password="test"
# ftp根目录，末尾不要加/
ftp_dir="$HOME/ftp"
# 可写目录的目录名
writable="writable"


# 如果没有加sudo，提示错误并退出
if [ "x$(id -u)" != x0 ]; then  
  echo "Error: please run this script with 'sudo'."  
  exit 1
fi

# 核心工具，vsftpd。 -y是对所有提示都回答yes
sudo yum  install vsftpd -y
# db-util是用来生成用户列表数据库的工具
sudo yum  install db-util -y

# 以下步骤参考https://help.ubuntu.com/community/vsftpd#The_workshop
# 创建用户名和密码的数据库，以单数行为用户名，双数行为密码记录
cd /tmp
printf "$userName\n$password\n" > vusers.txt
db_load -T -t hash -f vusers.txt vsftpd-virtual-user.db
sudo cp -f vsftpd-virtual-user.db /etc/
cd /etc
chmod 600 vsftpd-virtual-user.db
if [ ! -e vsftpd.conf.old ]; then
	sudo cp -f vsftpd.conf vsftpd.conf.old
fi

# 创建PAM file。bash的here-document，直接输出这些内容覆盖原文件
(sudo cat <<EOF
auth       required     pam_userdb.so db=/etc/vsftpd-virtual-user
account    required     pam_userdb.so db=/etc/vsftpd-virtual-user
session    required     pam_loginuid.so
EOF
) > pam.d/vsftpd.virtual

# 获取当前的用户名，不能用whoami或$LOGNAME，否则得到的是root
owner=`whoami | awk '{print $1}'`

# 创建vsftpd的配置文件。转载请注明出处：http://blog.csdn.net/hursing
(sudo cat <<EOF
listen=YES
anonymous_enable=NO
local_enable=YES
virtual_use_local_privs=YES
write_enable=YES
local_umask=000
dirmessage_enable=YES
use_localtime=YES
xferlog_enable=YES
connect_from_port_20=YES
chroot_local_user=YES
hide_ids=YES
secure_chroot_dir=/var/run/vsftpd/empty
pam_service_name=vsftpd.virtual
guest_enable=YES
user_sub_token=$USER
rsa_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem
rsa_private_key_file=/etc/ssl/private/ssl-cert-snakeoil.key
EOF
) > vsftpd.conf
sudo echo "local_root=$ftp_dir" >> vsftpd.conf
# 虚拟用户需要映射为本地用户，设为自己，避免权限问题，但同时也令自己对ftp根目录不可写
sudo echo "guest_username=$owner" >> vsftpd.conf


# 设置了每个虚拟用户只可以浏览其根及子目录（否则可访问磁盘根目录），
# 这样会被要求根目录不可写，所以创建一个writable的子目录
mkdir "$ftp_dir"
mkdir "$ftp_dir/$writable"
sudo chmod a-w "$ftp_dir"
sudo chown -R $owner:$owner $ftp_dir

sudo /etc/init.d/vsftpd restart
