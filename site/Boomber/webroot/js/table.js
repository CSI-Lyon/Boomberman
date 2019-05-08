function sortTable(field)
{
   var table = document.getElementById("scoreboard"); // Récupération du tableau

   var direction = "asc"; // Direction du tri

   var switchcount = 0;

   var rows = table.rows; // Lignes du tableau

   var switching = true;
   while (switching)
   {
      switching = false;

      for (i = 1; i < (rows.length - 1); i++)
      {
         row = rows[i].getElementsByTagName("TD")[field];
         nextRow = rows[i + 1].getElementsByTagName("TD")[field];

         var shouldSwitch = false;

         if (direction == "asc")
         {
            if (row.innerHTML > nextRow.innerHTML)
            {
               shouldSwitch = true; // Demande de switch
               break;
            }
         }
         else if (direction == "desc")
         {
            if (row.innerHTML < nextRow.innerHTML)
            {
               shouldSwitch = true; // Demande de switch
               break;
            }
         }
      }

      if (shouldSwitch)
      {
         rows[i].parentNode.insertBefore(rows[i + 1], rows[i]); // Switch
         switching = true;
         switchcount ++;
      }
      else
      {
         if (switchcount == 0 && direction == "asc")
         {
            // Si il n'y a pas encore eu de switch et que la direction est ascendante
            direction = "desc";
            switching = true;
         }
      }
   }
}

function redirect($path)
{
   window.location.href = $path;
}
