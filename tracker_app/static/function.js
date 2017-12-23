//var jsonObserv = {{ observations|safe }};


$('#myBtn1').click(function(){
	$('#myCarousel').carousel('next');
	
});
$('#myBtn2').click(function(){
	$('#myCarousel').carousel('prev');
	
});
drawChart1("chart_container_weight", jsonObj.daily_weight, jsonObj.date, {title : "Weight Tracker", yAxis_title : "kg", series_name : "weight"})
drawChart1("chart_container_hydrate", jsonObj.daily_hydrate, jsonObj.date, {title : "Hydrate Tracker", yAxis_title : "c.c", series_name : "Hydrate Volume"})
drawChart2("chart_container_bp", jsonObj.daily_sbp, jsonObj.daily_dbp, jsonObj.date, {title : "Body Pressure Tracker", yAxis_title : "mmHg", series_name1 : "Systolic blood pressure", series_name2 : "Diastolic blood pressure"})
drawChart1("chart_container_sleep", jsonObj.daily_sleep, jsonObj.date, {title : "Sleep Tracker", yAxis_title : "hours", series_name : "Sleep time"})
function drawChart1(divID, parameter, date, customType){
	var id = "#" + divID;
	$(function(){
		$(id).highcharts({
			chart: {
				backgroundColor: "#E7FCE7"
			},
			title: {
				text: customType.title,
				style: {
					fontWeight : 'bold'
				}
			},
			xAxis: {
				categories: date
			},
			yAxis: {
				gridLineWidth: 2,
				title: {
					text: customType.yAxis_title
				}
			},
			/*plotOptions: {
				
				series: {
					threshold: 0,
					trackByArea: true,
					stickyTracking: false
				}
					
				
			},*/
			series: 
			[
				{
					name: customType.series_name,
					data: parameter
				}, 
			]
		});
	})
};
function drawChart2(divID, parameter1, parameter2, date, customType){
	var id = "#" + divID;
	$(function(){
		$(id).highcharts({
			chart: {
				backgroundColor: "#E7FCE7"
			},
			title: {
				text: customType.title,
				style: {
					fontWeight : 'bold'
				}
			},
			xAxis: {
				categories: date
			},
			yAxis: {
				title: {
					text: customType.yAxis_title
				}
			},
			series: 
			[
				{
					name: customType.series_name1,
					data: parameter1
				}, 
				{
					name: customType.series_name2,
					data: parameter2
				}, 
			]
		});
	})
};
