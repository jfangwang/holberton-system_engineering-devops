# Fix request number 15 -> 4000. 4000 should be fine.
exec { 'fix request number':
    command  => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4000\"/g" /etc/default/nginx',
    provider => shell,
}

# Restart nginx
exec { 'Restart nginx':
    command  => 'sudo service nginx restart',
    provider => shell,
}
