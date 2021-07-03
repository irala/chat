const path = require('path');
const webpack = require('webpack');
function resolveSrc(_path) {
  return path.join(__dirname, _path)
}

module.exports = {
  // configureWebpack: {
  //   // Set up all the aliases we use in our app.
  //   resolve: {
  //     alias: {
  //       'src': resolveSrc('src'),
  //       'chart.js': 'chart.js/dist/Chart.js',
  //       // add this line for include components inside swal alert
  //       'vue$':'vue/dist/vue.esm.js'
  //     }
  //   },
  //   plugins: [
  //     new webpack.optimize.LimitChunkCountPlugin({
  //       maxChunks: 6
  //     })
  //   ]
  // },
  // chainWebpack(config) {
  //   // config.plugin('workbox')
  //   config.plugins.delete('prefetch');
  // },
  // pwa: {
  //   name: 'chat',
  //   themeColor: '#66615B',
  //   msTileColor: '#66615B',
  //   appleMobileWebAppCapable: 'yes',
  //   appleMobileWebAppStatusBarStyle: '#66615B'
  // },
  devServer: {
    port: 8080,
    // compress: true,
    // http2: true,
    clientLogLevel: 'info',
    https: false,
    proxy: {
      'identity': {
        target: 'http://localhost:8081',
        changeOrigin: true,
        // logLevel: "debug",
        pathRewrite: {
          '^/identity': ''
        }
      }
    }
  },
  css: {
    sourceMap: true
  },

  runtimeCompiler: true
};
