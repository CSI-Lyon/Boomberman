<?php $title_for_layout = $post->name; ?>

<a href="<?php echo Router::url('blog') ?>"><< Retour</a>

<h1><?php echo $post->name ?></h1>

<?php echo $post->content ?>
