var places

ymaps.ready(map_init);
function map_init() {
    var myMap = new ymaps.Map("map", {
        center: places[places.length-1], //set a pre-calculated center
        zoom: 12
    });
    for (let i = 0; i < places.length-1; i++) {
        // add points on map
        myMap.geoObjects
        .add(new ymaps.Placemark(places[i][3], {
            balloonContent: places[i][1],
            iconCaption: places[i][0]
        }, {
            preset: 'islands#greenDotIconWithCaption'
        }));
    }
}
