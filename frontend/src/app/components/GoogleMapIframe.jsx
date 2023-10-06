import Image from "next/image"
import { isMobile } from "react-device-detect"

{/*
  機能名:GoogelMap Iframe用
*/}
const GoogleMapIframe = (props) => {

  return (
    <div>
      {props.water_gate_map_url ? (
        <iframe
          src={props.water_gate_map_url}
          width="100%"
          className="aspect-square"
        >
        </iframe>
      ) : (
        <Image
          src="/no_map.webp"
          alt="地図なし"
          width={500}
          height={400}
          priority={true}
          quality={isMobile ? 50 : 70}
        />
      )}
    </div>
  )
}

export default GoogleMapIframe