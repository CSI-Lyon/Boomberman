<?php
class Post extends Model
{
   // Règles de validation
   var $validation = array(
      'name' => array(
         'rule' => 'notEmpty',
         'message' => 'Vous devez préciser un tire'
      ),
      'slug' => array(
         'rule' => '([a-z0-9\-]+)',
         'message' => "L'url n'est pas valide"
      )
   );
}
