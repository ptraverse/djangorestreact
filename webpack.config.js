var path = require("path");
var webpack = require("webpack");

module.exports = {
    entry: path.resolve(__dirname, "frontend/index.jsx"),
    output: {
        path: path.resolve(__dirname, "out"),
        publicPath: 'out/',
        filename: 'app.js'
    },
    resolve: {
        modulesDirectories: ["node_modules", "bower_components"]
    },
    module: {
        loaders: [
            {
                test: /\.jsx?$/,
                loader: 'babel',
                exclude: /node_modules/
            }
        ]
    },
    plugins: [
        new webpack.ResolverPlugin(
            new webpack.ResolverPlugin.DirectoryDescriptionFilePlugin(".bower.json", ["main"])
        )
    ]
};