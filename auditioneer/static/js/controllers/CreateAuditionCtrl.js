/**
 * Created by Holl on 3/14/14.
 */


function CreateAuditionCtrl($scope, $http, $location) {

            $scope.map = {
                center: {
                    latitude: 41,
                    longitude: -73.75
                },
                zoom: 9
            };

    $http.get('/api/v1/tag/?format=json').
        success(function(tag){
            $scope.tags = tag.objects;
            console.log(tag)
        });

    $scope.submitForm = function(){

        $scope.audition.latitude = 0;
        $scope.audition.longitude = 0;
        $scope.audition.production_user_id = request.user;
        $http.post('/api/v1/audition/?format=json', $scope.audition).
            success(function(response){
                $location.path('/')
        })
    }
}