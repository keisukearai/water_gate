'use client'
import { useState } from "react"
import { useParams } from "next/navigation"
import Image from "next/image"
import { Loading } from "src/app/components/Loading"
import Error from "src/app/components/Error"
import { isMobile } from "react-device-detect"
import { useAreaInfo } from 'src/api/Api'
import { HashTag } from "src/app/components/HashTag"

{/*
  機能名:AreaMap
*/}
export default function AreaMap() {
  {/* 画像パス */ }
  const media_path = process.env.NEXT_PUBLIC_API_MEDIA_PATH

  {/* マップ用 */ }
  const [areaSelectedName, setAreaSelectedName] = useState(
    (typeof window !== 'undefined') ? (JSON.parse(localStorage.getItem("pageInfo"))?.area == null) ? '' : JSON.parse(localStorage.getItem("pageInfo")).area : ''
  )

  {/* リクエストパラメータ取得 */ }
  const params = useParams()

  {/* API実行 */ }
  const { data, error, isValidating } = useAreaInfo(params.slug)

  {/* ローディング処理 */ }
  if (isValidating) return <Loading />
  if (error) return <Error />

  {/* 画像loader設定 */ }
  const imgLoader = () => {
    return (data.data[0].water_gate_map !== '') ? isMobile ? `${media_path}${data.data[0].water_gate_map_sm}` : `${media_path}${data.data[0].water_gate_map}` : '/no_image.webp'
  }

  return (
    <main className="p-5 pt-20 mb-12 sm:ml-64 bg-body-color">
      <div className="container mx-auto text-center">
        <HashTag selectedName='安芸津' />
        <Image
          loader={imgLoader}
          src={(data.data[0].water_gate_map !== '') ? isMobile ? `${media_path}${data.data[0].water_gate_map_sm}` : `${media_path}${data.data[0].water_gate_map}` : '/no_image.webp'}
          alt={data.data[0].area_name}
          width={(data.data[0].water_gate_map !== '') ? isMobile ? 300 : 900 : 500}
          height={(data.data[0].water_gate_map !== '') ? isMobile ? 240 : 720 : 400}
          priority={true}
          className="z-10 relative hover:opacity-75 border border-gray-200"
          quality={isMobile ? 50 : 70}
          unoptimized
        />
      </div>
    </main>
  )
}