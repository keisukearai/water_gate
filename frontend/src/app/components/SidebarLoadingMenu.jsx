'use client'
import 'src/app/globals.css'
import { Sidebar } from 'flowbite-react'
import { IoHomeSharp, IoLockClosed, IoLockOpen, IoMap } from "react-icons/io5"
import { IconContext } from 'react-icons'
import { BASE_STATE } from 'src/app/utils/Constants'
import { SideBarTheme } from "src/app/utils/SideBarTheme"

{/*
  機能名:ローディング中のメニュー
*/}
export default function LoadingMenu() {
  return (
    <div className="invisible md:visible">
      <Sidebar className="fixed top-20 left-0 z-10 w-64 h-screen"
        theme={SideBarTheme}
      >
        <Sidebar.Items>
          <Sidebar.ItemGroup>
            <IconContext.Provider value={{ className: "text-white" }}>
              <Sidebar.Item
                icon={IoHomeSharp}
                className="hover:bg-gray-800 hover:text-white text-white"
              >
                <p>
                  {BASE_STATE.ALL.NAME}
                  <span className="inline-flex items-center justify-center w-8 h-4 ml-6 text-xs font-semibold text-slate-700 bg-slate-300 rounded-full">
                    -
                  </span>
                </p>
              </Sidebar.Item>
            </IconContext.Provider>
            <IconContext.Provider value={{ className: "text-white" }}>
              <Sidebar.Item
                icon={IoLockOpen}
                className="hover:bg-gray-800 hover:text-white text-white"
              >
                <p>
                  {BASE_STATE.OPEN.NAME}
                  <span className="inline-flex items-center justify-center w-8 h-4 ml-4 text-xs font-semibold bg-pink-100 text-pink-800 rounded-full">
                    -
                  </span>
                </p>
              </Sidebar.Item>
            </IconContext.Provider>
            <IconContext.Provider value={{ className: "text-white" }}>
              <Sidebar.Item
                icon={IoLockClosed}
                className="hover:bg-gray-800 hover:text-white text-white"
              >
                <p>
                  {BASE_STATE.CLOSE.NAME}
                  <span className="inline-flex items-center justify-center w-8 h-4 ml-4 text-xs font-semibold text-gray-100 bg-gray-600 rounded-full">
                    -
                  </span>
                </p>
              </Sidebar.Item>
            </IconContext.Provider>
            <IconContext.Provider value={{ className: "text-white group-hover:text-white" }}>
              <Sidebar.Collapse
                open={true}
                icon={IoMap}
                label="マップ"
                className="hover:bg-gray-800 text-white"
              >
              </Sidebar.Collapse>
            </IconContext.Provider>
          </Sidebar.ItemGroup>
        </Sidebar.Items>
      </Sidebar>
    </div>
  )
}