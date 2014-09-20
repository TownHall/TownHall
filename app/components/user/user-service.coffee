User = ($resource, Config) ->
  userEndpoint = '/users/:id'

  UserResource = $resource Config.apiURL + userEndpoint,
    id: '@id'
  ,
    list:
      method: 'get'
      transformResponse: (data, headersGetter) ->
        return JSON.parse data
          .users
      isArray: true
    login:
      method: 'post'
      url: '/users/login'
    edit:
      method: 'put'
    create:
      method: 'post'

angular
  .module 'townhall.services.user', []
  .factory 'User', User