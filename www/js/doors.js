

// jQuery shorthand for onDocumentReady
$(() => {
    $.get("/action/doors/log", function(data) {
        var stats = {"Front Door": "", "Back Door": ""}

        log = JSON.parse(data);
        log.reverse();
        for (evnt of log) {
            let sensor = evnt.sensor == "front" ? "Front Door" : "Back Door";
            let action = evnt.action == "close" ? "Closed" : "Opened";

            stats[sensor] = action        

            // We need to do add the UTC timezone into here because JS Date.parse interprets ISO strings
            // without a timezone as local time. This forces JS to convert from UTC to localtime
            // As per: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse
            let time = new Date(`${evnt.time}+00:00`);
            let color = evnt.action == "close" ? "#303030" : "darkblue";
            let elm = `
                <tr style="background-color: ${color}">
                    <td>${sensor}</td>  
                    <td>${action}</td>  
                    <td><time datetime="${time.toISOString()}" title="${time.toString()}"></time></td>
                <tr>
            `;
            
            $("#log").append(elm);
        }

        for (sensor in stats) {
            let state = stats[sensor];
            let elm = `<p>${sensor}: ${state}</p>`
            if (state == "Closed") {
                $("#app").prepend(`<div style="background-color: #303030">${elm}</div>`);
            } else {
                $("#app").prepend(`<div style="background-color: darkblue">${elm}</div>`);
            }
        }

        $("time").timeago();
    });
});
