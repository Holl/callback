/**
 * Created by Holl on 3/13/14.
 */
function MapCtrl($scope, $http) {
            $scope.map = {
                center: {
                    latitude: 41,
                    longitude: -73.75
                },
                zoom: 9
            };

    $http.get('/api/v1/audition/?format=json').
        success(function(points){
            $scope.markers = points.objects
        });

}

