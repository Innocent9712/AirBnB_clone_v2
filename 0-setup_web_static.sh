#!/usr/bin/env bash
<<<<<<< HEAD
# sets up the web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "This is a test" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start
=======
# Script setup ngnix web servers for the AirBnB web_static files
data=/data
web_static=$data/web_static
releases=$web_static/releases
shared=$web_static/shared
test=$releases/test
index=$test/index.html
test_symlink=$web_static/current
default_web=/etc/nginx/sites-available/default
config_text=\
"server {
	listen 80 default;
	listen [::]:80 default_server;

	root /var/www/html;

	index index.html index.htm index.nginx-debian.html;

	server_name _;

	error_page 404 /error.html;
	add_header X-Served-By $(hostname);

	location /hbnb_static {
		 alias $test_symlink;
	}
	location / {
		 try_files \$uri \$uri/ =404;
	}
}"

systemctl status nginx > /dev/null 2>&1
cmd_status=$?
if [[ $cmd_status -ne 0 ]]; then
    sudo apt-get update
    sudo apt-get install nginx -y
fi

if ! [ -d $test ]; then
    sudo mkdir -p $test
    sudo touch $index
    echo "Hello new nginx" | sudo tee $index > /dev/null
fi

if ! [ -d $shared ]; then
    sudo mkdir -p $shared
fi
sudo ln -sfn $test $test_symlink
sudo chown -R ubuntu:ubuntu $data
echo "$config_text" | sudo tee $default_web > /dev/null
sudo service nginx restart
>>>>>>> 3a8481dacf820165e6faab8d6a01b3ca689df150
