<?php
class Dispatcher
{
   private $request;

   public function __construct()
   {
      $this->request = new Request();

      Router::connect();
      $this->request = Router::parse($this->request->url, $this->request);

      if (!$this->request) return;

      $controller = $this->loadController();

      $action = $this->request->action;

      if (!in_array($action, array_diff(get_class_methods($controller), get_class_methods('Controller'))))
         $controller->e404('Le controller ' . $this->request->controller . ' n\'a pas de méthode ' . $action);

      call_user_func_array(array($controller, $action), $this->request->args); // Appel de la méthode de l'action du controller

      $controller->render($action); // Appel de la vue associée à l'action du controller
   }

   //localhost:8888/Boomber/profil/mailbox/view/3

   /**
   * Charge le controller associé à l'URL
   * @return controller Controller associé à l'URL
   */
   private function loadController()
   {
      $name = ucfirst($this->request->controller) . 'Controller'; // Nom du controller à appeler
      $file = ROOT . DS . 'controller' . DS . $name . '.php'; // Fichier controller
      require $file;

      $controller = new $name($this->request);

      return $controller;
   }
}
