# Kill a process willy

exec { 'pkill -f killmenow':
  path => '/bin'
}
