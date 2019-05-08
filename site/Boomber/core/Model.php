<?php
class Model
{
   public static $connections = array();

   private $config = 'default'; // ID de la base
   private $table = false; // Table

   private $db; // Base de données

   public function __construct()
   {
      if ($this->table == false)
         $this->table = strtolower(get_class($this)) . 's'; // Initialisation de la table à utiliser

      // Connexion à la base de données
      $config = Configuration::getAttribute('sql')[$this->config];

      if (isset(Model::$connnections[$this->config]))
      {
         $this->db = $connections[$this->config]; // Si la connexion est déjà établie, on la prend et on sort du constructeur
         return true;
      }

      try
      {
         $pdo = new PDO(
            'mysql:host=' . $config['host'] . ';dbname=' . $config['dbname'],
            $config['username'],
            $config['password'],
            array(PDO::MYSQL_ATTR_INIT_COMMAND => 'SET NAMES utf8') // Définition de l'encodage
         );

         if (Configuration::isDebugMode()) $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_WARNING); // Debug

         self::$connections[$this->config] = $pdo;
         $this->db = $pdo;
      }
      catch (\PDOException $e)
      {
         if (Configuration::isDebugMode())
         {
            die($e->getMessage());
         }
         else
         {
            die('Impossible de se connecter à la base de données. Contactez le développeur de ce site si le problème persisite.');
         }
      }
   }

   /**
   * Exécute une requête personnalisée
   * @param req Requête à exécuter
   * @return result Résultat de la requête
   */
   public function find($req)
   {
      $sql = 'SELECT ';

      /*
      Construction de la clause COUNT
      */
      if (isset($req['fields']))
      {
         if (is_array($req['fields']))
            $sql .= implode(', ', $req['fields']); // Séparation des champs par ','
         else
            $sql .= $req['fields'];
      }
      else
         $sql .= '*';

      $sql .= ' FROM ' . $this->table . ' AS ' . get_class($this) . ' ';

      /*
      Construction de la clause WHERE
      */
      if (isset($req['conditions']))
      {
         $sql .= 'WHERE ';
         if (!is_array($req['conditions']))
            $sql .= $req['conditions'] . ' ';
         else
         {
         $conditions = array();
         foreach ($req['conditions'] as $key => $value)
         {
            if (!is_numeric($value))
            {
               $value = '"' . htmlentities($value, ENT_QUOTES) . '"'; // Supression des guillemets
            }

            $conditions[] = "$key = $value";
         }

         $sql .= implode(' AND ', $conditions); // Séparation des conditions par AND
         }
      }

      if (isset($req['orderBy']))
         $sql .= 'ORDER BY ' . $req['orderBy'];

      /*
      Construction de la clause LIMIT
      */
      if (isset($req['limit']))
         $sql .= 'LIMIT ' . $req['limit'];

      $pre = $this->db->prepare($sql);
      $pre->execute();

      $result = $pre->fetchAll(PDO::FETCH_OBJ);

      return $result;
   }

   /**
   * Exécute une requête personnalisée mais ne retourne qu'un seul élément
   * @param req Rquête à exécuter
   *
   * @return result Résultat de la requête
   */
   public function findFirst($req)
   {
      $result = current($this->find($req));

      return $result;
   }

   /**
   * Exécute une requête personnalisée en comptant le nombre d'entrées
   * @param conditions Conditions de la requête (facultatif)
   *
   * @return count Nombre d'entrées
   */
   public function findCount($conditions = null)
   {
      if (isset($conditions))
      {
         $result = $this->findFirst(array(
            'fields' => 'COUNT(*) AS count',
            'conditions' => $conditions
         ));
      }
      else
      {
         $result = $this->findFirst(array(
            'fields' => 'COUNT(*) AS count'
         ));
      }

      $count = $result->count;

      return $count;
   }

   /**
   * Suprime une entrée dans la base de données
   * @param id Id de l'entrée à supprimer
   */
   public function delete($id)
   {
      $sql = "DELETE FROM $this->table WHERE id = $id";

      $this->db->query($sql);
   }

   /**
   * Insère ou met à jour une entrée dans la base de données
   * @param data Données à mettre à jour
   *
   * @return id Id de l'entrée insérée
   */
   public function save($data)
   {
      $fields = array();
      $values = array();

      foreach ($data as $key => $value)
      {
         if ($key != 'id')
         {
            $fields[] = "$key=:$key";
            $values[":$key"] = $value;
         }
      }

      if (isset($data->id) && !empty($data->id))
      {
         // Mise à jour
         $sql = 'UPDATE ' . $this->table . ' SET ' . implode($fields, ', ') . ' WHERE id=' . $data->id . '';
      }
      else
      {
         // Insertion
         $sql = 'INSERT INTO ' . $this->table . ' SET ' . implode($fields, ', ');
      }

      $pre = $this->db->prepare($sql);

      $pre->execute($values);

      return $this->db->lastInsertId();
   }
}
