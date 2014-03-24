/**
 * Created by Holl on 3/14/14.
 */

function AuditionCtrl($scope, $http, $routeParams) {
    var id = $routeParams.id;



    $http.get('/api/v1/audition/'+id+'/?format=json').
        success(function(audition){
            $scope.audition = audition;
            console.log(audition);
            $scope.user = username;

            console.log(audition.parts);

                $('.apply-buttons').click(function(){


                })
            });






}