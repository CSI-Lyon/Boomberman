<!DOCTYPE html>
<html lang="en" dir="ltr">
   <head>
      <meta charset="utf-8">
      <title>Bomberman - <?php echo isset($title_for_layout) ? $title_for_layout : 'Administration' ?></title>
      <link rel="stylesheet" href="webroot/css/layout.css">
   </head>
   <body>

      <header>
         <nav>
            <h3><a href="<?php echo Router::url('admin/blog') ?>">Administration</a></h3>
            <ul>
               <li><a href="<?php echo Router::url('admin/blog') ?>">Articles</a></li>
               <li><a href="<?php echo Router::url('') ?>">Voir le site</a></li>
            </ul>
         </nav>
      </header>

      <div class="container">
         <?php echo $this->Session->flash() ?> <!-- Messages flash -->
         <?php echo $content_for_layout ?>
      </div>
   </body>
</html>
