<?php
class MessagesController extends Controller
{
   function index()
   {
      if ($this->Session->isLogged())
      {
         $perPage = 10; // Nombre de messages par page

         $this->loadModel('Message');
         $this->loadModel('User');

         $array['messages'] = $this->Message->find(array(
            'fields' => 'id, sender_id, subject, created',
            'conditions' => array('receiver_id' => $this->Session->read('user')->id),
            'limit'      => (($this->request->page - 1) * $perPage) . ',' . $perPage,
         ));

         /*
         Remplacement de l'ID par un nom
         */
         foreach ($array['messages'] as $message)
         {
            $message->sender_id = $this->User->findFirst(array(
               'fields'     => 'username',
               'conditions' => array('id' => $message->sender_id)
            ))->username;
         }

         $array['nbMessages'] = $this->Message->findCount();

         $array['nbPages'] = ceil($array['nbMessages'] / $perPage);

         $this->setAll($array);
      }
   }

   function view($id)
   {
      $this->set('id', $id);
   }

   function send()
   {

   }
}
