<?php $title_for_layout = 'Blog' ?>

<h1>Blog</h1>

<?php foreach ($posts as $post): ?>

   <h2><?php echo $post->name ?></h2>

   <?php echo $post->content ?>

   <p><a href=<?php echo Router::url("blog/view/$post->slug-$post->id") ?>>Lire la suite &rarr;</a></p>

<?php endforeach; ?>

<div class="pagination">
      <ul>
         <?php for ($i = 1; $i <= $nbPages; $i++): ?>
            <li><a href="?page=<?php echo $i ?>"><?php echo $i ?></a></li>
         <?php endfor; ?>
      </ul>
</div>
