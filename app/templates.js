angular.module("townhall.templates", []).run(["$templateCache", function($templateCache) {$templateCache.put("main/main.html","<div class=\"row\">\n  <div class=\"small-12 columns\">\n    <h1>Main</h1>\n    <p>{{hello}}</p>\n  </div>\n</div>");}]);