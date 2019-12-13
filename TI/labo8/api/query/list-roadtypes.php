<?php

require_once('../model/accidents.php');

echo json_encode(Accidents::the()->roadtype);
