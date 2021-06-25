# Mispelled the extension...should be php instead of phpp
exec { 'fix extension':
	command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
	provider => shell,
}
