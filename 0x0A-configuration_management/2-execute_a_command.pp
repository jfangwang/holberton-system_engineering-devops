# Kill a process willy

exec { 'pkill -f killmenow':
  path => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
