AuthInterceptor = ->
  AuthInterceptor =
    request: (config) ->
      return config
  return AuthInterceptor

angular
  .module 'townhall.services.auth-interceptor', []
  .factory 'AuthInterceptor', AuthInterceptor
  .config ($httpProvider) ->
    $httpProvider.interceptors.push 'AuthInterceptor'