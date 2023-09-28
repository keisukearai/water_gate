'use client'
import { useParams } from "next/navigation"
import Image from "next/image"
import { isMobile } from "react-device-detect"
import { Loading } from "src/app/components/Loading"
import Error from "src/app/components/Error"
import MapGoogle from "src/app/components/GoogleMap"
import { BASE_STATE } from 'src/app/utils/Constants'
import { useApiContenDatail } from "src/api/Api"

{/*
  機能名:内容詳細
*/}
export default function ContentDetail() {

  {/* 画像パス */}
  const media_path = process.env.NEXT_PUBLIC_API_MEDIA_PATH

  {/* リクエストパラメータ取得 */}
  const params = useParams()

  {/* API実行 */}
  const { data, error, isValidating } = useApiContenDatail(params.slug)
  // console.log(`data=${data}, error=${error}, isValidating=${isValidating}`)
  // console.log(data)

  {/* ローディング処理 */}
  if (isValidating) return <Loading />
  if (error) return <Error />

  {/* 画像loader設定 */}
  const imgLoader = () => {
    return isMobile ? `${media_path}${data.data.water_gate_image_sm}` : `${media_path}${data.data.water_gate_image}`
  }

  return (
    <main className="p-5 pt-16 mb-6 sm:ml-64">
      <div className="bg-white py-6 sm:py-4 lg:py-4">
        <div className="mx-auto max-w-screen-lg p-4 md:p-8">
          <div className="grid gap-4 md:grid-cols-2">
            <div className="md:pb-8">
              <div className="mb-4 md:mb-6">
                <span className="mb-0.5 inline-block text-gray-500 font-bold">
                  安芸津
                </span>
                <h2 className="text-2xl font-bold text-gray-800 lg:text-3xl">
                  {data.data.water_gate_name}
                </h2>
              </div>
              <div className="mb-4 md:mb-6">
                <span className="mb-3 inline-block text-sm font-semibold text-gray-500 md:text-base">
                  状態
                </span>
                <div className="flex flex-wrap gap-2">
                  <span className={`mr-2 px-3 py-1 rounded-md shadow-md text-lg font-bold border border-stone-200
                        ${(data.id % 2 === 0) ? "bg-gray-600 text-white" : "bg-pink-100 text-pink-800"}`}
                  >
                    {(data.id % 2 === 0) ? BASE_STATE.CLOSE.NAME : BASE_STATE.OPEN.NAME}
                  </span>
                </div>
              </div>
              <div className="mb-4 md:mb-6">
                <span className="mb-3 inline-block text-sm font-semibold text-gray-500 md:text-base">
                  バッテリー残量
                </span>
                <div className="flex flex-wrap gap-3">
                  <div className="w-8/12 bg-gray-200 rounded-xl">
                    <div className="bg-teal-600 text-base font-medium text-teal-100 text-center p-1 leading-none rounded-xl"
                      style={{ width: (35 >= 100 ? 100 : 35) + '%' }}>{(35 >= 100 ? 100 : 35)}%
                    </div>
                  </div>
                </div>
              </div>
              <div className="mb-4 md:mb-6">
                <span className="mb-3 inline-block text-sm font-semibold text-gray-500 md:text-base">
                  住所
                </span>
                <div className="flex flex-wrap gap-3">
                  { data.data.water_gateaddress }
                </div>
              </div>
              <div className="mb-4 md:mb-6">
                <span className="mb-3 inline-block text-sm font-semibold text-gray-500 md:text-base">
                  更新日
                </span>
                <div className="flex flex-wrap gap-3">
                  2023/09/27 12:34:56
                </div>
              </div>
              <div className="mb-4 md:mb-6">
                <div className="mb-3 inline-block text-sm font-semibold text-gray-500 md:text-base">
                  補足
                </div>
                <p className="whitespace-pre-wrap">
                  {data.data.water_gate_supplement}
                </p>
              </div>
            </div>
            <div className="space-y-4 z-5">
              {/* メイン画像 */}
              <div className="rounded-md shadow-md border-2 border-dark-500">
                <Image
                  loader={imgLoader}
                  src={(data.data.water_gate_image !== '') ? isMobile ? `${media_path}${data.data.water_gate_image_sm}` : `${media_path}${data.data.water_gate_image}` : '/no_image.webp'}
                  alt={data.data.water_gate_name}
                  width={500}
                  height={400}
                  priority={true}
                  loading={"eager"}
                  quality={isMobile ? 10 : 100}
                  unoptimized
                />
              </div>
              <div className="z-5 relative w-full h-80 rounded-md shadow-md border-2 border-dark-500">
                <MapGoogle lat={data.data.water_gate_latitude} lng={data.data.water_gate_longitude} />
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  )
}
