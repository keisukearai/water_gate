/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
    "./node_modules/flowbite-react/**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        /** カラー名': 'カラーコード */
        'header-color': '#FFFFFF',
        'header-text-color': '#FFFFFF',
        'menu-color': '#005bac',
        'body-color': '#FFFFFF',
        'footer-color': '#212a37',
        'footer-text-color': '#FFFFFF',
      },
    },
  },
  plugins: [
    require("flowbite/plugin")
  ],
}
