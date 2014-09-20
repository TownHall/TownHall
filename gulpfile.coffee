gulp = require "gulp"
browserify = require "browserify"
shim = require "browserify-shim"
source = require "vinyl-source-stream"
plugins = require("gulp-load-plugins") lazy: false
penthouse = require "penthouse"
fs = require "fs"

onError = (err) ->
  plugins.util.beep()
  console.log err
  return

URL = "http://localhost:8080/project-template"
gulp.task "browserify", ->
  browserify "./scripts/main.coffee"
    .bundle()
    .pipe plugins.plumber
      errorHandler: onError
    .pipe source "main.js"
    .pipe gulp.dest "./scripts"
    .pipe plugins.streamify plugins.uglify()
    .pipe plugins.rename "main.min.js"
    .pipe gulp.dest "./scripts"

gulp.task "styles", ->
  # using libsass for foundation (compass)
  gulp.src "./styles/main.scss"
    .pipe plugins.plumber
      errorHandler: onError
    .pipe plugins.sass
      outputStyle: "expanded"
      includePaths: ["./styles"]
    .pipe plugins.autoprefixer "last 2 versions"
    .pipe gulp.dest "./styles"
    .pipe plugins.size()
  return

gulp.task "critical-css", ["styles"], ->
  penthouse
    url: URL
    css: "./styles/main.css"
    height: 640
    width: 480
  , (err, criticalCss) ->
    fs.writeFileSync "./styles/critical.css", criticalCss
    return


gulp.task "images", ->
  gulp.src "./images/uncompressed/**/*.{jpg,jpeg,png,gif,svg}"
    .pipe gulp.dest "./images"
    .pipe plugins.size()
  return

gulp.task "watch", ->
  gulp.watch [
    "./**/*.html"
    "./scripts/**/*.js"
    "./styles/**/*.css"
  ]
    .on "change", plugins.livereload.changed
  gulp.watch "./scripts/**/*.coffee", ["browserify"]
  gulp.watch "./styles/**/*.scss", ["critical-css"]
  gulp.watch "./images/uncompressed/**/*.{jpg,png,jpeg,gif}", ["images"]
  return

gulp.task "livereload", ->
  plugins.livereload.listen()
  return

gulp.task "default", [
  "livereload"
  "browserify"
  "critical-css"
  "watch"
  "images"
]

gulp.task "build", [
  "browserify"
  "critical-css"
  "images"
]