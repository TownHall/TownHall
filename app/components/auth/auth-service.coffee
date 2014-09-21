Auth = ($http, Config) ->
  Auth = {}
  Auth.user = false
  Auth.token = false

  Auth.authenticate = (creds) -> #creds should be an object {username: "devers", password: "blah"}
    # return $http
    #   .post Config.apiURL + '/user/login', creds
    #   .then (res) ->
    #     Auth.user = res.data.user
    #     Auth.token = res.data.token

    #for testing purposes, lets pretend we always log in correctly as devers talmage

    Auth.user =
      id: 1
      name: 'Devers Talmage'
    Auth.token = 'abc123'
    return

  Auth.isAuthenticated = ->
    return !!Auth.user

  return Auth

angular
  .module 'townhall.services.auth', []
  .factory 'Auth', Auth