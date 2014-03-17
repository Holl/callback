/**
 * Created by Holl on 3/12/14.
 */

var auditioneer = angular.module('auditioneer', ['ngRoute', 'google-maps']);

auditioneer.config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when('/', {templateUrl: '/static/views/map.html', controller: MapCtrl}).
        when('/create', {templateUrl: '/static/views/create.html', controller: CreateAuditionCtrl}).
        when('/profile/:id', {templateUrl: '/static/views/profile.html', controller: ProfileCtrl}).
        when('/:id', {templateUrl: '/static/views/audition.html', controller: AuditionCtrl})
}])
