'use client'
import { Pagination } from 'flowbite-react'
import { useState, useCallback } from "react"
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

  // console.log("menuSelectedName:" + menuSelectedName)

  return (
    <main className="p-5 pt-20 mb-12 sm:ml-64 bg-body-color">
      <div className="container mx-auto text-center">
        <HashTag selectedName={menuSelectedName} />
        <table className="w-full text-sm text-left rtl:text-right text-gray-700">
          <thead className="text-gray-800 uppercase bg-gray-100">
            <tr>
              <th scope="col" className="px-6 py-3">
                扉番号
              </th>
              <th scope="col" className="px-6 py-3">
                ゲート状態
              </th>
              <th scope="col" className="px-6 py-3">
                電池残量
              </th>
              <th scope="col" className="px-6 py-3">
                通信状態
              </th>
            </tr>
          </thead>
          <tbody>
            {/* 一覧の件数分ループ */}
            {Object.values(data.products).map((item, index) => {
              return (
                <tr  key={item.id} className="bg-white border-b">
                  <th className="px-6 py-4 font-medium whitespace-nowrap">
                    12
                  </th>
                  <td className="px-6 py-4">
                    <div className={`bg-gray-100 text-gray-800 text-sm font-medium w-14 px-3 py-0.5 rounded-md font-semibold border border-stone-200
                                  ${(item.id % 2 === 0) ? "bg-gray-600 text-white" : "bg-pink-100 text-pink-800"}`}>
                      {(item.id % 2 === 0) ? BASE_STATE.CLOSE.NAME : BASE_STATE.OPEN.NAME}
                    </div>
                  </td>
                  <td className="px-6 py-4">
                    80%
                  </td>
                  <td className="px-6 py-4">
                    通信良好
                  </td>
                </tr>
              )
            })}
          </tbody>
        </table>
      </div>
      <div className="grid gap-1 md:grid-cols-2 p-2">
        <div className="text-sm py-2">
          <span className="bg-gray-100 text-gray-800 text-xs font-medium mr-2 px-2.5 py-0.5 rounded border border-gray-300">
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
