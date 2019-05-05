<!DOCTYPE html>
<html lang="en" dir="ltr">
   <head>
      <meta charset="utf-8">
      <title>Bomberman - <?php echo isset($title_for_layout) ? $title_for_layout : 'Administration' ?></title>
   </head>
   <body>

      <header>
         <nav>
            <h3><a href="<?php echo Router::url('admin/posts/index') ?>">Administration</a></h3>
            <ul>
               <li><a href="<?php echo Router::url('admin/posts/index') ?>">Articles</a></li>
               <li><a href="<?php echo Router::url('admin/pages/index') ?>">Pages</a></li>
               <li><a href="<?php echo Router::url('/') ?>">Voir le site</a></li>
            </ul>
         </nav>
      </header>

      <div class="container">
         <?php echo $this->Session->flash() ?> <!-- Messages flash -->
         <?php echo $content_for_layout ?>
      </div>
   </body>
</html>
