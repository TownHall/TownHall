MainCtrl = ($scope) ->

Config = ($routeProvider) ->
  $routeProvider
    .when '/',
      templateUrl: 'main/main.html'
      controller: 'MainCtrl'

angular
  .module 'townhall.main', []
  .config Config
  .controller 'MainCtrl', MainCtrl