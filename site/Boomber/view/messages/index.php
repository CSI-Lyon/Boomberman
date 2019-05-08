<?php $title_for_layout = 'Boite mail' ?>

<h1>Boîte mail</h1>

<div class="pagination">
      <ul>
         <?php for ($i = 1; $i <= $nbPages; $i++): ?>
            <li><a href="?page=<?php echo $i ?>"><?php echo $i ?></a></li>
         <?php endfor; ?>
      </ul>
</div>

<?php
$tableHeader = array(
   'senderName',
   'subject',
   'created',
   'see'
);

echo $this->Table->table('mailbox', $tableHeader, $messages, array('headerVisibility' => 'hidden', 'hideField' => 'id', 'linked' => 'messages/view/'));
?>
