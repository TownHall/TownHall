Login = (Auth) ->
  Login = {}
  Login.restrict = 'E'
  Login.replace = true
  Login.templateUrl = 'components/login/login.html'

  Login.link = (scope, element, attrs) ->
    scope.loggedIn = Auth.isAuthenticated()
    scope.user = Auth.user
    scope.login = (user, pass) ->
      Auth.authenticate user, pass
      scope.loggedIn = Auth.isAuthenticated()
      scope.user = Auth.user
    return

  return Login

angular
  .module 'townhall.directives.login', []
  .directive 'townhallLogin', Login