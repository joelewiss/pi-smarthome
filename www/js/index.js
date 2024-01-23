const list = `
  <div id="app-list">
    <a href="/">Dashboard</a>
    <a href="/coffee.html">Coffee</a>
    <a href="list.html">Action List</a>
  </div>`

$(() => {
  $("body").prepend(list);
});
