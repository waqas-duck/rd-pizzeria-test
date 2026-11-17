// Menu card colours: turns the theme's hex colours into rgba() for the
// translucent category badges.
function hexToRgb(hex) {
  var pattern = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i;
  var match = pattern.exec(hex);
  if (!match) {
    return [0, 0, 0];
  }
  return [parseInt(match[1], 16), parseInt(match[2], 16), parseInt(match[3], 16)];
}

function badgeBackground(hex, alpha) {
  var rgb = hexToRgb(hex);
  return "rgba(" + rgb[0] + ", " + rgb[1] + ", " + rgb[2] + ", " + alpha + ")";
}

document.querySelectorAll("[data-badge-colour]").forEach(function (el) {
  el.style.backgroundColor = badgeBackground(el.getAttribute("data-badge-colour"), 0.15);
});
