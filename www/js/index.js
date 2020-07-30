const list = `
  <div id="app-list">
    <a href="/">Dashboard</a>
    <a href="list.html">Action List</a>
    <a href="doors.html">Doors</a>
  </div>`

$(() => {
  $("body").prepend(list);
});
