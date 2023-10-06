{/*
  機能名:GoogelMap Iframe用
*/}
const GoogleMapIframe = (props) => {

  return (
    <div>
      <iframe
        src={ props.water_gate_map_url }
        width="100%"
        className="aspect-square"
      >
      </iframe>
    </div>
  )
}

export default GoogleMapIframe