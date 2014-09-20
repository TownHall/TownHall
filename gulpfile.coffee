gulp = require 'gulp'
browserify = require 'browserify'
shim = require 'browserify-shim'
source = require 'vinyl-source-stream'
plugins = require('gulp-load-plugins') lazy: false
penthouse = require 'penthouse'
fs = require 'fs'

onError = (err) ->
  plugins.util.beep()
  console.log err
  return

URL = 'http://localhost/TownHall'

gulp.task 'browserify', ->
  browserify
    entries: './app/app.coffee'
    extensions: [
      '.coffee'
      '.js'
      '.json'
    ]
  .bundle()
  .pipe plugins.plumber
    errorHandler: onError
  .pipe source 'app.js'
  .pipe gulp.dest './build'
  .pipe plugins.streamify plugins.uglify()
  .pipe plugins.rename 'app.min.js'
  .pipe gulp.dest './build'

gulp.task 'styles', ->
  # using libsass for foundation (compass)
  gulp.src './app/app.scss'
    .pipe plugins.plumber
      errorHandler: onError
    .pipe plugins.sass
      outputStyle: 'expanded'
      includePaths: [
        './app'
        './node_modules'
      ]
    .pipe plugins.autoprefixer 'last 2 versions'
    .pipe gulp.dest './build'
    .pipe plugins.size()
  return

gulp.task 'critical-css', ['styles'], ->
  penthouse
    url: URL
    css: './build/app.css'
    height: 640
    width: 480
  , (err, criticalCss) ->
    fs.writeFileSync './build/critical.css', criticalCss
    return

gulp.task 'templates', ->
  # combine all template files of the app into a js file
  gulp.src [
    '!./app/index.html'
    './app/**/*.html'
  ]
    .pipe plugins.angularTemplatecache 'templates.js',
      module: 'townhall.templates'
      standalone: true
    .pipe gulp.dest './app'
    .pipe plugins.size
      title: 'templates'

gulp.task 'index', ->
  gulp.src './app/index.html'
    .pipe gulp.dest './build'

gulp.task 'images', ->
  gulp.src './app/images/**/*.{jpg,jpeg,png,gif,svg}'
    .pipe gulp.dest './build'
    .pipe plugins.size()
  return

gulp.task 'watch', ->
  gulp.watch [
    './build/**/*.html'
    './build/**/*.js'
    './build/**/*.css'
  ]
    .on 'change', plugins.livereload.changed
  gulp.watch [
    './app/**/*.coffee'
    './app/**/*.js'
  ], ['browserify']
  gulp.watch './app/**/*.scss', ['critical-css']
  gulp.watch [
    '!./app/index.html'
    './app/**/*.html'
  ], ['templates']
  gulp.watch './app/images/**/*.{jpg,png,jpeg,gif}', ['images']
  gulp.watch './app/index.html', ['index']
  return

gulp.task 'livereload', ->
  plugins.livereload.listen()
  return

gulp.task 'default', [
  'livereload'
  'browserify'
  'templates'
  'critical-css'
  'index'
  'watch'
  'images'
]

gulp.task 'build', [
  'browserify'
  'templates'
  'critical-css'
  'index'
  'images'
]