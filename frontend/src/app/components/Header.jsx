import 'src/app/globals.css'

import HeaderLoading from "src/app/components/HeaderLoading"
import HamburgerMenuButton from 'src/app/components/HamburgerMenuButton'
import { useApiHeaderInfo } from "src/api/Api"

{/*
  機能名:ヘッダー
*/}
export default function Header(props) {
  // console.log("header:" + props.menuOpen)

  {/* API実行 */ }
  const { data, error, isValidating } = useApiHeaderInfo()
  {/* ローディング処理 */ }
  if (isValidating) return <HeaderLoading />

  return (
    <header>
      <div className="z-20 w-full relative">
        <div className="fixed top-0 left-0 flex h-20 w-full text-header-text-color border-b-2 border-neutral-300 bg-gradient-to-r from-cyan-800 to-cyan-600">
          {/* ハンバーガーメニューボタン */}
          <HamburgerMenuButton {...props} />
          <div className="text-header-text-color text-center flex justify-center items-center px-4 lg:px-14 text-2xl font-semibold font-mono">
            {data.header_title}
          </div>
        </div>
      </div>
    </header>
  )
}
