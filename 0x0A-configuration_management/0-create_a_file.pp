file { '/tmp/school':
    owner    => 'www-data',
    group    => 'www-data',
    mode     => '0744',
    contents => 'I love Puppet'
}