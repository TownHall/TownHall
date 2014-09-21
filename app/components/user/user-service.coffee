User = ($resource, Config) ->
  
  userEndpoint = '/users/:id'

  #don't bother implementing get or delete/remove methods, as $resource supports those out of the box
  UserResource = $resource Config.apiURL + userEndpoint,
    id: '@id'
  ,
    list:
      method: 'get'
      transformResponse: (data, headersGetter) ->
        return JSON.parse data
          .users
      isArray: true
    edit:
      method: 'put'
    create:
      method: 'post'

  return UserResource

angular
  .module 'townhall.services.user', []
  .factory 'User', User