DiscussionCtrl = ($routeParams, Discussion) ->
  vm = @
  vm.discussion = Discussion.get
    id: $routeParams.id
  return

Config = ($routeProvider) ->
  $routeProvider
    .when '/discussion/:id',
      templateUrl: 'discussion/discussion.html'
      controller: 'DiscussionCtrl'
      controllerAs: 'discussion'

angular
  .module 'townhall.discussion', []
  .config Config
  .controller 'DiscussionCtrl', DiscussionCtrl