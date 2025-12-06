$(function() {
	// plot = document.getElementById('plot');
    const width = 840;
    const height = 400;
    const marginTop = 20;
    const marginRight = 20;
    const marginBottom = 30;
    const marginLeft = 50;

    plot = d3.select("svg")
	textresult = document.getElementById('textresult');

                    
    
    console.log("initialized")
  

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
            	//console.log(data)

                // we have to somehow return our timeseries in the form of
                // JSON objects
                console.log(data)

                plot.selectAll("*").remove()

                // Declare the x (horizontal position) scale.
                const x = d3.scaleLinear(d3.extent(data, d => d.year), [marginLeft, width-marginRight]);

                // Declare the y (vertical position) scale.
                const y = d3.scaleLinear([0, d3.max(data, d=>d.count)], [height - marginBottom, marginTop])

                // Declare the line generator
                const line = d3.line()
                    .x(d => x(d.year))
                    .y(d => y(d.count))

                
                plot.attr("width", width)
                    .attr("height", height)
                    .attr("viewBox", [0,0,width,height])
                    .attr("class", "svg-style")
                    //.attr("style", "max-width: 100%; height: auto; height: intrinsic;");

                // Add the x-axis.
                plot.append("g")
                    .attr("transform", `translate(0,${height - marginBottom})`)
                    .call(d3.axisBottom(x).ticks(width/40).tickSizeOuter(0));

                // Add the y-axis.
                plot.append("g")
                    .attr("transform", `translate(${marginLeft},0)`)
                    .call(d3.axisLeft(y).ticks(height / 40))
                    .call(g => g.select(".domain").remove())
                    .call(g => g.selectAll(".tick line").clone()
                        .attr("x2", width - marginLeft - marginRight)
                        .attr("stroke-opacity", 0.1))
                    .call(g => g.append("text")
                        .attr("x", -marginLeft)
                        .attr("y", 10)
                        .attr("fill", "currentColor")
                        .attr("text-anchor", "start")
                        .text("Count"))

                plot.append("path")
                    .attr("fill", "none")
                    .attr("stroke", "steelblue")
                    .attr("stroke-width", 1.5)
                    .attr("d", line(data))

                return plot.node()

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

    function redraw(data) {
        const selection = d3.select('svg')
            .data(data)

        selection.exit()
            .remove()

        // const entering = selection.enter()
        //     .append()
    }

});