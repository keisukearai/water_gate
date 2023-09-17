'use client'
import 'src/app/globals.css'
import { useCallback, useEffect, useState } from 'react'
import { Sidebar } from 'flowbite-react'
import { IoHomeSharp, IoLockClosed, IoLockOpenOutline, IoAlbumsSharp } from "react-icons/io5"
import { BASE_STATE, AREA_STATE } from 'src/app/utils/Constants'
import Error from "src/app/components/Error"
import { PageObject, isTypeofWindow } from "src/app/utils/StorageObject"
import { useAreaInfo } from 'src/api/Api'

{/*
  機能名:サイドバーメニュー
*/}
export default function SidebarMenu({ handleMenuOpen, menuOpen }) {

  {/* 状態用 */ }
  const [menuState, setMenuState] = useState(null)
  const [menuStateName, setMenuStateName] = useState(null)

  {/* 地域用 */ }
  const [areaState, setAreaState] = useState(null)
  const [areaStateName, setAreaStateName] = useState(null)

  {/* localStorageクリア */ }
  // localStorage.removeItem("pageInfo")

  useEffect(() => {
    if (isTypeofWindow) {
      const pageinfo = JSON.parse(localStorage.getItem("pageInfo"))
      // console.log(pageinfo?.state)
      setMenuState((pageinfo?.state === undefined ? BASE_STATE.ALL.CODE : pageinfo.state))
      setMenuStateName(pageinfo?.stateName)
      setAreaState(pageinfo?.area)
      setAreaStateName(pageinfo?.areaName)
    }
  }, [menuState, areaState])

  {/* メニューのリンククリック時の処理 */ }
  const handleMenuLinkClick = useCallback((state, stateName, area, areaName) => {
    if (isTypeofWindow) {
      PageObject.currentPage = 1
      PageObject.state = state
      PageObject.stateName = stateName
      PageObject.area = area
      PageObject.areaName = areaName
      // console.log("state=" + state + ",area=" + area)
      if (state === BASE_STATE.ALL.CODE && area !== AREA_STATE.NONE) {
        PageObject.state = BASE_STATE.NONE.CODE
        PageObject.stateName = BASE_STATE.NONE.NAME
      }
      localStorage.setItem("pageInfo", JSON.stringify(PageObject))
    }
  },[])

  {/* API実行 */ }
  const { data, error, isValidating } = useAreaInfo()

  {/* ローディング処理 */ }
  if (isValidating) return <LoadingMenu />
  if (error) return <Error />

  return (
    <div>
      {/* モバイルでハンバガーメニュークリックした場合のみクリック可能とする */}
      <Sidebar className={`fixed top-20 left-0 z-10 w-64 h-screen
      ${menuOpen ? "-translate-x-full transition-transform sm:translate-x-0" : ""}`}
        onClick={() => !menuOpen ? handleMenuOpen() : ""}
      >
        <Sidebar.Items>
          <Sidebar.ItemGroup>
            <Sidebar.Item
              href="/"
              icon={IoHomeSharp}
              className={`${(menuState === BASE_STATE.ALL.CODE) ? "bg-gray-200" : ""}`}
              onClick={() => handleMenuLinkClick(
                BASE_STATE.ALL.CODE,
                BASE_STATE.ALL.NAME,
                AREA_STATE.NONE,
                AREA_STATE.NAME)}
            >
              <p>
                {BASE_STATE.ALL.NAME}
                <span className="inline-flex items-center justify-center w-8 h-4 ml-4 text-xs font-semibold text-slate-700 bg-slate-300 rounded-full">
                  99
                </span>
              </p>
            </Sidebar.Item>
            <Sidebar.Item
              href="/"
              icon={IoLockOpenOutline}
              className={`${(menuState === BASE_STATE.OPEN.CODE) ? "bg-gray-200" : ""}`}
              onClick={() => handleMenuLinkClick(
                BASE_STATE.OPEN.CODE,
                BASE_STATE.OPEN.NAME,
                areaState,
                areaStateName)}
            >
              <p>
                {BASE_STATE.OPEN.NAME}
                <span className="inline-flex items-center justify-center w-8 h-4 ml-4 text-xs font-semibold bg-pink-100 text-pink-800 rounded-full">
                  19
                </span>
              </p>
            </Sidebar.Item>
            <Sidebar.Item
              href="/"
              icon={IoLockClosed}
              className={`${(menuState === BASE_STATE.CLOSE.CODE) ? "bg-gray-200" : ""}`}
              onClick={() => handleMenuLinkClick(
                BASE_STATE.CLOSE.CODE,
                BASE_STATE.CLOSE.NAME,
                areaState,
                areaStateName)}
            >
              <p>
                {BASE_STATE.CLOSE.NAME}
                <span className="inline-flex items-center justify-center w-8 h-4 ml-4 text-xs font-semibold text-gray-100 bg-gray-600 rounded-full">
                  80
                </span>
              </p>
            </Sidebar.Item>
            <Sidebar.Collapse
              open={true}
              icon={IoAlbumsSharp}
              label="地域"
            >
              {Object.values(data.data).map((item) => {
                return (
                  <Sidebar.Item
                    key={item.id}
                    href={`/?area=${item.areaName}`}
                    className={`${(areaState === item.area_name) ? "bg-gray-200" : ""}`}
                    onClick={() => handleMenuLinkClick(
                      menuState,
                      menuStateName,
                      item.area_name,
                      item.area_name)}
                  >
                    {item.area_name}
                    <span className="inline-flex items-center justify-center w-8 h-4 ml-4 text-xs font-semibold text-slate-700 bg-slate-300 rounded-full">
                      {item.area_count}
                    </span>
                  </Sidebar.Item>
                )
              })}
            </Sidebar.Collapse>
          </Sidebar.ItemGroup>
        </Sidebar.Items>
      </Sidebar>
    </div>
  )
}

{/*
  機能名:ローディング中のメニュー
*/}
function LoadingMenu() {
  return (
    <div>
      <Sidebar className="fixed top-20 left-0 z-10 w-64 h-screen">
        <Sidebar.Items>
          <Sidebar.ItemGroup>
            <Sidebar.Item
              icon={IoHomeSharp}
            >
              <p>
                {BASE_STATE.ALL.NAME}
                <span className="inline-flex items-center justify-center w-8 h-4 ml-6 text-xs font-semibold text-slate-700 bg-slate-300 rounded-full">
                  -
                </span>
              </p>
            </Sidebar.Item>
            <Sidebar.Item
              icon={IoLockOpenOutline}
            >
              <p>
                {BASE_STATE.OPEN.NAME}
                <span className="inline-flex items-center justify-center w-8 h-4 ml-4 text-xs font-semibold bg-pink-100 text-pink-800 rounded-full">
                  -
                </span>
              </p>
            </Sidebar.Item>
            <Sidebar.Item
              icon={IoLockClosed}
            >
              <p>
                {BASE_STATE.CLOSE.NAME}
                <span className="inline-flex items-center justify-center w-8 h-4 ml-4 text-xs font-semibold text-gray-100 bg-gray-600 rounded-full">
                  -
                </span>
              </p>
            </Sidebar.Item>
            <Sidebar.Collapse
              open={true}
              icon={IoAlbumsSharp}
              label="地域"
            >
            </Sidebar.Collapse>
          </Sidebar.ItemGroup>
        </Sidebar.Items>
      </Sidebar>
    </div>
  )
}