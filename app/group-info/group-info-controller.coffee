GroupInfoCtrl = ($routeParams, Group) ->
  vm = @
  vm.group = Group.get
    id: $routeParams.groupId

Config = ($routeProvider) ->
  $routeProvider
    .when '/group-info/:groupId',
      templateUrl: 'group-info/group-info.html'
      controller: 'GroupInfoCtrl'
      controllerAs: 'groupInfo'

angular
  .module 'townhall.group-info', []
  .config Config
  .controller 'GroupInfoCtrl', GroupInfoCtrl