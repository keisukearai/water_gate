'use client'
import Link from "next/link"
import Image from "next/image"
import { Pagination } from 'flowbite-react'
import { useState, useCallback } from "react"
import { isMobile } from "react-device-detect"
import { Loading } from "src/app/components/Loading"
import Error from "src/app/components/Error"
import { paginationTheme } from "src/app/utils/PaginationTheme"
import { isTypeofWindow } from "src/app/utils/StorageObject"
import { BASE_STATE } from 'src/app/utils/Constants'
import { HashTag } from "src/app/components/HashTag"
import { useApiContenList } from "src/api/Api"

{/*
  機能名:内容一覧
*/}
export default function ContentList() {

  {/* ページネーション用 */ }
  const [currentPage, setCurrentPage] = useState(
    (typeof window !== 'undefined') ? (JSON.parse(localStorage.getItem("pageInfo"))?.currentPage == null) ? 1 : Number(JSON.parse(localStorage.getItem("pageInfo")).currentPage) : 1
  )
  {/* 状態用 */ }
  const [menuSelectedName, setMenuSelectedName] = useState(
    (typeof window !== 'undefined') ? (JSON.parse(localStorage.getItem("pageInfo"))?.stateName == null) ? BASE_STATE.ALL.NAME : JSON.parse(localStorage.getItem("pageInfo")).stateName : ''
  )

  {/* 地域用 */ }
  const [areaSelectedName, setAreaSelectedName] = useState(
    (typeof window !== 'undefined') ? (JSON.parse(localStorage.getItem("pageInfo"))?.areaName == null) ? '' : JSON.parse(localStorage.getItem("pageInfo")).areaName : ''
  )

  {/* ページネーションリンククリック処理 */ }
  const handlePageChange = useCallback((page) => {
    // console.log("page change:" + page)
    setCurrentPage(page)
    if (isTypeofWindow) {
      const pageinfo = JSON.parse(localStorage.getItem("pageInfo"))
      pageinfo.currentPage = page
      localStorage.setItem("pageInfo", JSON.stringify(pageinfo))
    }
  }, [])

  {/* API実行 */ }
  const { data, error, isValidating } = useApiContenList(currentPage)
  // console.log(`data=${data}, error=${error}, isValidating=${isValidating}`)

  {/* ローディング処理 */ }
  if (isValidating) return <Loading />
  if (error) return <Error />

  // console.log("areaSelectedName:" + areaSelectedName)

  return (
    <main className="p-5 pt-20 mb-12 sm:ml-64">
      <HashTag menuSelectedName={menuSelectedName} areaSelectedName={areaSelectedName} />
      <div className="container mx-auto text-center">
        <div className="-mx-4 flex flex-wrap">
          {/* 一覧の件数分ループ */}
          {Object.values(data.products).map((item, index) => {
            return (
              <div key={item.id} className="p-1.5 md:p-3 w-1/2 md:w-1/3 lg:w-1/5">
                <div className="max-w-sm bg-white border border-gray-200 rounded-md shadow dark:bg-gray-800 dark:border-gray-700">
                  <Link href={`detail/${item.id}`} rel="preload">
                    <Image
                      src="/sample.jpg"
                      alt="水門画像"
                      width={400}
                      height={400}
                      priority={true}
                      loading={"eager"}
                      className="hover:opacity-80"
                      quality={isMobile ? 5 : 50}
                    />
                  </Link>
                  <div className="p-5 text-left">
                    <div className="mb-0.5 inline-block text-gray-500 text-sm font-bold">
                      安芸津
                      <span className={`bg-gray-100 text-gray-800 text-xs font-medium ml-5 px-2.5 py-0.5 rounded-md font-semibold border border-stone-200
                                    ${(item.id % 2 === 0) ? "bg-gray-600 text-white" : "bg-pink-100 text-pink-800"}`}>
                        {(item.id % 2 === 0) ? BASE_STATE.CLOSE.NAME : BASE_STATE.OPEN.NAME}
                      </span>
                    </div>
                    <h5 className="mb-1 md:text-lg font-bold tracking-tight text-gray-900 dark:text-white">
                      サンプルサンプル{(item.id % 2 === 0) ? "サンプルサンプル" : ""}水門{item.id}
                    </h5>
                    <div className="text-xs mb-1">
                      バッテリー容量
                    </div>
                    <div className="w-full bg-gray-200 rounded-xl dark:bg-gray-700">
                      <div className="bg-teal-600 text-xs font-medium text-teal-100 text-center p-0.5 leading-none rounded-xl"
                        style={{ width: (item.stock >= 100 ? 100 : item.stock) + '%' }}>
                        {(item.stock >= 100 ? 100 : item.stock)}%
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            )
          })}
        </div>
      </div>
      <div className="grid gap-1 md:grid-cols-2 p-2">
        <div className="text-sm py-2">
          <span className="bg-gray-100 text-gray-800 text-xs font-medium mr-2 px-2.5 py-0.5 rounded dark:bg-gray-700 dark:text-gray-400 border border-gray-300">
            全100件
          </span>
        </div>
        <div className="text-right">
          {/* ページネーション */}
          <Pagination
            layout="pagination"
            previousLabel="<"
            nextLabel=">"
            currentPage={currentPage}
            onPageChange={handlePageChange}
            totalPages={10}
            theme={paginationTheme}
          />
        </div>
      </div>
    </main>
  )
}
