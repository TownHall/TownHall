MainCtrl = (Group) ->
  vm = @
  vm.groups = Group.list()
  return

Config = ($routeProvider) ->
  $routeProvider
    .when '/',
      templateUrl: 'main/main.html'
      controller: 'MainCtrl'
      controllerAs: 'main'

angular
  .module 'townhall.main', []
  .config Config
  .controller 'MainCtrl', MainCtrl