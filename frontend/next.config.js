/** @type {import('next').NextConfig} */
const nextConfig = {
    reactStrictMode: false,
    experimental: {
      appDir: true,
      scrollRestoration: false,
    },
    compiler: {
      styledComponents: true,
    },
}

module.exports = nextConfig
