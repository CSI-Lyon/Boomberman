<?php
class Table
{
   private $controller;

   public function __construct($controller)
   {
      $this->controller = $controller;
   }

   /**
   * Génère un tableau
   * @param name Nom du tableau
   * @param tableHeader Entête du tableau
   *
   * @return html Code html du tableau crée
   */
   public function table($name, $tableHeader, $entries, $options = array())
   {
      $html = '<table id="scoreboard"> <tr>';

      foreach ($tableHeader as $key => $value)
      {
         $html .= '<th';
         if (isset($options['sorted']) and in_array($key, $options['sorted']))
            $html .= ' onclick="sortTable(\'' . $key . '\')" sorted sortedMethod="asc"';
         $html .= '>' . ((isset($options['headerVisibility']) and $options['headerVisibility'] == 'hidden') ? '' : $value) . '</th>';
      }

      $html .= '</tr>';

      foreach ($entries as $entry)
      {
         $html .= '<tr>';

         foreach ($entry as $field)
         {
            if (isset($options['hideField']) and strpos($field, $options['hideField']) === 0) break;

            $html .= '<td';
            if (isset($options['linked']))
            {
               $html .= ' onclick=';
               $link = Router::url($options['linked'] . $entry->id);
               $html .= 'redirect("' . $link . '")';
               $html .= '>' . $field;
            }
            else
            {
               $html .= '>' . $field;
            }
            $html .= '</td>';
         }
         $html .= '</tr>';
      }

      $html .= '</table>'>

      $html .= '<link href="webroot/css/table.css" rel="stylesheet">';

      $content = file_get_contents(WEBROOT . DS . 'js' . DS . 'table.js');

      $html .= '<script>' . $content . '</script>';

      //$html .= '<script src="webroot/js/table.js"></script>';

      //debug(htmlspecialchars($html)); die();
      return $html;
   }
}
