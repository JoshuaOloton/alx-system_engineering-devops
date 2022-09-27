# automate the task of creating a custom HTTP header response

exec { 'update system':
        command => '/usr/bin/apt-get update',
}

package { 'nginx':
    ensure => 'installed',
}

exec { 'allow HTTP':
  command => "ufw allow 'Nginx HTTP'",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

exec { 'chown www folder':
  command => 'chown -R "$USER:$USER" /var/www/html/',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

file { '/var/www/html/index.html':
  content => "Hello World!\n",
}

file {'nginix config file': 
  ensure  => file,
  path    => '/etc/nginx/sites-enabled/default',
  content => 
"server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;

        # Add index.php to the list if you are using PHP
        index index.html index.htm index.nginx-debian.html;

        server_name _;

        add_header X-Served-By $HOSTNAME;

        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files \$uri \$uri/ =404;
        }

        error_page 404 /error-page.html;
        location = /error-page.html {
                root /var/www/html;
                internal;
        }

        location /redirect_me {
            return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
}
",
}

exec { 'restart service':
  command => 'service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin',
}


