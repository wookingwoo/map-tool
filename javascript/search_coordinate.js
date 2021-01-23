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

//        // 마커를 생성합니다
//        var marker = new kakao
//        .maps
//        .Marker({position: moveLatLon});

//    // 마커가 지도 위에 표시되도록 설정합니다
//    marker.setMap(map);

   // 커스텀 오버레이에 표시할 내용입니다 HTML 문자열 또는 Dom Element 입니다
   var content = '<div class="overlay_info">';
   content += '    <a href="https://place.map.kakao.com/17600274" target="_blank"><strong>월정리' +
           ' 해수욕장</strong></a>';
   content += '    <div class="desc">';
   content += '        <img src="https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/pla' +
           'ce_thumb.png" alt="">';
   content += '        <span class="address">제주특별자치도 제주시 구좌읍 월정리 33-3</span>';
   content += '    </div>';
   content += '</div>';

   // 커스텀 오버레이를 생성합니다
   var mapCustomOverlay = new kakao
       .maps
       .CustomOverlay({
           position: moveLatLon, content: content, xAnchor: 0.5, // 커스텀 오버레이의 x축 위치입니다. 1에 가까울수록 왼쪽에 위치합니다. 기본값은 0.5 입니다
           yAnchor: 1.1 // 커스텀 오버레이의 y축 위치입니다. 1에 가까울수록 위쪽에 위치합니다. 기본값은 0.5 입니다
       });

   // 커스텀 오버레이를 지도에 표시합니다
   mapCustomOverlay.setMap(map);



    
    } catch (e) {
        alert("입력하신 좌표를 찾을 수 없습니다.\n정확한 좌표를 입력해주세요~\n국내 좌표만 검색이 가능합니다.");
    }



 

}
