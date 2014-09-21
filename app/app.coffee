require 'jquery'
require 'angular/angular'
require 'angular-resource/angular-resource'
require 'angular-route/angular-route'

require './main/main-controller'
require './group-info/group-info-controller'
require './user-info/user-info-controller'
require './discussion/discussion-controller'

require './components/group/group-service'
require './components/user/user-service'
require './components/discussion/discussion-service'
require './components/proposal/proposal-service'
require './components/comment/comment-service'
require './components/tag/tag-service'
require './components/auth-interceptor/auth-interceptor-service'
require './components/auth/auth-service'

require './components/login/login-directive'

require './templates'


angular
  .module 'townhall', [
    'ngRoute'
    'ngResource'
    'townhall.main'
    'townhall.group-info'
    'townhall.user-info'
    'townhall.discussion'
    'townhall.services.group'
    'townhall.services.user'
    'townhall.services.discussion'
    'townhall.services.proposal'
    'townhall.services.comment'
    'townhall.services.tag'
    'townhall.services.auth-interceptor'
    'townhall.services.auth'
    'townhall.directives.login'
    'townhall.templates'
  ]
  .constant 'Config',
    apiURL: 'http://demo4757189.mockable.io'