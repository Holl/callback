/**
 * Created by Holl on 3/14/14.
 */

function ProfileCtrl($scope, $http, $routeParams) {
    var id = $routeParams.id;
    $http.get('/api/v1/actor_profile/'+id+'/?format=json').
        success(function(actor){
            $scope.actor = actor;
            console.log(actor);
            $scope.HighlightVideo = "http://127.0.0.1:8000" + actor.highlight_reel;

        });



}