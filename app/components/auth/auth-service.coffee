Auth = ($http, Config) ->
  Auth = {}
  Auth.user = false

  Auth.authenticate = (creds) -> #creds should be an object {username: "devers", password: "blah"}
    return $http
      .post Config.apiURL + '/user/login', creds
      .then (res) ->
        Auth.user = res.data.user
        return Auth.user

  Auth.isAuthenticated = ->
    return !!Auth.user

  return Auth

angular
  .module 'townhall.services.auth', []
  .factory 'Auth', Auth