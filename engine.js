// Gravy Math engine - hypothetical arithmetic on labeled norms only.
// Thickening ratios, per-guest pours and fix doses are labeled norms,
// not measurements of your pan, your stock or your guests.

function plural(n, one, many) { return n === 1 ? one : many; }
function tenths(x) { return Math.floor(x * 10 + 0.5) / 10; }
function fixed1(x) { return tenths(x).toFixed(1); }

function rouxTruth(fat) {
  if (!(fat > 0)) throw new Error("the fat must be above zero");
  return `${fat} ${plural(fat, "tablespoon", "tablespoons")} of fat ${fat === 1 ? "asks" : "ask"} ${fat} ${plural(fat, "tablespoon", "tablespoons")} of flour and ${fat === 1 ? "thickens" : "thicken"} ${fat} ${plural(fat, "cup", "cups")} of liquid honestly.`;
}

function crowdTruth(guests) {
  if (!(guests > 0)) throw new Error("the guests must be above zero");
  const cups = tenths(guests / 3); // labeled norm: a third of a cup per guest; rounded figure the verdict judges
  return `${guests} ${plural(guests, "guest", "guests")} at an honest third of a cup each ${guests === 1 ? "asks" : "ask"} ${fixed1(cups)} cups of gravy - ${fixed1(cups)} ${plural(tenths(cups), "tablespoon", "tablespoons")} of fat and flour honestly.`;
}

function fixTruth(cups, mode) {
  if (!(cups > 0)) throw new Error("the cups must be above zero");
  if (mode === "thin") {
    return `${fixed1(cups)} ${plural(tenths(cups), "cup", "cups")} of thin gravy ${tenths(cups) === 1 ? "asks" : "ask"} ${fixed1(cups)} ${plural(tenths(cups), "teaspoon", "teaspoons")} of cornstarch whisked into cold water honestly.`;
  }
  if (mode === "thick") {
    return `${fixed1(cups)} ${plural(tenths(cups), "cup", "cups")} of thick gravy ${tenths(cups) === 1 ? "loosens" : "loosen"} with ${fixed1(cups * 2)} ${plural(tenths(cups * 2), "tablespoon", "tablespoons")} of warm broth honestly.`;
  }
  throw new Error("the fix must be thin or thick");
}

if (typeof module !== "undefined") {
  module.exports = { rouxTruth, crowdTruth, fixTruth };
}
