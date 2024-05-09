map.on('mouseenter', '1', function(e)
{
    showPopup(e.features[0]);
});

function showPopup(feature)
{
    new mapboxgl.Popup()
        .setLngLat(feature.geometry.coordinates)
        .setHTML('<h3>' + feature.properties.title + '</h3><p>' + feature.properties.description + '</p>')
        .addTo(map);
}