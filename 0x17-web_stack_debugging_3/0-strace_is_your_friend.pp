#script to fix typo in configuration settings of wordpress

exec { 'typo correct':
  provider => shell,
  command  => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php"
}
