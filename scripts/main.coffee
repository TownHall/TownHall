$ = require('jquery')

## Non-AngularJS boilerplate coffeescript code

# $.js = (el) ->
#   $ '[data-js=' + el + ']'
#
# $.js('social-link').on 'click', (e) ->
#   e.preventDefault()
#   w = 700
#   h = 300
#   m_w = $(window).outerWidth() / 2 - w / 8
#   m_h = $(window).outerHeight() / 2 - h / 2
#   window.open $(this).attr('href'), '_blank', 'width=' + w + ', height=' + h + 'location=no, menubar=no, scrollbars=yes, status=no, toolbar=no, top=' + m_h + ', left=' + m_w

## AngularJS boilerplate coffeescript code, uncomment and comment code above for AngularJS projects

require 'angular/angular'

angular.module 'project-template', []
  .controller 'ProjectTemplateCtrl', [
    '$scope',
    ($scope) ->
      $scope.title = 'word around town I\'m a caveman'
      $scope.message = 'rocks on my hand cost eighty grand'
  ]