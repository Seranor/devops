# devops
迁移仓库，原仓库 https://github.com/klcc-c

## 后端运行

```
git clone https://github.com/Seranor/minio-upfile.git
# python3.6
cd devops_api/
pip install -r requirements.txt

pip install uwsgi

# 该项目存放在 /web 目录下使用该配置文件
cat > /web/devops_api/devops_api/devopsapi.xml <<EOF
<uwsgi>    
   <socket>127.0.0.1:8888</socket>
   <chdir>/web/devops_api/devops_api/</chdir>    
   <module>devops_api.wsgi</module>
   <processes>4</processes>
   <daemonize>uwsgi.log</daemonize>
</uwsgi>
EOF

# nginx配置文件
cat > /usr/local/nginx/conf/vhost/devopsapi.conf<< EOF
server {
    listen 8080;
    server_name  127.0.0.1;
    charset utf-8;
    location / {
       include uwsgi_params;
       uwsgi_pass 127.0.0.1:8888;
       uwsgi_param UWSGI_SCRIPT devops_api.wsgi;
       uwsgi_param UWSGI_CHDIR /web/devops_api/devops_api/;
    }
}
EOF

# mysql 具体的密码视情况而定
create database devops default charset=utf8mb4;
grant all privileges on devops.* to 'devops'@'%' identified by 'asd123...';
grant all privileges on devops.* to 'devops'@'localhost' identified by 'asd123...';
flush privileges;

# Redis 准备好即可，如果设置了密码在settings/dev.py/prod.py 中添加密码即可，
# 以及在celery_tasks/config.py 中把密码填写上

# python 初始化数据库命令
python manage.py makemigrations
python manage.py migrate

# 主要配置文件
settings/dev.py/prod.py  # 注意配置数据库相关，Gitlab，Jenkins，Redis，MySQL的信息等

# manage.py 中选择dev或者prod的配置文件
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devops_api.settings.dev')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devops_api.settings.prod')


# 启动celery  命令必须在manage.py的父目录下执行
  # 启动定时任务首先需要有一个work执行异步任务，然后再启动一个定时器触发任务。
  celery -A celery_tasks.main worker -l info

  # 启动定时器触发 beat  (注意：下面是一条完整指令)
  celery -A celery_tasks.main beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

## 前端运行

```
# node v18.2.0
# npm 8.9.0

# 下载依赖
cd devops_web/
npm install  


# 修改相关地址的文件
vue.config.js
settings.js

# 打包得到dist的静态文件 放到nginx服务器上即可
npm run build 

# nginx配置文件
server {
    listen 80;
    server_name  localhost;
    charset utf-8;
    location / {
        root /web/devops_web/dist;
        index index.html;
        try_files $uri $uri/ /index.html; # 解决单页面应用刷新404问题
    }
}
```

## 展示

![hNbS3a](https://klcc-img-1251900471.cos.ap-chengdu.myqcloud.com/img/hNbS3a.png)
![WwxDBm](https://klcc-img-1251900471.cos.ap-chengdu.myqcloud.com/img/WwxDBm.png)
![BTtHeo](https://klcc-img-1251900471.cos.ap-chengdu.myqcloud.com/img/BTtHeo.png)
![nQuPpD](https://klcc-img-1251900471.cos.ap-chengdu.myqcloud.com/img/nQuPpD.png)
![cpYNMA](https://klcc-img-1251900471.cos.ap-chengdu.myqcloud.com/img/cpYNMA.png)
![jAXElP](https://klcc-img-1251900471.cos.ap-chengdu.myqcloud.com/img/jAXElP.png)
![0jx29C](https://klcc-img-1251900471.cos.ap-chengdu.myqcloud.com/img/0jx29C.png)
![f2iOMx](https://klcc-img-1251900471.cos.ap-chengdu.myqcloud.com/img/f2iOMx.png)
![RW7MrX](https://klcc-img-1251900471.cos.ap-chengdu.myqcloud.com/img/RW7MrX.png)
![1g5Y78](https://klcc-img-1251900471.cos.ap-chengdu.myqcloud.com/img/1g5Y78.png)
