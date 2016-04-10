<?php
$old_path = getcwd();
chdir('/var/www/html');
$output = shell_exec('./run.sh');
chdir($old_path);
echo "<pre>$output</pre>";

?>
