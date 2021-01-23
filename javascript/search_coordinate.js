var mapContainer = document.getElementById('map'), // 지도를 표시할 div
    mapOption = {
        center: new kakao
            .maps
            .LatLng(37.566826, 126.9786567), // 지도의 중심좌표
        level: 3 // 지도의 확대 레벨
    };

var map = new kakao
    .maps
    .Map(mapContainer, mapOption); // 지도를 생성합니다

function setCenter() {
    // 이동할 위도 경도 위치를 생성합니다
    var moveLatLon = new kakao
        .maps
        .LatLng(33.452613, 126.570888);

    // 지도 중심을 이동 시킵니다
    map.setCenter(moveLatLon);
}

function panToCoordinate() {

    try {

        var input_latitude = document
            .getElementById('input_latitude')
            .value;
        var input_longitude = document
            .getElementById('input_longitude')
            .value;

        // 이동할 위도 경도 위치를 생성합니다
        var moveLatLon = new kakao
            .maps
            .LatLng(input_latitude, input_longitude);

        // 지도 중심을 부드럽게 이동시킵니다 만약 이동할 거리가 지도 화면보다 크면 부드러운 효과 없이 이동합니다
        map.panTo(moveLatLon);

        // // 마커를 생성합니다
        // var marker = new kakao
        //     .maps
        //     .Marker({position: moveLatLon}); //    마커가 지도 위에 표시되도록 설정합니다
        // marker.setMap(map); //툴팁을 노출하는 마커를 생성합니다.



        var iwContent = '<div style="padding:5px;">위도: ' + input_latitude + '</div><div' +
        ' style="padding:5px;">경도: ' + input_longitude + '</div>', // 인포윈도우에 표출될 내용으로 HTML 문자열이나 document element가 가능합니다
iwRemoveable = true; // removeable 속성을 ture 로 설정하면 인포윈도우를 닫을 수 있는 x버튼이 표시됩니다

// 인포윈도우를 생성하고 지도에 표시합니다
var infowindow = new kakao
.maps
.InfoWindow({
    map: map, // 인포윈도우가 표시될 지도
    position: moveLatLon,
    content: iwContent,
    removable: iwRemoveable
});

}


    } catch (e) {
        alert("입력하신 좌표를 찾을 수 없습니다.\n정확한 좌표를 입력해주세요~\n국내 좌표만 검색이 가능합니다.");
    }

  
