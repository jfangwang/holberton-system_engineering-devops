# Create a file holberton

file_line { 'Turn off passwd auth':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    match  => 'PasswordAuthentication'
    line   => 'PasswordAuthentication no'
    replace=> true,
file_line { 'Declare identity file':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/holberton'
