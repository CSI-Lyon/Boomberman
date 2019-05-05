<?php
class Session
{
   public function __construct()
   {
      if (!isset($_SESSION))
      {
         session_start();
      }
   }

   /**
   * Ajoute un message à la session
   * @param message Message
   * @param type Type du message
   */
   public function setFlash($message, $type = null)
   {
      $_SESSION['flash'] = array(
         'message' => $message,
         'type' => $type
      );
   }

   /**
   * Affiche les messages stockés en session
   */
   public function flash()
   {
      if (isset($_SESSION['flash']['message']))
      {
         $html = $_SESSION['flash']['message'];
         $_SESSION['flash'] = array(); // On vide la liste de messages flash

         return $html;
      }
   }

   /**
   * Ajoute ou MAJ une variable session
   * @param key Variable
   * @param value Valeur de la variable
   */
   public function write($key, $value)
   {
      $_SESSION[$key] = $value;
   }

   /**
   * Lit une variable session ou $_SESSION
   * @param key Variable
   *
   * @return value Valeur de la variable
   */
   public function read($key = null)
   {
      if ($key)
      {
         if (isset($_SESSION[$key]))
         {
            $value = $_SESSION[$key];
         }
         else
         {
            // La variable n'existe pas
            $value = false;
         }
      }
      else
      {
         $value = $_SESSION;
      }

      return $value;
   }

   /**
   * Test si un utilisateur est connecté
   * @return connected True si l'utilisateur est connecté / False sinon
   */
   public function isLogged()
   {
      $connected = isset($_SESSION['user']);

      return $connected;
   }

   /**
   * Déconnecte la session
   */
   public function disconnect()
   {
      unset($_SESSION['user']); // Supression de la variable $_SESSION['user']
   }
}
