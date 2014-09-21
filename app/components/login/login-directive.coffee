Login = (Auth) ->
  Login = {}
  Login.restrict = 'E'
  Login.replace = true
  Login.templateUrl = 'components/login/login.html'

  Login.link = (scope, element, attrs) ->
    return 'yisss'

  return Login

angular
  .module 'townhall.directives.login', []
  .directive 'townhallLogin', Login