'use client'
import { useParams } from "next/navigation"
import Image from "next/image"
import { isMobile } from "react-device-detect"
import { Loading } from "src/app/components/Loading"
import Error from "src/app/components/Error"
import MapGoogle from "src/app/components/GoogleMap"
import { useApiContenDatail } from "src/api/Api"

{/*
  機能名:内容詳細
*/}
export default function ContentDetail() {

  {/* リクエストパラメータ取得 */}
  const params = useParams()

  {/* API実行 */}
  const { data, error, isValidating } = useApiContenDatail(params.slug)
  // console.log(`data=${data}, error=${error}, isValidating=${isValidating}`)

  {/* ローディング処理 */}
  if (isValidating) return <Loading />
  if (error) return <Error />

  return (
    <main className="p-5 pt-16 mb-12 sm:ml-64">
      <div className="bg-white py-6 sm:py-4 lg:py-4">
        <div className="mx-auto max-w-screen-lg p-4 md:p-8">
          <div className="grid gap-4 md:grid-cols-2">
            <div className="md:pb-8">
              <div className="mb-4 md:mb-6">
                <span className="mb-0.5 inline-block text-gray-500 font-bold">
                  安芸津
                </span>
                <h2 className="text-2xl font-bold text-gray-800 lg:text-3xl">
                  サンプルサンプル水門{data.id}
                </h2>
              </div>
              <div className="mb-4 md:mb-6">
                <span className="mb-3 inline-block text-sm font-semibold text-gray-500 md:text-base">
                  状態
                </span>
                <div className="flex flex-wrap gap-2">
                  <span className={`mr-2 px-3 py-1 rounded shadow-md text-lg font-bold
                        ${(data.id % 2 === 0) ? "bg-gray-600 text-white" : "bg-pink-100 text-pink-800"}`}
                  >
                    {(data.id % 2 === 0) ? '閉' : '開'}
                  </span>
                </div>
              </div>
              <div className="mb-4 md:mb-6">
                <span className="mb-3 inline-block text-sm font-semibold text-gray-500 md:text-base">
                  バッテリー容量
                </span>
                <div className="flex flex-wrap gap-3">
                  <div className="w-full bg-gray-200 rounded-full dark:bg-gray-700">
                    <div className="bg-sky-600 text-lg font-medium text-blue-100 text-center p-2 leading-none rounded-full"
                      style={{ width: (data.stock >= 100 ? 100 : data.stock) + '%' }}>{(data.stock >= 100 ? 100 : data.stock)}%
                    </div>
                  </div>
                </div>
              </div>
              <div className="mb-4 md:mb-6">
                <span className="mb-3 inline-block text-sm font-semibold text-gray-500 md:text-base">
                  住所
                </span>
                <div className="flex flex-wrap gap-3">
                  東広島市安芸津1234-5678
                </div>
              </div>
              <div className="mb-4 md:mb-6">
                <span className="mb-3 inline-block text-sm font-semibold text-gray-500 md:text-base">
                  更新日
                </span>
                <div className="flex flex-wrap gap-3">
                  2023/10/10 10:10:10
                </div>
              </div>
              <div className="mb-4 md:mb-6">
                <div className="mb-3 inline-block text-sm font-semibold text-gray-500 md:text-base">
                  補足
                </div>
                <p>
                  あいうえおあいうえおあいうえおあいうえおあいうえお
                  かきくけこかきくけこかきくけこかきくけこかきくけこ
                  さしすせそさしすせそさしすせそさしすせそさしすせそ
                  たちつてとたちつてとたちつてとたちつてとたちつてと
                  なにぬねのなにぬねのなにぬねのなにぬねのなにぬねの
                </p>
              </div>
            </div>
            <div className="space-y-4 z-5">
              {/* メイン画像 */}
              <div className="rounded-lg border-4 border-dark-500">
                <Image
                  src="/sample.jpg"
                  alt="Vercel Logo"
                  className="dark:invert"
                  width={500}
                  height={500}
                  priority={true}
                  loading={"eager"}
                  quality={isMobile ? 10 : 100}
                />
              </div>
              <div className="z-5 relative w-full h-80 border-4 border-dark-500 rounded-lg">
                <MapGoogle lat="34.322113346548036" lng="132.8181288949294" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  )
}
