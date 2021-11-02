var places

ymaps.ready(map_init);
function map_init() {
    var myMap = new ymaps.Map("map", {
        center: [0, 0],
        zoom: 12
    });
    var centerLat = 0,
        centerLong = 0;
    for (let i = 0; i < places.length; i++) {
        // calculate center between points
        centerLat += places[i][3][0];
        centerLong += places[i][3][1];
        // add points on map
        myMap.geoObjects
        .add(new ymaps.Placemark(places[i][3], {
            balloonContent: places[i][1],
            iconCaption: places[i][0]
        }, {
            preset: 'islands#greenDotIconWithCaption'
        }));
    }
    myMap.setCenter([centerLat/places.length, centerLong/places.length]);
}
