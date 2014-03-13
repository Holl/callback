/**
 * Created by Holl on 3/12/14.
 */

var auditioneer = angular.module('auditioneer', ['ngRoute']);

auditioneer.config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when('/', {templateUrl: '/static/views/audition.html', controller: AuditionCtrl})
}])
