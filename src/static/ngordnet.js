$(function() {
	// plot = document.getElementById('plot');
    const width = 640;
    const height = 400;
    const marginTop = 20;
    const marginRight = 20;
    const marginBottom = 30;
    const marginLeft = 40;

    plot = d3.select("svg")
	textresult = document.getElementById('textresult');

    
    console.log("initialized")
  
    // Declare the x (horizontal position) scale.
    const x = d3.scaleUtc()
        .domain([new Date("2023-01-01"), new Date("2024-01-01")])
        .range([marginLeft, width - marginRight]);

    // Declare the y (vertical position) scale.
    const y = d3.scaleLinear()
        .domain([0, 100])
        .range([height - marginBottom, marginTop]);
    
    plot.attr("width", width).attr("height, height");

    // Add the x-axis.
    plot.append("g")
        .attr("transform", `translate(0,${height - marginBottom})`)
        .call(d3.axisBottom(x));

    // Add the y-axis.
    plot.append("g")
        .attr("transform", `translate(${marginLeft},0)`)
        .call(d3.axisLeft(y));                

	var host;

    host = 'http://localhost:4567'; // Establish a connection to host

    // Create URLs 
    const history_server = host + '/history';
    const historytext_server = host + '/historytext';
    const hyponyms_server = host + '/hyponyms';

    function get_params() {
        return {
            words: document.getElementById('words').value,
            startYear: document.getElementById('start').value,
            endYear: document.getElementById('end').value,
            // k: document.getElementById('k').value
        }
    }

    $('#history').click(historyButton);
    $('#historytext').click(historyTextButton);
    $('#hyponyms').click(hyponymsButton);

    function historyButton() {
        $("#textresult").hide();
        $("#plot").show();

        var params = get_params();
        console.log(params);
        $.get({
            async: false,
            url: history_server,
            data: params,
            success: function(data) {
            	console.log(data)

                // we have to somehow return our timeseries in the form of
                // JSON objects
                
            },
            error: function(data) {
            	console.log("error")
            	console.log(data);
            	// plot.src = 'data:image/png;base64,' + data;
            },
            dataType: 'json'
        });
    }

    function historyTextButton() {
        console.log("history text call");
        $("#plot").hide();
        $("#textresult").show();

        var params = get_params();
        console.log(params);
        $.get({
            url: historytext_server,
            data: params,
            success: function(data) {
            	console.log(data)
                res = JSON.stringify(data)
                console.log(res)
                textresult.value = res;
            },
            error: function(data) {
            	console.log(`error trying to access ${historytext_server}`)
            	console.log(data);
            },
            dataType: 'json'
        });
    }

    function hyponymsButton() {
        console.log("hyponyms call");
        $("#plot").hide();
        $("#textresult").show();

        var params = get_params();
        console.log(params);
        $.get({
            async: false,
            url: hyponyms_server,
            data: params,
            success: function(data) {
                console.log(data)

                textresult.value = data;

            },
            error: function(data) {
                console.log("error")
                console.log(data);
            },
            dataType: 'json'
        });
    }

});