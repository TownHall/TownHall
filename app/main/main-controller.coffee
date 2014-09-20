MainCtrl = (Group, User) ->
  vm = @
  vm.groups = Group.list()
  vm.users = User.list()
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