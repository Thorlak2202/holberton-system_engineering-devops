#script to fix typo in configuration settings of wordpress

exec { 'typo correct':
  command => "sed -i 's/.phpp/.php' /var/www/html/wp-settings.php",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
