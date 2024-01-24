var switch_status = "";
var schedule_status = "";

function update_switch() {
  $.get("/action/coffee/status/", function(data) {
    $("#powerButton").text(data);
    switch_status = data;
  });
}

function update_schedule() {
  $.get("/action/coffee/schedule_status/", function(data) {
    $("#current_schedule").text(data);
    schedule_status = data;
  });
}


$(() => {
  update_switch();
  update_schedule();
});

function togglePower() {
  if (switch_status == "On") {
    $.get("/action/coffee/off/");
    
  } else {
    $.get("/action/coffee/on/");
  }
}

function setSchedule() {
  const time = $("#scheduleTime").val().split(":");
  const now = new Date();
  // If this is tomorrow's time, add a day
  if (now.getHours() > time[0]) {
    now.setDate(now.getDate() + 1);
  }
  now.setHours(time[0], time[1], 0, 0);
  console.log(now);

  $.post("/action/coffee/schedule_on/", {"time": now.getTime()/1000}, function() {
    update_schedule();
  });
}

function clearSchedule() {
    $.get("/action/coffee/clear_schedule/", function () {
      update_schedule();
    });
}
