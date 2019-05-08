<?php
class Router
{
   private static $routes = array();

   public static function parse($url, $request)
   {
      $url = trim($url, '/');
      foreach (self::$routes as $route)
      {
         if (preg_match($route['match'], $url))
         {
            $args = [];
            for ($i = 1; $i <= sizeof($route['args']); $i++)
            {
               $args[] = trim(preg_replace($route['match'], '$' . $i, $url), '/');
            }

            $request->controller = $route['controller'];
            $request->action = $route['action'];
            $request->args = $args;

            return $request;
         }
      }

      echo 'Erreur : cette page n\'existe pas !';
      return false;
   }

   public static function connect()
   {
      if (empty(self::$routes))
      {
         foreach (Configuration::getRoutes() as $confRoute)
         {
            $path = $confRoute['path'] . ' ';
            $params = explode('{', $path);

            $route['path'] =  $params[0];

            $controller = explode(':', $confRoute['controller']);

            $route['controller'] = $controller[0];
            $route['action'] = $controller[1];

            $route['args'] = array();
            foreach ($params as $key => $param)
            {
               if ($key == 0) continue;

               $arg = explode(':', $param);

               $route['args'][] = $arg[0];

               $arg[1] = str_replace('}', '', $arg[1]);

               $params[$key] = $arg[1];
            }

            $path = implode('', $params);
            $path = str_replace('/', '\/', $path);
            $path = str_replace(' ', '', $path);

            $route['match'] = '#^' . $path . '$#';

            self::$routes[] = $route;
         }
      }
   }

   public static function url($url)
   {
      return BASE_URL . '/' . $url;
   }
}
