<?php
error_reporting(0);

/* Using REMOTE_ADDR wouldn't give the correct visitor IP address every time, due to which this function is built. */
function userIP(){
    if(!empty($_SERVER['HTTP_CLIENT_IP'])){
        $ip = $_SERVER['HTTP_CLIENT_IP'];
    }elseif(!empty($_SERVER['HTTP_X_FORWARDED_FOR'])){
        $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
    }else{
        $ip = $_SERVER['REMOTE_ADDR'];
    }
    return $ip;
}

$userData = json_decode(file_get_contents("http://www.geoplugin.net/json.gp?ip=".userIP()));
$userCountry = $userData->geoplugin_countryName;

/* Getting the COVID-19 Tracking Records from an API! */
$response = file_get_contents("https://api.covid19api.com/summary");
$response = json_decode($response);

/* Because sometimes the resource isn't loaded due to server issues. */
while (!is_object($response)){
	$response = file_get_contents("https://api.covid19api.com/summary");
	$response = json_decode($response);
}

/* Parsing the COVID-19 Tracking Records properly to display in the web application! */
$worldwideData = $response->Global;
$countryData = $response->Countries;
foreach ($countryData as $countryObject){
	if ($countryObject->Country == $userCountry){
		$nc = $countryObject->NewConfirmed;
		$nr = $countryObject->NewRecovered;
		$nd = $countryObject->NewDeaths;
		$tc = $countryObject->TotalConfirmed;
		$tr = $countryObject->TotalRecovered;
		$td = $countryObject->TotalDeaths;
		$ta = $tc - $tr - $td;
	}
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width,initial-scale=1.0">
	<title>COVID-19 Tracking Web Application for the Modern World</title>
	<link rel="icon" href="./assets/img/icon.ico" type="image/x-icon" />
	<link rel="stylesheet" type="text/css" href="./assets/css/style.css"> 
</head>
<body>

<h1>COVID-19 <span class="yellow">Tracking Web Application</span></h1>
<h2>This utility is brought to you by <strong>U-TEC 31337</strong>.</h2>

<table class="recordTable">
	<thead>
		<tr>
			<th><h1>Statistics</h1></th>
			<th><h1>Global</h1></th>
			<th><h1>Local</h1></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>New Confirmed</td>
			<td><?php echo $worldwideData->NewConfirmed;?></td>
			<td><?php echo $nc;?></td>
		</tr>
		<tr>
			<td>New Recovered</td>
			<td><?php echo $worldwideData->NewRecovered;?></td>
			<td><?php echo $nr;?></td>
		</tr>
		<tr>
			<td>New Deaths</td>
			<td><?php echo $worldwideData->NewDeaths;?></td>
			<td><?php echo $nd;?></td>
		</tr>
		<tr>
			<td>Total Active</td>
			<td><?php echo ($worldwideData->TotalConfirmed-$worldwideData->TotalRecovered-$worldwideData->TotalDeaths);?></td>
			<td><?php echo $ta;?></td>
		</tr>
		<tr>
			<td>Total Confirmed</td>
			<td><?php echo $worldwideData->TotalConfirmed;?></td>
			<td><?php echo $tc;?></td>
		</tr>
		<tr>
			<td>Total Recovered</td>
			<td><?php echo $worldwideData->TotalRecovered;?></td>
			<td><?php echo $tr;?></td>
		</tr>
		<tr>
			<td>Total Deaths</td>
			<td><?php echo $worldwideData->TotalDeaths;?></td>
			<td><?php echo $td;?></td>
		</tr>
	</tbody>
</table>
</body>
</html>