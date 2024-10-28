/** @type {import('tailwindcss').Config} */
const palettes = {
  'fuchsia-blue': {
        '50': '#eef0ff',
        '100': '#e1e4fe',
        '200': '#c9cdfc',
        '300': '#a7acfa',
        '400': '#8684f5',
        '500': '#7467ed',
        '600': '#7159e3',
        '700': '#563cc6',
        '800': '#4733a0',
        '900': '#3c307f',
        '950': '#241c4a',
    }
}

module.exports = {
  darkMode: 'class',
  content: [
    './templates/**/*.html',
    './*/templates/**/*.html',
    './templates/**/*.svg',
    './*/templates/**/*.svg',
    '!./node_modules',
    '!./venv',
    './**/*.py',
  ],
  theme: {
    extend: {
      colors: {
        'primary': palettes['fuchsia-blue'],
      }
    },
  },
  plugins: [],
}

