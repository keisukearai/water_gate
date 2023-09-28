import 'src/app/globals.css'
import HamburgerMenuButton from 'src/app/components/HamburgerMenuButton'

{/*
  機能名:ヘッダー
*/}
export default function Header(props) {
  return (
    <header>
      <div className="z-20 w-full relative">
        <div className="fixed top-0 left-0 flex h-20 w-full text-header-text-color border-b-2 border-neutral-300 bg-gradient-to-r from-sky-700 to-sky-500">
          {/* ハンバーガーメニューボタン */}
          <HamburgerMenuButton handleMenuOpen={props.handleMenuOpen} />
          <div className="text-header-text-color text-center flex justify-center items-center px-10 text-2xl font-semibold font-mono">
            {process.env.NEXT_PUBLIC_SITE_NAME}
          </div>
        </div>
      </div>
    </header>
  )
}
