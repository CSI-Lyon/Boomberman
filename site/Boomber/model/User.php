<?php
class User extends Model
{
   /**
   * Test si un nom d'utilisateur est enregistré dans la bdd
   * @param username Nom de l'utilisateur
   *
   * @return result True : Le pseudo existe / False : Le pseudo n'existe pas
   */
   public function usernameExists($username)
   {
      $user = $this->findFirst(array(
         'conditions' => 'username = "' . $username . '"'
      ));

      $result = empty($user) ? false : true;

      return $result;
   }
}
