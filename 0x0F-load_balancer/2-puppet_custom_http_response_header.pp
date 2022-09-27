# automate the task of creating a custom HTTP header response

exec { 'command':
  command  => 'apt-get -y update;
  apt -y install nginx;
  sudo sed -i "s/server_name _;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  service nginx restart',
  provider => shell,
}

