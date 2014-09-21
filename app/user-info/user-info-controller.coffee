UserInfoCtrl = ($routeParams, $scope, User, Auth) ->
  vm = @
  vm.user = User.get
    id: $routeParams.userId
  vm.authUser = Auth.user
  vm.save = (user) ->
    vm.edit = false
    User.edit
      id: user.id
  $scope.$on 'authUser', (event, user) ->
    console.log user
    vm.authUser = user
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