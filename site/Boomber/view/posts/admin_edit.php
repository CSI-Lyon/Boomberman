<h1>Éditer un article</h1>

<form action="<?php isset($id) ? Router::url('admin/blog/edit/' . $id) : Router::url('admin/blog/create')?>" method="post">
   <?php echo $this->Form->input('name', 'Nom : ') ?>
   <br>

   <?php echo $this->Form->input('slug', 'Url :') ?>

   <!-- Champ caché -->
   <?php echo $this->Form->input('id', 'hidden') ?>
   <br>

   <?php echo $this->Form->input('content', '', array(
      'type' => 'textarea',
      'rows' => 20,
      'cols' => 70
   )) ?>
   <br>

   <?php echo $this->Form->input('online', 'En ligne', array(
      'type' => 'checkbox'
   )) ?>
   <br>

   <input type="submit" value="Envoyer">
</form>
