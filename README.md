# python_for_learn
A record for learning and teaching python.
Welcome to join and help us better.

## 连接数据库准备(python3)

### 服务器开启数据库应用对应端口

```
systemctl start firewalld 
firewall-cmd --zone=public --add-port=3306/tcp --permanent
firewall-cmd --reload(此步非必须)
```

```
命令含义：

--zone #作用域

--add-port=80/tcp #添加端口，格式为：端口/通讯协议

--permanent #永久生效，没有此参数重启后失效
```

### 安装python用于连接数据库的模块

```
git clone https://github.com/PyMySQL/PyMySQL
cd PyMySQL/
python3 setup.py install
cd ..
rm -rf PyMySQL/
```

### 修改mysql原始密码

```
mysql -u root

mysql> use mysql;

mysql> UPDATE user SET Password = PASSWORD('newpass') WHERE user = 'root';

mysql> FLUSH PRIVILEGES;
```
