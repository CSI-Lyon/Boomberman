<?php
class PagesController extends Controller
{
   /**
   * Affichage d'une page
   */
   function view($id)
   {
      $this->loadModel('Post');
      $page = $this->Post->findFirst(array(
         'conditions' => array('id' => $id, 'online' => 1, 'type' => 'page')
      ));

      if(empty($page))
      {
         $this->e404('Cette page n\'existe pas');
      }

      $this->set('page', $page);
   }

   /**
   * Récupère les pages du menu
   * @return pages Pages du menu
   */
   public function getMenu()
   {
      $this->loadModel('Post');
      $pages = $this->Post->find(array(
         'conditions' => array('online' => 1, 'type' => 'page')
      ));

      return $pages;
   }
}
