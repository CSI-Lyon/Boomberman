<?php
class Form
{
   public $controller;
   public $errors;

   public function __construct($controller)
   {
      $this->controller = $controller;
   }

   /**
   * Génère un champ d'entrée
   * @param name Nom de l'entrée
   * @param label Label de l'entrée
   * @param options Options de l'entrée
   *
   * @return html Code html de l'entrée crée
   */
   public function input($name, $label, $options = array())
   {
      $error = false;
      $classError = '';
      if (isset($this->errors[$name]))
      {
         $error = $this->errors[$name];
         $classError = $error;
      }

      $value = isset($this->controller->request->data->$name) ? $this->controller->request->data->$name : '';

      if ($label == 'hidden')
      {
         return '<input type="hidden" name="' . $name . '" value="' . $value . '">';
      }

      $html = '<label for="input' . $name .'">' . $label .'</label>';

      $attributes = ''; // Attributs sumplémentaires
      foreach ($options as $k => $v)
      {
         if ($k != 'type')
         {
            $attributes .= ' ' . $k . '="' . $v . '"';
         }
      }

      /*
      Prise en charge du type
      */
      if (!isset($options['type']))
      {
         $html .= '<input type="text" id="input' . $name .'" name="' . $name .'" value="' . $value . '"' . $attributes . '>';
      }
      else
      {
         switch ($options['type'])
         {
            case 'textarea':
               $html .= '<textarea id="input' . $name .'" name="' . $name . '"' . $attributes . '>' . $value . '</textarea>';
               break;

            case 'checkbox':
               $html .= '<input type="hidden" name="' . $name . '" value="0"><input type="checkbox" name="' . $name . '" value="1" ' . (empty($value) ? '' : 'checked') . '>';
               break;

            case 'hidden':
               break;

            case 'password':
               $html .= '<input type="password" id="input' . $name .'" name="' . $name .'" value="' . $value . '"' . $attributes . '>';
         }
      }

      if ($error)
      {
         $html .= '<span>' . $error . '</span>';
      }

      return $html;
   }
}
