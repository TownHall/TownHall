require 'jquery'
require 'angular/angular'
require 'angular-resource/angular-resource'
require 'angular-route/angular-route'

require './main/main-controller'

require './templates'


angular
  .module 'townhall', [
    'ngRoute'
    'ngResource'
    'townhall.main'
    'townhall.templates'
  ]