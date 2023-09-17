import 'src/app/globals.css'
import { HiMenuAlt2 } from 'react-icons/hi'

{/*
  機能名:モバイル時のハンバガーメニューボタン
*/}
export default function HamburgerMenuButton({ handleMenuOpen }) {
  // console.log(props)
  return (
    <div>
      <HiMenuAlt2 size={45}
        className="inline-flex items-center border p-2 mt-4 ml-3 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
        onClick={() => handleMenuOpen()}
      />
    </div>
  )
}
