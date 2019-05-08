<?php $title_for_layout = 'Inscription' ?>

<h1>S'inscrire</h1>

<form action="<?php echo Router::url('users/register') ?>" method="post">
   <?php echo $this->Form->input('username', 'Identifiant') ?>
   <br>
   <?php echo $this->Form->input('password', 'Mot de passe', array('type' => 'password')) ?>
   <br>
   <?php echo $this->Form->input('recapPassword', 'Confirmation du mot de passe', array('type' => 'password')) ?>
   <br>

   <input type="submit" value="S'inscrire">
</form>
