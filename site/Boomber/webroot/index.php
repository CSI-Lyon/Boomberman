<?php
$start = microtime(true);

define('WEBROOT', dirname(__FILE__)); // /Applications/MAMP/htdocs/Boomber/webroot
define('ROOT', dirname(WEBROOT)); // /Applications/MAMP/htdocs/Boomber

define('DS', DIRECTORY_SEPARATOR);

define('CORE', ROOT . DS . 'core'); // /Applications/MAMP/htdocs/Boomber/core
define('BASE_URL', dirname(dirname($_SERVER['SCRIPT_NAME']))); // /Boomber

require CORE . DS . 'loader.php';

new Dispatcher();

/*
<!-- DEBUG -->
<div style="position:fixed; background-color: red; color: white;">
   <?php echo 'Page générée en ' . round(microtime(true) - $start, 5) . ' secondes'; ?>
</div>
*/
