<?php
require ROOT . DS . 'libs' . DS . 'Spyc.php';
require 'functions.php';

function autoload($class)
{
   require $class . '.php';
}

spl_autoload_register('autoload');

Router::prefix('pastel', 'admin');

Router::connect('/', 'posts/index');
Router::connect('post/:slug-:id', 'posts/view/id:([0-9]+)/slug:([a-z0-9\-]+)'); //Définition des routes
Router::connect('blog/:action', 'posts/:action');
