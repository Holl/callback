/**
 * Created by Holl on 3/13/14.
 */
function MapCtrl($scope, $http) {
            $scope.map = {
                center: {
                    latitude: 40.74,
                    longitude: -73.95
                },
                zoom: 11
            };

    $http.get('/api/v1/audition/?format=json').
        success(function(points){
            console.log(points.objects)
            $scope.markers = points.objects
        });

}

