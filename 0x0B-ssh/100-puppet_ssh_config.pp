# Create a file holberton

file { 'ssh_config'
    path              => '/etc/ssh/ssh_config',
    ensure            => 'present',
    match             => 'PasswordAuthentication',
    line              => 'PasswordAuthentication no',
    replace           => true,
    match_for_absence => false,
}

