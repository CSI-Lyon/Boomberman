<?php
class PostsController extends Controller
{
   /**
   * Page principale du Blog
   */
   function index()
   {
      $perPage = 2; // Nombre de posts par page

      $this->loadModel('Post');

      $array['posts'] = $this->Post->find(array(
         'conditions' => 'online = 1',
         'limit' => (($this->request->page - 1) * $perPage) . ',' . $perPage
      ));

      $array['nbPosts'] = $this->Post->findCount('online = 1');
      $array['nbPages'] = ceil($array['nbPosts'] / $perPage);

      $this->setAll($array);
   }

   /**
   * Visualisation d'un post
   * @param id Id du post à afficher
   * @param slug Slug du post à afficher
   */
   function view($slug, $id)
   {
      $this->loadModel('Post');

      $post = $this->Post->findFirst(array(
         'fields'     => 'id, slug, content, name',
         'conditions' => array('id' => $id, 'online' => 1)
      ));

      if (empty($post))
      {
         $this->e404('Cette page n\'existe pas');
      }

      if ($slug != $post->slug)
      {
         // Le slug a été modifié dans la base de données, on demande à Google d'effectuer une redirection permanente
         $this->redirect("blog/view/$post->slug-$post->id", 301);
      }

      $this->set('post', $post);
   }

   /* ============
        ADMIN
   ============ */

   /**
   * Liste des posts indexés
   */
   function admin_index()
   {
      $perPage = 10; // Nombre de posts par page

      $this->loadModel('Post');

      $posting['posts'] = $this->Post->find(array(
         'fields' => 'id, name, online',
         'limit'  => (($this->request->page - 1) * $perPage) . ',' . $perPage
      ));

      $posting['nbPosts'] = $this->Post->findCount();
      $posting['nbPages'] = ceil($posting['nbPosts'] / $perPage);

      $this->setAll($posting);
   }

   /**
   * Supression d'un post
   * @param id Id du post à supprimer
   */
   function admin_delete($id)
   {
      $this->loadModel('Post');

      $this->Post->delete($id);
      $this->Session->setFlash('Le contenu a bien été supprimé');

      $this->redirect('admin/blog');
   }

   /**
   * Édition d'un post
   * @param id Id du post à éditer
   */
   function admin_edit($id = null)
   {
      $this->loadModel('Post');

      if ($this->request->data)
      {

         /*
         Gestion du formulaire d'édition
         */

         // Règles de validation
         $validation = array(
            'name' => array(
               'required' => true,
            ),
            'slug' => array(
               'required' => true,
               'rule' => '([a-z0-9\-]+)',
               'message' => "L'url n'est pas valide"
            )
         );

         if ($this->Form->validates($validation))
         {
            // Le formulaire est bon
            $this->request->data->created = date('Y-m-d h:i:s'); // Ajout de la date

            $id = $this->Post->save($this->request->data); // Sauvegarde des données
            $this->Session->setFlash('Le contenu a bien été sauvegardé');

            $this->redirect('admin/blog'); // Redirection vers l'accueil
         }
         else
         {
            // Erreur(s) dans le formulaire
            $this->Session->setFlash('Merci de corriger vos informations', 'error');
         }
      }
      else
      {
         if ($id)
         {
            $this->request->data = $this->Post->findFirst(array(
               'conditions' => array('id' => $id)
            ));
         }
      }

      $this->set('id', $id);
   }
}
