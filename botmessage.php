<?php
$token = "1415543455:AAG2i-xttKYeZI1w2rWof3JeGgDIOv_mn3s";

$data = [
    'text' => 'your message here',
    'chat_id' => '1190088274'
];

file_get_contents("https://api.telegram.org/bot$token/sendMessage?" . http_build_query($data) );

?>