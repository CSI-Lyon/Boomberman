<?php
class Controller
{
   public $request;

   private $vars = array(); // Variables accessibles par la vue

   public $layout = 'default';
   private $rendered = false;

   function __construct($request = null)
   {
      if ($request)
      {
         $this->request = $request;
         if(!empty($request->prefix)) $this->layout = Configuration::getAttribute('hook')[$this->request->prefix];
      }
   }

   /**
   * Importe une vue
   * @param view Vue à importer
   */
   public function render($view)
   {
      if ($this->rendered) return false; // Si la vue a déjà était render, on quitte la méthode

      extract($this->vars); // Import des variables de vars

      if (strpos($view, '/') === 0)
      {
         $view = ROOT . DS . 'view' . $view . '.php';
      }
      else
      {
         $view = ROOT . DS . 'view' . DS . $this->request->controller . DS . $view . '.php';
      }

      /*
      * Récupération du contenu au lieu de l'afficher
      */
      ob_start();
      require $view;
      $content_for_layout = ob_get_clean();

      require ROOT . DS . 'view' . DS . 'layout' . DS . $this->layout . '.php';

      $this->rendered = true;
   }

   /**
   * Charge un modèle
   * @param model Modèle à charger
   */
   public function loadModel($model)
   {
      if (!isset($this->$model))
      {
         $file = ROOT . DS . 'model' . DS . $model . '.php';
         require_once $file;

         $this->$model = new $model();

         if (isset($this->Form))
         {
            $this->$model->Form = $this->Form;
         }
      }
   }

   /**
   * Ajoute ou modifie une variable
   * @param key Nom de la variable
   * @param value Valeur de la variable
   */
   public function set($key, $value)
   {
      $this->vars[$key] = $value;
   }

   /**
   * Ajoute ou modifie des variables
   * @param vars Tableau des variables à ajouter/modifier
   */
   public function setAll($vars)
   {
      $this->vars = $vars;
   }

   /**
   * Déclenche une erreur 404 (page inexistante)
   * @param message Message à afficher
   */
   public function e404($message)
   {
      header("HTTP/1.0 404 Not Found");

      $this->set('message', $message);
      $this->render('/errors/404');

      die();
   }

   /**
   * Appel un controleur depuis une vue
   * @param controller Nom du controleur à appeler
   * @param action Nom de l'action à appeler
   *
   * @return result Résultat de l'action appelée
   */
   public function request($controller, $action)
   {
      $controller .= 'Controller';
      require_once ROOT . DS . 'controller' . DS . $controller . '.php';

      $c = new $controller();

      $result = $c->$action(); // Appel de l'action

      return $result;
   }

   public function redirect($url, $code = null)
   {
      if ($code == 301)
      {
         header('HTTP/1.1 301 Moved Permanently');
      }

      header('Location: ' . Router::url($url));
   }
}
?>
