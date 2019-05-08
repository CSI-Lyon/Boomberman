<!DOCTYPE html>
<html lang="en" dir="ltr">
   <head>
      <meta charset="utf-8">
      <title>Bomberman - <?php echo isset($title_for_layout) ? $title_for_layout : '' ?></title>
      <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.0/css/all.css" integrity="sha384-lZN37f5QGtY3VHgisS14W3ExzMWZxybE1SJSEsQp9S+oqd12jhcu+A56Ebc1zFSJ" crossorigin="anonymous">
   </head>
   <body>

      <header>
         <nav>
            <ul>
               <li><a href="<?php echo Router::url('') ?>" class="title">Boomberman</a><li>
               <li><a href="<?php echo Router::url('blog') ?>">Actualités</a></li>
               <li><a href="<?php echo Router::url('scoreboard') ?>">Classement</a></li>
               <li style="float: right">
                  <?php
                  if ($this->Session->isLogged())
                  {
                     $url = Router::url('profil/logout');
                     echo "<a href=$url>Se déconnecter</a>";
                  }
                  else
                  {
                     $url = Router::url('users/login');
                     echo "<a href=$url>Se connecter</a>";
                  }
                  ?>
               </li>
            </ul>
         </nav>
      </header>

      <div class="container">
         <?php echo $this->Session->flash() ?>
         <?php echo $content_for_layout ?>
      </div>
   </body>
</html>
