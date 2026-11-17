// Kitchen order import: one CSV line of the till export becomes an order row.
var OrderRow = function () {
  function OrderRow(line) {
    this.line = line;
    this.fields = [];
    this.decode();
  }

  OrderRow.prototype.decode = function decode() {
    var out = [];
    var current = "";
    var quoted = false;
    for (var i = 0; i < this.line.length; i++) {
      var ch = this.line[i];
      if (ch === '"') {
        quoted = !quoted;
      } else if (ch === "," && !quoted) {
        out.push(current);
        current = "";
      } else {
        current += ch;
      }
    }
    out.push(current);
    this.fields = out;
  };

  return OrderRow;
}();

function parseOrders(text) {
  return text.split("\n").filter(Boolean).map(function (line) {
    return new OrderRow(line).fields;
  });
}
