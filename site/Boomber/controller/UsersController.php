<?php
class UsersController extends Controller
{
   /**
   * Inscription
   */
   function register()
   {
      if ($this->request->data)
      {
         $this->loadModel('User');

         $data = $this->request->data;

         /*
         Gestion du formulaire d'inscription
         */

         // Règles de validation
         $validation = array(
            'username' => array(
               'required' => true,
               'rule' => '([\w0-9]{4,})',
               'message' => "Le pseudo n'est pas valide (4 caractères alphanumériques au moins)"
            ),
            'password' => array(
               'required' => true,
               'rule' => '([\w0-9]{6,})',
               'message' => "Le mot de passe n'est pas valide (6 caractères alphanumériques au moins)"
            ),
            'recapPassword' => array(
               'required' => true,
               'equals' => 'password',
               'message' => "Ce champ n'est pas identique au mot de passe tapé"
            )
         );

         if ($this->Form->validates($validation))
         {
            /*
            Le formulaire est valide
            */
            if (!$this->User->usernameExists($data->username))
            {
               /*
               Le nom d'utilisateur n'existe pas
               */
               unset($data->recapPassword);
               $data->password = sha1($data->password);
               $user = $this->User->save($data); // Insertion du nouveau membre dans la bdd

               $this->loadModel('Player');
               $this->Player->save($user); // Insertion du nouveau joueur dans la bdd

               $this->Session->setFlash('Bienvenue parmis nous !');
               $this->Session->write('user', $user);

               $this->redirect(''); // Redirection à la racine
            }
            else
            {
               // Le nom d'utilisateur existe déjà
               $this->Session->setFlash('Erreur : Le pseudo existe déjà');
            }
         }
         else
         {
            $this->Session->setFlash('Merci de bien vouloir corriger vos informations');
         }
      }
   }

   /**
   * Connexion
   */
   function login()
   {
      if ($this->request->data)
      {
         $this->loadModel('User');

         $data = $this->request->data;

         // Règles de validation
         $validation = array(
            'username' => array(
               'required' => true,
            ),
            'password' => array(
               'required' => true
            )
         );

         if ($this->Form->validates($validation))
         {
            /*
            Le formulaire est valide
            */
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
               $this->Session->setFlash("Content de vous revoir $username !");
            }
            else
            {
               /*
               Utilisateur non trouvé
               */
               $this->Session->setFlash('Pseudo ou mot de passe incorrect');
            }
         }
      }

      if ($this->Session->isLogged())
      {
         /*
         Une session est ouverte
         */
         $this->redirect('admin/blog'); // Redirection à la racine
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
