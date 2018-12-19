/*
 ./webpack.config.js
 */
const path = require('path');

const HtmlWebpackPlugin = require('html-webpack-plugin');
const HtmlWebpackPluginConfig = new HtmlWebpackPlugin({template: './client/index.html',
                                                      filename: 'index.html',
                                                      inject: 'body'})

module.exports = {
    entry: './client/index.js',
    output: {
        path: path.resolve('dist'),
        filename: 'index_bundle.js'
    },
    module: {
        rules: [
                { test: /\.css$/,
                  use: [
                    { loader: "style-loader" },
                    { loader: "css-loader" }
                    ]
                },
                {
                  test: /\.js$/,
                  exclude: /node_modules/,
                  use: "babel-loader"
                }, {
                  test: /\.jsx?$/,
                  exclude: /node_modules/,
                  use: "babel-loader"
                }, {
		  test: /\.(jpe?g|png|gif)$/i,
            	  use: "file-loader"
		}
                ]
            },
    devServer: {
        contentBase: path.join(__dirname, 'dist'),
        compress: true,
        port: 8080,
        headers: {
            'Access-Control-Allow-Origin': '*'
        }
    },
    plugins: [HtmlWebpackPluginConfig]
}
