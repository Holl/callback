/**
 * Created by Holl on 3/14/14.
 */

function AuditionCtrl($scope, $http, $routeParams) {
    var id = $routeParams.id;



    $http.get('/api/v1/audition/'+id+'/?format=json').
        success(function(audition){
            $scope.audition = audition;
            console.log(audition);

            console.log(audition.parts);

            $('#applyButton').click(function()
            {
                audition.actor.append(username);
                console.log("Apply Button Clicked!");

                console.log("going out:");
                console.log(audition);

                $http.post('/api/v1/audition/'+id+'/?format=json', audition).
                    success(function(audition){
                        $location.path('/')

                    })
            });
        });





}