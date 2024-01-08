import 'src/app/globals.css'
import { HiMenuAlt2, HiOutlineX } from 'react-icons/hi'

{/*
  機能名:モバイル時のハンバガーメニューボタン
*/}
export default function HamburgerMenuButton(props) {
  // console.log(props.menuOpen)
  return (
    <div>
      {props.menuOpen ? (
        <HiMenuAlt2 size={40}
          className="inline-flex items-center border p-1.5 mt-5 ml-3 text-sm text-neutral-100 rounded-lg sm:hidden bg-gray-600
                    focus:outline-none focus:ring-2 focus:ring-neutral-700"
          onClick={() => props.handleMenuOpen()}
        />
      ) : (
        <HiOutlineX size={40}
          className="inline-flex items-center border p-1.5 mt-5 ml-3 text-sm text-neutral-100 rounded-lg sm:hidden bg-gray-600
                    focus:outline-none focus:ring-2 focus:ring-neutral-700"
          onClick={() => props.handleMenuOpen()}
        />
      )}
    </div>
  )
}
