<?php
class UsersController extends Controller
{
   /**
   * Connexion
   */
   function login()
   {
      if ($this->request->data)
      {
         $this->loadModel('User');

         $data = $this->request->data;

         $username = $data->username;
         $password = sha1($data->password); // Encodage du mot de passe

         $user = $this->User->findFirst(array(
            'conditions' => array('username' => $username, 'password' => $password)
         ));

         if (!empty($user))
         {
            /*
            Utilisateur trouvé
            */
            $this->request->data->password = ''; // Supression du mot de passe de la requête

            $this->Session->write('user', $user);
            $this->Session->setFlash("Content de vous revoir $user->username !");
         }
         else
         {
            /*
            Utilisateur non trouvé
            */
            $this->Session->setFlash('Pseudo ou mot de passe incorrect');
         }
      }

      if ($this->Session->isLogged())
      {
         /*
         Une session est ouverte
         */
         $this->redirect(''); // Redirection à la racine
      }
   }

   /**
   * Déconnexion
   */
   function logout()
   {
      $this->Session->disconnect();
      $this->Session->setFlash('Vous avez été déconnecté');

      $this->redirect(''); // Redirection à la racine
   }
}
