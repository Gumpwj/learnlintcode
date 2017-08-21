#!/bin/bash

#清理环境
if [ "x$(id -u)" != x0 ]; then  
  echo " Error: please run this script with 'sudo'. "  
  exit 1
fi

sudo rm /home/jiawu/.ssh/known_hosts
sudo rm /root/.ssh/known_hosts

echo "请输入ip："
read ip
sudo scp /home/jiawu/test/rhvh.repo /home/jiawu/test/clear_disk.py $ip:/etc/yum.repos.d/


read -n1 -p "Do you want scp rpm package, continue [Y/N]?" answer
case $answer in
Y | y)
      echo
      echo "请输入rpm包的ID号： " 
      read ID
      sudo scp /home/jiawu/test/rpm/redhat-virtualization-host-image-update-$ID.noarch.rpm $ip:/etc/yum.repos.d/
;;      
N | n)
      echo "No need to scp '.rpm' package."
;;      
*)
      echo "error choice"
;;      
esac


#if [$char == y]; then
#  echo "请输入rpm包的ID号： " 
#  read ID
#  sudo scp /home/jiawu/test/rpm/redhat-virtualization-host-image-update-$ID.noarch.rpm
#else
#  echo "No need to scp '.rpm' package. "
#fi

echo "job is done! "

ssh -lroot $ip

exit 0