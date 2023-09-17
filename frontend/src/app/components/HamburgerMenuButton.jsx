import 'src/app/globals.css'
import { HiMenuAlt2 } from 'react-icons/hi'

{/*
  機能名:モバイル時のハンバガーメニューボタン
*/}
export default function HamburgerMenuButton({ handleMenuOpen }) {
  // console.log(props)
  return (
    <div>
      <HiMenuAlt2 size={40}
        className="inline-flex items-center border p-1.5 mt-5 ml-3 text-sm text-sky-100 rounded-lg sm:hidden
                  hover:bg-sky-700 focus:outline-none focus:ring-2 focus:ring-sky-700 dark:text-sky-400 dark:hover:bg-sky-700 dark:focus:ring-sky-600"
        onClick={() => handleMenuOpen()}
      />
    </div>
  )
}
