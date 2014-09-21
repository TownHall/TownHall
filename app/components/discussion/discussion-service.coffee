Discussion = ($resource, Config) ->

  groupDiscussionEndpoint = '/groups/:groupId/discussions'
  discussionEndpoint = '/discussion/:id'
  discussionCommentEndpoint = '/discussion/:id/comment'


  #don't bother implementing get or delete/remove methods, as $resource supports those out of the box
  DiscussionResource = $resource Config.apiURL + discussionEndpoint,
    id: '@id'
    groupId: '@groupId'
  ,
    list:
      method: 'get'
      url: Config.apiURL + groupDiscussionEndpoint
      transformResponse: (data, headersGetter) ->
        return JSON.parse data
          .discussions
      isArray: true
    create:
      method: 'post'
      url: Config.apiURL + groupDiscussionEndpoint
    edit:
      method: 'put'
    comment:
      method: 'post'
      url: Config.apiURL + discussionCommentEndpoint

  return DiscussionResource

angular
  .module 'townhall.services.discussion', []
  .factory 'Discussion', Discussion