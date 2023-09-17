import 'src/app/globals.css'
import HamburgerMenuButton from 'src/app/components/HamburgerMenuButton'

{/*
  機能名:ヘッダー
*/}
export default function Header(props) {
  return (
    <header>
      <div className="z-20 w-full">
        <div className="fixed top-0 left-0 flex h-20 w-full bg-white border-b-2 border-neutral-100">
          {/* ハンバーガーメニューボタン */}
          <HamburgerMenuButton handleMenuOpen={props.handleMenuOpen} />
          <div className="text-neutral-800 text-center flex justify-center items-center px-10 text-lg">
            {process.env.NEXT_PUBLIC_SITE_NAME}
          </div>
        </div>
      </div>
    </header>
  )
}
