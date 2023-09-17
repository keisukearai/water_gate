import { Map, GoogleApiWrapper, Marker } from "google-maps-react"

{/*
  機能名:GoogelMap
*/}
const GoogleMap = (props) => {

  {/* MAPのポジション設定 */}
  const position =
  {
    lat: `${props.lat}`,
    lng: `${props.lng}`
  }

  return (
    <div>
      <Map
        google={window.google}
        zoom={17}
        className="absolute top-0 left-0 w-full h-full"
        initialCenter={position}
      >
        <Marker
          position={position}
        />
      </Map>
    </div>
  )
}

export default GoogleApiWrapper({
  // GOOGLE MAP API KEY
  apiKey: process.env.NEXT_PUBLIC_GOOGLE_MAP_API_KEY
})(GoogleMap);