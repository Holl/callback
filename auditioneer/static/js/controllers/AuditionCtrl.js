/**
 * Created by Holl on 3/14/14.
 */

function AuditionCtrl($scope, $http, $routeParams) {
    var id = $routeParams.id;

    $http({method: 'POST', url: '/callback/auditioneer/views.py'}).
      success(function(data){
            console.log(data);
          $scope.user_data = data;
      });


    $http.get('/api/v1/audition/'+id+'/?format=json').
        success(function(audition){
            $scope.audition = audition;
            console.log(audition);

            console.log(audition.parts);


        });




}