$(function() {
    $.get("/action/list", function(data) {
        $("#content").empty();
        for (module in data) {
            heading = `<h3>${module}</h3>`;
            $("#content").append(heading);

            for (action of data[module].actions) {
                action = `<button id="${module}-${action}" onclick="javascript:execute('${module}', '${action}');">${action}</button>`;
                $("#content").append(action);
            }

            spacer = "<div class='spacer'></div>";
            $("#content").append(spacer);
        }

        output = `<div id="output"></div>`;
        $("body").append(output);
    });
});

function execute(module, action) {
    request = `/action/${module}/${action}`;
    $.get(request, function(response) {
        $("#output").html(response);
    });
}
