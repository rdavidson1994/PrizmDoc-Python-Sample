"use strict";

var fs = require("fs");
var path = require("path");

fs.copyFile(path.join(__dirname, "..", "node_modules", "@prizmdoc", "viewer-core", "viewercontrol.js"), path.join(__dirname, "..", "PrizmDoc-Python-Sample", "static", "js", "lib", "viewercontrol.js"), function(error) {
    if (error) {
        throw new Error(JSON.stringify(error, undefined, "\t"));
    }
});

fs.copyFile(path.join(__dirname, "..", "node_modules", "@prizmdoc", "viewer-core", "viewercontrol.css"), path.join(__dirname, "..", "PrizmDoc-Python-Sample", "static", "css", "lib", "viewercontrol.css"), function(error) {
    if (error) {
        throw new Error(JSON.stringify(error, undefined, "\t"));
    }
});
