/**
 * Created by Holl on 3/13/14.
 */
function AuditionCtrl($scope, $http) {
            $scope.map = {
                center: {
                    latitude: 41,
                    longitude: -73.75
                },
                zoom: 9
            };

    $http.get('/api/v1/audition/?format=json').
        success(function(points){
            console.log("The following is points:")
            console.log(points.objects)
        });

            $scope.searchLocationMarker = {
                coords: {
                    latitude: 40.1451,
                    longitude: -99.6680
                },
            };

        }