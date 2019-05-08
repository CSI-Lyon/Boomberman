<?php
class Controller
{
   public $request;

   private $layout = 'default';
   private $vars = array(); // Variables accessibles par la vue
   private $rendered = false;

   function __construct($request = null)
   {
      $this->Session = new Session(); // Chargement de la session

      $this->Form = new Form($this); // Chargement du gestionnaire de formulaire
      $this->Table = new Table($this); // Chargement du gestionnaire de tableau

      if ($request)
      {
         $this->request = $request;


         if (strpos($request->url, '/profil') === 0 and !$this->Session->isLogged())
         {
            // Si l'utilisateur tente d'accéder au profil alors qu'il n'est pas connecté, on le redirige à l'accueil
            $this->redirect('');
         }
         else if (strpos($request->url, '/admin') === 0) {
            $this->layout = 'admin';

            if (strpos($this->request->url, '/admin') === 0)
            {
               if (!$this->Session->isLogged()) //and Configuration::getAttribute('perms')[$this->Session->read('user')])
               {
                  // L'utilisateur n'a pas la permission
                  $this->redirect(''); // Redirection à la racine
               }
            }
         }
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
      A AMELIORER
      */
      $file = WEBROOT . DS . 'css' . DS . 'boomber.css';
      $content = file_get_contents($file);

      echo '<style>' . $content . '</style>';

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
