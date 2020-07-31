const COLORS = {
    "Front Door": {
        "Closed": "darkblue",
        "Opened": "#0000bf",
    },
    "Back Door": {
        "Closed": "#004d00",
        "Opened": "darkgreen",
    }
}



// jQuery shorthand for onDocumentReady
$(() => {
    $.get("/action/doors/log", function(data) {
        var stats = {"Front Door": "", "Back Door": ""}

        let log = JSON.parse(data);
        window.events = []
        
        for (evnt of log) {
            let sensor = evnt.sensor == "front" ? "Front Door" : "Back Door";
            let action = evnt.action == "close" ? "Closed" : "Opened";
            // We need to do add the UTC timezone into here because JS 
            // Date.parse interprets ISO strings without a timezone as local 
            // time. This forces JS to convert from UTC to localtime
            // As per: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse
            let time = new Date(`${evnt.time}+00:00`);
            
            let newevnt = {
                sensor: sensor,
                action: action,
                time: time,
            };

            window.events.push(newevnt);
        }


        for (evnt of events) {
            stats[evnt.sensor] = evnt.action
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


        var now = Date.now();
        let reverse = events.slice().reverse();
        for (let i = 0; i < reverse.length; i++) {
            let evnt = reverse[i]
            let color = COLORS[evnt.sensor][evnt.action]; 
            let timeStr = evnt.time.toLocaleDateString("en-us") +
                        " " + evnt.time.toLocaleTimeString("en-us");

            let elm = `
                <tr style="background-color: ${color}">
                    <td>${evnt.sensor}</td>  
                    <td>${evnt.action}</td> 
                    <td>${timeStr}</td>
                    <td><time datetime="${evnt.time.toISOString()}"></time></td>
                <tr>
            `;
            
            // Again, I don't like it, but JS does epoch in milis not
            // seconds... I make this mistake every time. Maybe if I write 
            // enough useless comments it will help me remember.
            if (now - evnt.time < (86400 * 1000)) {
                $("#log").append(elm);
            }

            // Add padding between groups of events
            if (i < reverse.length - 1 && reverse[i + 1].sensor != evnt.sensor) {
                $("#log").append("<p></p>");
            }
        }

        $("time").timeago();
    });
});
