<?php
/**
* Debug
*/
function debug($var)
{
   if(Configuration::isDebugMode())
   {
      $debug = debug_backtrace();

      echo '<p><a href=#>' . $debug[0]['file'] . ' </strong> l.' . $debug[0]['line'] . '</a></p>';

      echo '<ol>';
      foreach ($debug as $key=>$value)
      {
         if ($key > 0)
         {
            echo '<li><strong>' . $value['file'] . ' </strong> l.' . $value['line'] . '</li>';
         }
      }
      echo '</ol>';

      echo '<pre>';
      print_r($var);
      echo '</pre>';
   }
}
