'use client'
import 'src/app/globals.css'
import { useCallback, useEffect, useState } from 'react'
import { Sidebar } from 'flowbite-react'
import { IoHomeSharp, IoLockClosed, IoLockOpen, IoMap } from "react-icons/io5"
import { IconContext } from 'react-icons'
import { BASE_STATE, AREA_STATE } from 'src/app/utils/Constants'
import Error from "src/app/components/Error"
import LoadingMenu from "src/app/components/SidebarLoadingMenu"
import { SideBarTheme } from "src/app/utils/SideBarTheme"
import { PageObject, isTypeofWindow } from "src/app/utils/StorageObject"
import { useApiMenuInfo } from 'src/api/Api'

{/*
  機能名:サイドバーメニュー
*/}
export default function SidebarMenu(props) {

  {/* 状態用 */ }
  const [menuState, setMenuState] = useState(null)
  const [menuStateName, setMenuStateName] = useState(null)

  {/* マップ用 */ }
  const [areaState, setAreaState] = useState(null)

  {/* localStorageクリア */ }
  // localStorage.removeItem("pageInfo")

  useEffect(() => {
    if (isTypeofWindow) {
      const pageinfo = JSON.parse(localStorage.getItem("pageInfo"))
      // console.log(pageinfo?.state)
      setMenuState((pageinfo?.state === undefined ? BASE_STATE.ALL.CODE : pageinfo.state))
      setMenuStateName(pageinfo?.stateName)
      setAreaState(pageinfo?.area)
    }
  }, [menuState, areaState])

  {/* メニューのリンククリック時の処理 */ }
  const handleMenuLinkClick = useCallback((state, stateName, area) => {
    if (isTypeofWindow) {
      PageObject.currentPage = 1
      PageObject.state = state
      PageObject.stateName = stateName
      PageObject.area = area
      // console.log("state=" + state + ",area=" + area)
      if (state === BASE_STATE.NONE.CODE) {
        PageObject.state = BASE_STATE.ALL.CODE
        PageObject.stateName = BASE_STATE.ALL.NAME
      }
      if (area !== AREA_STATE.NONE) {
        PageObject.state = BASE_STATE.NONE.CODE
        PageObject.stateName = BASE_STATE.NONE.NAME
      }
      localStorage.setItem("pageInfo", JSON.stringify(PageObject))
    }
  }, [])

  {/* API実行 */ }
  const { data, error, isValidating } = useApiMenuInfo()

  {/* ローディング処理 */ }
  if (isValidating) return <LoadingMenu />
  if (error) return <Error />
  // console.log("menuState:" + menuState)

  return (
    <div>
      {/* モバイルでハンバガーメニュークリックした場合のみクリック可能とする */}
      <Sidebar className={`fixed top-20 left-0 z-20 w-64 h-screen
      ${props.menuOpen ? "-translate-x-full transition-transform sm:translate-x-0" : ""}`}
        theme={SideBarTheme}
      >
        <Sidebar.Items>
          <Sidebar.ItemGroup>
            {/* すべて */ }
            <IconContext.Provider value={{ className: `${(menuState !== BASE_STATE.ALL.CODE) ? "text-white" : ""}` }}>
              <Sidebar.Item
                href="/"
                icon={IoHomeSharp}
                className={`hover:bg-gray-800 hover:text-white ${(menuState === BASE_STATE.ALL.CODE) ? "bg-gray-50" : "text-white"}`}
                onClick={() => handleMenuLinkClick(
                  BASE_STATE.ALL.CODE,
                  BASE_STATE.ALL.NAME,
                  AREA_STATE.NONE)}
              >
                <p>
                  {BASE_STATE.ALL.NAME}
                  <span className="inline-flex items-center justify-center w-8 h-4 ml-4 text-xs font-semibold text-slate-700 bg-slate-300 rounded-full">
                    {data.all_count}{/* 件数 */ }
                  </span>
                </p>
              </Sidebar.Item>
            </IconContext.Provider>
            {/* 消灯 */ }
            <IconContext.Provider value={{ className: `${(menuState !== BASE_STATE.OPEN.CODE) ? "text-white" : ""}` }}>
              <Sidebar.Item
                href="/"
                icon={IoLockOpen}
                className={`hover:bg-gray-800 hover:text-white ${(menuState === BASE_STATE.OPEN.CODE) ? "bg-gray-50" : "text-white"}`}
                onClick={() => handleMenuLinkClick(
                  BASE_STATE.OPEN.CODE,
                  BASE_STATE.OPEN.NAME,
                  AREA_STATE.NONE)}
              >
                <p>
                  {BASE_STATE.OPEN.NAME}
                  <span className="inline-flex items-center justify-center w-8 h-4 ml-4 text-xs font-semibold bg-pink-100 text-pink-800 rounded-full">
                    {data.open_count}{/* 件数 */ }
                  </span>
                </p>
              </Sidebar.Item>
            </IconContext.Provider>
            {/* 全閉 */ }
            <IconContext.Provider value={{ className: `${(menuState !== BASE_STATE.CLOSE.CODE) ? "text-white" : ""}` }}>
              <Sidebar.Item
                href="/"
                icon={IoLockClosed}
                className={`hover:bg-gray-800 hover:text-white ${(menuState === BASE_STATE.CLOSE.CODE) ? "bg-gray-50" : "text-white"}`}
                onClick={() => handleMenuLinkClick(
                  BASE_STATE.CLOSE.CODE,
                  BASE_STATE.CLOSE.NAME,
                  AREA_STATE.NONE)}
              >
                <p>
                  {BASE_STATE.CLOSE.NAME}
                  <span className="inline-flex items-center justify-center w-8 h-4 ml-4 text-xs font-semibold text-gray-100 bg-gray-600 rounded-full">
                    {data.close_count}{/* 件数 */ }
                  </span>
                </p>
              </Sidebar.Item>
            </IconContext.Provider>
            <IconContext.Provider value={{ className: "text-white group-hover:text-white" }}>
              <Sidebar.Collapse
                open={true}
                icon={IoMap}
                label="マップ"
                className="text-white hover:bg-gray-800"
              >
                {Object.values(data.area).map((item) => {
                  return (
                    <Sidebar.Item
                      key={item.id}
                      href={`/areamap/${item.id}`}
                      className={`hover:bg-gray-800 hover:text-white ${(areaState === item.area_name) ? "bg-gray-50" : "text-white"}`}
                      onClick={() => handleMenuLinkClick(
                        menuState,
                        menuStateName,
                        item.area_name)}
                    >
                      {item.area_name}
                    </Sidebar.Item>
                  )
                })}
              </Sidebar.Collapse>
            </IconContext.Provider>
          </Sidebar.ItemGroup>
        </Sidebar.Items>
      </Sidebar>
    </div>
  )
}