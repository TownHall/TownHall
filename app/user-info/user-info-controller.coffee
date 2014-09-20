UserInfoCtrl = ($routeParams, User) ->
  vm = @
  vm.user = User.get
    id: $routeParams.userId
  return

Config = ($routeProvider) ->
  $routeProvider
    .when '/user-info/:userId',
      templateUrl: 'user-info/user-info.html'
      controller: 'UserInfoCtrl'
      controllerAs: 'userInfo'

angular
  .module 'townhall.user-info', []
  .config Config
  .controller 'UserInfoCtrl', UserInfoCtrl