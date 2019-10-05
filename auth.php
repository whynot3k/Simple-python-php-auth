<?php
    date_default_timezone_set('Europe/Paris');
    $currentDateTime = date('Y-m-d');
    $authkey = $_GET["AUTH"];
    $HWIDS = $_GET["HWID"];
    $salt = "discordtool";
    $authkey = array("user1", "user2");
    $userhwid = array("hwid1", "hwid2")
    $STRINGS = "$currentDateTime$authkey$currentDateTime$HWIDS$salt";
if (in_array($authkey, $authkey))
  {
      if (in_array($HWIDS, $userhwid))
      {
            echo md5($STRINGS);
      }
      else
      {
          echo "WRONG HWID";
      }
  }
else
  {
  echo "INVALID AUTH KEY";
  }
?>