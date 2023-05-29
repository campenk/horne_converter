/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./app/**/*.{html,js}',],
 theme: {
    extend:
    {
      fontFamily: {
        'courier': ['Courier Prime', 'serif'],
        'veteranTypewriter': ["Veteran Typewriter", "mono"]
      },
    },
  },
  plugins: [],
}

