<?php $title_for_layout = "Classement" ?>

<h1>Classement</h1>

<?php

if (empty($players))
{
   echo "Aucun joueur enregistré pour l'instant. Revenez plus tard :)";
}
else
{
   $tableHeader = array(
      'Pseudo',
      'Parties jouées',
      'Score',
   );

   echo $this->Table->table('scoreboard', $tableHeader, $players, array('sorted' => array(1, 2)));   
}
?>
