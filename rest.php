<?php

function makeRestCall($username, $password) {
    $url = "http://localh2-env.eba-rpvpzjqz.eu-central-1.elasticbeanstalk.com/plug/48551917CE6C";

    // ophalen en verwerken van de username en password
    $auth = base64_encode("$username:$password");
    $headers = array("Authorization: Basic $auth");

    try {
        // call maken
        $ch = curl_init($url);
        curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

        $response = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

        // als er een connectie is print de response uit anders error printen
        if ($httpCode == 200) {
            echo "REST call successful." . PHP_EOL;
            echo "Response:" . PHP_EOL;
            echo $response;
        } else {
            echo "Failed to make the REST call. Status Code: $httpCode" . PHP_EOL;
            echo "Response:" . PHP_EOL;
            echo $response;
        }

        curl_close($ch);

    } catch (Exception $e) {
        echo "An error occurred: " . $e->getMessage() . PHP_EOL;
    }
}

// username en password via input zoat niemand erbij kan
$username = readline("Enter username: ");
$password = readline("Enter password: ");

makeRestCall($username, $password);

?>
