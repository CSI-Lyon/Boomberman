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

      $conditions = array('online' => 1, 'type' => 'post');

      $posting['posts'] = $this->Post->find(array(
         'conditions' => $conditions,
         'limit' => (($this->request->page - 1) * $perPage) . ',' . $perPage
      ));
      $posting['nbPosts'] = $this->Post->findCount($conditions);
      $posting['nbPages'] = ceil($posting['nbPosts'] / $perPage);

      $this->setAll($posting);
   }

   /**
   * Visualisation d'un post
   * @param id Id du post à afficher
   * @param slug Slug du post à afficher
   */
   function view($id, $slug)
   {
      $this->loadModel('Post');

      $post = $this->Post->findFirst(array(
         'fields'     => 'id, slug, content, name',
         'conditions' => array('id' => $id, 'online' => 1, 'type' => 'post')
      ));

      if (empty($post))
      {
         $this->e404('Cette page n\'existe pas');
      }

      if ($slug != $post->slug)
      {
         // Le slug a été modifié dans la base de données, on demande à Google d'effectuer une redirection permanente
         $this->redirect("posts/view/id:$id/slug:$post->slug", 301);
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

      $conditions = array('type' => 'post');

      $posting['posts'] = $this->Post->find(array(
         'fields' => 'id, name, online',
         'conditions' => $conditions,
         'limit' => (($this->request->page - 1) * $perPage) . ',' . $perPage
      ));
      $posting['nbPosts'] = $this->Post->findCount($conditions);
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

      $this->redirect('admin/posts/index');
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
         Gestion du formulaire
         */
         if ($this->Post->validates($this->request->data))
         {
            // Le formulaire est bon
            $this->request->data->type = 'post'; // Ajout du type
            $this->request->data->created = date('Y-m-d h:i:s'); // Ajout de la date

            $this->Post->save($this->request->data); // Sauvegarde des données
            $this->Session->setFlash('Le contenu a bien été modifié');
            $id = $this->request->data->id;

            $this->redirect('admin/posts/index'); // Redirection vers l'accueil
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
