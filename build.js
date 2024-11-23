const tailwindcss = require('tailwindcss');
const fs = require('fs');
const postcss = require('postcss');
const path = require('path');

fs.readFile(path.resolve(__dirname, 'static/css/styles.css'), 'utf8', (err, css) => {
  if (err) throw err;

  postcss([tailwindcss])
    .process(css, { from: undefined })
    .then(result => {
      fs.writeFile(path.resolve(__dirname, 'static/css/output.css'), result.css, () => true);
    });
});
