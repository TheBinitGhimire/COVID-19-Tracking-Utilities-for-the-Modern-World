function startTracking(){
// WorldWide
	let ta1 = document.getElementById("ta1");
	let nc1 = document.getElementById("tc1");
	let nd1 = document.getElementById("td1");
	let tc1 = document.getElementById("tc1");
	let ts1 = document.getElementById("ts1");
	let tu1 = document.getElementById("tu1");
	let td1 = document.getElementById("td1");
// Local
	let ta2 = document.getElementById("ta2");
	let nc2 = document.getElementById("tc2");
	let nd2 = document.getElementById("td2");
	let tc2 = document.getElementById("tc2");
	let ts2 = document.getElementById("ts2");
	let tu2 = document.getElementById("tu2");
	let td2 = document.getElementById("td2");
	worldwideData();
}

$.get("https://api.ipify.org/?format=json", {"ip":"data"})
	.done(function(getIP){
		$.get("http://www.geoplugin.net/json.gp?ip="+getIP.ip, {"geoplugin_countryCode":"data"}, function(getCode){
			var userCountry = JSON.parse(getCode).geoplugin_countryCode;
			localData(userCountry);
		})
	});

function worldwideData(){
	$.get("https://api.thevirustracker.com/free-api?global=stats", function(getWorldWide){
		// console.log(getWorldWide.results);
		let wwD = getWorldWide.results[0];
		ta1.innerHTML = wwD.total_active_cases;
		nc1.innerHTML = wwD.total_new_cases_today;
		nd1.innerHTML = wwD.total_new_deaths_today;
		tc1.innerHTML = wwD.total_cases;
		ts1.innerHTML = wwD.total_serious_cases;
		tr1.innerHTML = wwD.total_recovered;
		tu1.innerHTML = wwD.total_unresolved;
		td1.innerHTML = wwD.total_deaths;
	});
}

function localData(country){
	$.get("https://api.thevirustracker.com/free-api?countryTotal="+country, function(getLocal){
		// console.log(getLocal.countrydata);
		let lD = getLocal.countrydata[0];
		ta2.innerHTML = lD.total_active_cases;
		nc2.innerHTML = lD.total_new_cases_today;
		nd2.innerHTML = lD.total_new_deaths_today;
		tc2.innerHTML = lD.total_cases;
		ts2.innerHTML = lD.total_serious_cases;
		tr2.innerHTML = lD.total_recovered;
		tu2.innerHTML = lD.total_unresolved;
		td2.innerHTML = lD.total_deaths;
	});
}
