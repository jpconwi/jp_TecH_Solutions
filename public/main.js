(function () {
  var log = document.getElementById("log");
  var yr = document.getElementById("yr");
  if (yr) yr.textContent = new Date().getFullYear();
  if (!log) return;

  var lines = [
    "boot: esp32 ready",
    "wifi: connected",
    "sensor: water_level=72%",
    "sensor: temp=29.4C",
    "relay: pump OFF",
    "sensor: water_level=41%",
    ["alert: level low, pump ON", "warn"],
    "relay: pump ON",
    "sensor: water_level=68%",
    "relay: pump OFF",
    "dashboard: synced"
  ];

  function add(entry) {
    var text = Array.isArray(entry) ? entry[0] : entry;
    var cls = Array.isArray(entry) ? entry[1] : "";
    var row = document.createElement("div");
    row.textContent = "> " + text;
    if (cls) row.className = cls;
    log.appendChild(row);
    while (log.children.length > 9) log.removeChild(log.firstChild);
  }

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce) { lines.slice(0, 8).forEach(add); return; }

  var i = 0;
  setInterval(function () { add(lines[i % lines.length]); i++; }, 1100);
})();
