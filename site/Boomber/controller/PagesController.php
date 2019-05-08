<?php
class PagesController extends Controller
{
   function index()
   {

   }

   function scoreboard()
   {
      $this->loadModel('User');
      $this->loadModel('Player');

      $players = $this->Player->find(array(
         'fields' => 'id, games_played, score',
         'orderBy' => 'score'
      ));

      foreach ($players as $player)
      {
         $player->id = $this->User->findFirst(array(
            'fields' => 'username',
            'conditions' => array('id' => $player->id)
         ))->username;
      }

      $this->set('players', $players);
   }
}
