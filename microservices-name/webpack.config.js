const path = require('path')
const glob = require('glob')

// Credits: https://hackernoon.com/webpack-creating-dynamically-named-outputs-for-wildcarded-entry-files-9241f596b065
const entryArray = glob.sync('./src/index.ts')

module.exports = {
  entry: entryArray,
  devtool: 'source-map',
  target: 'node',
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/
      }
    ]
  },
  resolve: {
    extensions: ['.tsx', '.ts', '.js']
  },
  // Output directive will generate build/<function-name>/index.js
  output: {
    filename: '[name]/index.js',
    path: path.resolve(__dirname, 'build'),
    devtoolModuleFilenameTemplate: '[absolute-resource-path]',
    // Credit to Richard Buggy!!
    libraryTarget: 'commonjs2'
  }
}