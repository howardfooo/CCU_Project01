mapboxgl.accessToken = 'pk.eyJ1IjoieW91c2hhbjc3IiwiYSI6ImNsdDdldDZoMzBseHoyanAzdXR5bGJmb2QifQ.vf_7WHFQFyRU60FiEMAW1Q'; 
const map = new mapboxgl.Map
({
  container: 'map',
  style: 'mapbox://styles/youshan77/clt7g9oro00h601ragj0n316g/draft',
  center: [120.47160374920969, 23.55617040204181], 
  zoom: 15.5,
  attributionControl: false,
});

map.addControl(new mapboxgl.NavigationControl());
map.addControl(new mapboxgl.GeolocateControl
({
  positionOptions:
  {
    enableHighAccuracy: true
  },
  trackUserLocation: true,
  showUserHeading: true
}));

const marker = new mapboxgl.Marker
({
  color: 'red',
  // draggable: true
})
  .setLngLat([120.47160374920969, 23.55617040204181])
  .setPopup(new mapboxgl.Popup().setHTML("<h1>~我的位置~</h1>"))
  .addTo(map);



map.on('load', ()=>{
  map.setLanguage('zh-Hant');
});

