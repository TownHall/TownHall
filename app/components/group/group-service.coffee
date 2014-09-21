Group = ($resource, Config) ->

  groupEndpoint = '/groups/:id'
  membersEndpoint = '/groups/:id/members/:memberId'

  #don't bother implementing get or delete/remove methods, as $resource supports those out of the box
  GroupResource = $resource Config.apiURL + groupEndpoint,
    id: '@id'
    memberId: '@memberId'
  ,
    list: #returns a list of groups, synonymous with built in resource method `query` but the response is NOT an array
      method: 'get'
      transformResponse: (data, headersGetter) ->
        return JSON.parse data
          .groups
      isArray: true
    edit: #edit a group
      method: 'put'
    create: #make a new group, synonymouse with built in resource method `save`
      method: 'post'
    member:
      method: 'get'
      url: Config.apiURL + membersEndpoint
    listMembers: #get a list of the members in a group
      method: 'get'
      url: Config.apiURL + membersEndpoint
    addMember: #add a user to a group as a member
      method: 'post'
      url: '/groups/:id/join'
    removeMember: #remove a member user from a group
      method: 'delete'
      url: Config.apiURL + membersEndpoint
    promoteMember: #promote a member within a group
      method: 'post'
      url: Config.apiURL + membersEndpoint

  return GroupResource

angular
  .module 'townhall.services.group', []
  .factory 'Group', Group