const places = JSON.parse(document.getElementById('places').textContent);

ymaps.ready(map_init);
function map_init() {
    var myMap = new ymaps.Map("map", {
        center: [0, 0],
        zoom: 12
    });
    var centerLat = 0,
        centerLong = 0;
    for (let i = 0; i < places.length; i++) {
        let cords = places[i].coordinates.split(' ').map(Number);;
        // calculate center between points
        centerLat += cords[0];
        centerLong += cords[1];
        // add points on map
        myMap.geoObjects
        .add(new ymaps.Placemark(cords, {
            balloonContent: places[i].categories,
            iconCaption: places[i].name
        }, {
            preset: 'islands#greenDotIconWithCaption'
        }));
    }
    myMap.setCenter([centerLat/places.length, centerLong/places.length]);
}
