<?php
class Router
{
   public static $routes = array();
   public static $prefixes = array();

   public static function prefix($url, $prefix)
   {
      self::$prefixes[$url] = $prefix;
   }

   /**
   * Parse une url
   * @param URL URL à parser
   * @param request Requête
   *
   * @return true
   **/
   public static function parse($url, $request)
   {
      $url = trim($url, '/'); // Découpage de l'URL en parties délimitées par '/'

      if(empty($url))
      {
         $url = Router::$routes[0]['url'];
      }
      else
      {
         foreach (self::$routes as $route)
         {
            if (preg_match($route['catcher'], $url, $match))
            {
               $request->controller = $route['controller'];
               $request->action = isset($match['action']) ? $match['action'] : $route['action'];
               $request->params = array();

               foreach ($route['params'] as $key => $value)
               {
                  $request->params[$key] = $match[$key];
               }

               if(!empty($match['args']))
               {
                  $request->params += explode('/', trim($match['args'], '/'));
               }

               return true;
            }
         }
      }

      $params = explode('/', $url); // Découpage de l'url en parties délimitées par '/'

      if (in_array($params[0], array_keys(self::$prefixes)))
      {
         $request->prefix = self::$prefixes[$params[0]];
         array_shift($params); // Décalage du tableau
      }

      $request->controller = $params[0];
      $request->action = isset($params[1]) ? $params[1] : 'index';
      $request->params = array_slice($params, 2);

      return true;
   }

   public static function connect($redirection, $url)
   {
      $route = array();
      $route['params'] = array();
      $route['url'] = $url;
      $route['redirection'] = $redirection;

      /*
      Modification de la règle pour la rendre conforme
      */
      $route['origin'] = str_replace(':action', '(?P<action>([a-z0-9]+))', $url);
      $route['origin'] = preg_replace('#([a-z0-9]+):([^\/]+)#', '${1}:(?P<${1}>${2})', $route['origin']);
      $route['origin'] = '#^' . str_replace('/', '\/', $route['origin']) . '(?P<args>\/?.*)$#';

      $params = explode('/', $url);
      foreach ($params as $key => $value)
      {
         if (strpos($value, ':'))
         {
            $p = explode(':', $value);
            $route['params'][$p[0]] = $p[1];
         }
         else
         {
            if ($key == 0)
            {
               $route['controller'] = $value;
            }
            elseif ($key == 1)
            {
               $route['action'] = $value;
            }
         }
      }

      $route['catcher'] = $redirection;
      $route['catcher'] = str_replace(':action', '(?P<action>([a-z0-9]+))', $route['catcher']);
      foreach ($route['params'] as $key => $value)
      {
         $route['catcher'] = str_replace(":$key", "(?P<$key>$value)", $route['catcher']);
      }
      $route['catcher'] = '#^' . str_replace('/', '\/', $route['catcher']) . '(?P<args>\/?.*)$#';

      self::$routes[] = $route;
   }

   public static function url($url)
   {
      foreach (self::$routes as $route)
      {
         if (preg_match($route['origin'], $url, $match)) // Si l'url vérifie la règle
         {
            foreach ($match as $key => $value)
            {
               if (!is_numeric($key))
               {
                  $route['redirection'] = str_replace(":$key", $value, $route['redirection']);
               }
            }
            return BASE_URL . str_replace('//', '/', '/' . $route['redirection']) . $match['args'];
         }
      }

      foreach (self::$prefixes as $prefix => $layout) {
         if (strpos($url, $layout) === 0)
         {
            if ($prefix == 'admin' and $this->Session->isLogged())
            {
               $url = str_replace($layout, $prefix, $url);   
            }
         }
      }
      return BASE_URL . '/' . $url;
   }
}
