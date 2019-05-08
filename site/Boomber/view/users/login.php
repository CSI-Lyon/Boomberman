<?php $title_for_layout = 'Connexion' ?>

<h1>Se connecter</h1>

<form action="<?php echo Router::url('users/login') ?>" method="post">
   <?php echo $this->Form->input('username', 'Identifiant') ?>
   <br>
   <?php echo $this->Form->input('password', 'Mot de passe', array('type' => 'password')) ?>
   <br>

   <input type="submit" value="Se connecter">
</form>

<p>
Pas encore inscrit ? <a href="<?php echo Router::url('users/register') ?>">Par ici</a> l'inscription !
</p>
