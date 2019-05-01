<h1><?php echo $nbPosts ?> articles(s) trouvé(s)</h1>

<table>
   <thead>
      <tr>
         <th>ID</th>
         <th>En ligne</th>
         <th>Titre</th>
         <th>Actions</th>
      </tr>
   </thead>

   <tbody>
      <?php foreach ($posts as $post): ?>
         <tr>
            <td><?php echo $post->id ?></td>
            <td><span><?php echo ($post->online ? 'Oui' : 'Non') ?></span></td>
            <td><?php echo $post->name ?></td>
            <td>
               <a href=<?php echo Router::url('admin/posts/edit/' . $post->id) ?>>Editer</a>
               <a href=<?php echo Router::url('admin/posts/delete/' . $post->id) ?> onclick="return confirm('Voulez vous vraiment supprimer ce contenu ?')">Supprimer</a>
            </td>
         </tr>
      <?php endforeach; ?>
   </tbody>
</table>

<a href="<?php echo Router::url('admin/posts/edit') ?>">Ajouter un article</a>
