require 'jquery'
require 'angular/angular'
require 'angular-resource/angular-resource'
require 'angular-route/angular-route'

require './main/main-controller'

require './components/group/group-service'
require './components/user/user-service'
require './components/discussion/discussion-service'
require './components/proposal/proposal-service'
require './components/comment/comment-service'
require './components/tag/tag-service'

require './templates'


angular
  .module 'townhall', [
    'ngRoute'
    'ngResource'
    'townhall.main'
    'townhall.services.group'
    'townhall.services.user'
    'townhall.services.discussion'
    'townhall.services.proposal'
    'townhall.services.comment'
    'townhall.services.tag'
    'townhall.templates'
  ]