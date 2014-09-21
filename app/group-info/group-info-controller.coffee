GroupInfoCtrl = ($routeParams, Group, Discussion) ->
  vm = @
  vm.group = Group.get
    id: $routeParams.groupId
  vm.discussions = Discussion.list
    groupId: $routeParams.groupId
  return

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