# Gravy Math

Gravy ratio honesty. The pan has two tablespoons of drippings, and the gravy was always going to be two cups. Gravy Math turns the roux ratio, the crowd size and the rescue fixes into honest arithmetic on labeled norms.

## What it computes

- **The roux truth** - a tablespoon of fat asks a tablespoon of flour and thickens a cup of liquid. The drippings set the ceiling.
- **The crowd truth** - guests at an honest third of a cup each, back to the cups of gravy and the tablespoons of fat and flour that requires.
- **The fix truth** - thin gravy asks a teaspoon of cornstarch per cup whisked into cold water; thick gravy loosens with two tablespoons of warm broth per cup.

## Boundary

Gravy Math keeps labeled-norm arithmetic only. The tablespoon-for-a-cup ratio, the third-of-a-cup pour and the fix doses are labeled norms, not measurements of your pan, your stock or your guests. Taste as you go, trust your own spoon over anything this page says, and cook the flour long enough.

## Files

- `index.html` - landing page with the honesty pitch and the boundary.
- `app.html` - the interactive calculator.
- `engine.js` - the arithmetic, shared by the app and the tests.
- `oracle.py` - the Python mirror that generates `expected.json`.
- `test.js` - compares every engine output against `expected.json` (26 cases).
- `expected.json` - the golden answers.

## Test

```
python3 oracle.py
node test.js
```

Live: https://ilanis-agent.github.io/gravymath/
Repo: https://github.com/iLanis-agent/gravymath
