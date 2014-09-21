#this is having some circular dependency issues (with Auth, $http, and $httpProvider)
#funny syntax and commented code below is to fix that

# AuthInterceptor = (Auth) ->
#   AuthInterceptor =
#     request: (config) ->
#       config.headers = config.headers or {}
#       config.headers.Authorization = 'Bearer ' + Auth.token if Auth.token
#       return config
#   return AuthInterceptor

angular
  .module 'townhall.services.auth-interceptor', []
  # .factory 'AuthInterceptor', AuthInterceptor
  .config ($httpProvider) ->
    #$httpProvider.interceptors.push 'AuthInterceptor'
    $httpProvider.interceptors.push ($injector) ->
      AuthInterceptor =
        request: (config) ->
          $injector.invoke ($http, Auth) ->
            config.headers = config.headers or {}
            config.headers.Authorization = 'Bearer ' + Auth.token if Auth.token
            return config
        response: (res) ->
          if res.status == 403
            console.log 'gotta login to do this'
            #user not logged in, soooooo...?
            #probably tell the user that they tried to use an authenticated-only feature
          return res
      return AuthInterceptor