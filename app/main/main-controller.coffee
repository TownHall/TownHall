MainCtrl = (Group) ->
  vm = @
  vm.title = 'Welcome'
  vm.groups = Group.list()

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