/** @type {import('tailwindcss').Config} */
const palettes = {
  'breaker-bay': {
        '50': '#f2fbfa',
        '100': '#d4f3f0',
        '200': '#aae5e1',
        '300': '#77d1ce',
        '400': '#4bb6b6',
        '500': '#31999a',
        '600': '#257a7c',
        '700': '#216264',
        '800': '#1f4d50',
        '900': '#1e4143',
        '950': '#0c2427',
    },
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
        'primary': palettes['breaker-bay'],
      }
    },
  },
  plugins: [],
}

