<?php
class Configuration
{
   private static $config = ROOT . DS . 'config' . DS . 'config.yml';

   private function __construct()
   {
   }

   /**
   * Retourne la valeur d'un attribut dans le fichier de config
   * @param name Nom de l'attribut
   *
   * @return value Valeur de l'attribut
   */
   public static function getAttribute($name)
   {
      $value = Spyc::YAMLLoad(self::$config)[$name];

      return $value;
   }

   /**
   * Retourne vrai si le mode debug est activé
   * @return isDebugMode Valeur du test
   */
   public static function isDebugMode()
   {
      $isDebugMode = self::getAttribute('debug_mode');

      return $isDebugMode;
   }
}
