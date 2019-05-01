<!DOCTYPE html>
<html lang="en" dir="ltr">
   <head>
      <meta charset="utf-8">
      <title>Bomberman - <?php echo isset($title_for_layout) ? $title_for_layout : '' ?></title>
   </head>
   <body>

      <header>
         <nav>
            <h3>Bomberman</h3>
            <ul>
               <?php $pagesMenu = $this->request('Pages', 'getMenu') ?>
               <?php foreach ($pagesMenu as $page): ?>
                  <li><a href=<?php echo BASE_URL . '/pages/view/' . $page->id ?>><?php echo $page->name ?></a></li>
               <?php endforeach; ?>

               <li><a href="<?php echo Router::url('posts/index') ?>">Actualités</a></li>
               <li><?php echo ($this->Session->isLogged() ? '<a href="' . BASE_URL . '/users/logout' . '">Se déconnecter</a>' : '<a href="' . BASE_URL . '/users/login' . '">Se connecter</a>')?></li>
            </ul>
         </nav>
      </header>

      <div class="container">
         <?php echo $this->Session->flash() ?> <!-- Messages flash -->
         <?php echo $content_for_layout ?>
      </div>
   </body>
</html>
