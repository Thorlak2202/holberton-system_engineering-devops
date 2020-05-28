#fixes stack so that we get to 0 requests failed.

exec { 'limit-augment':
  provider => shell,
  command  => "sed -i 's/15/4096/g' /etc/default/nginx"
}
