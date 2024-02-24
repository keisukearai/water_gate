import 'src/app/globals.css'

import Link from 'next/link'
import FooterLoading from "src/app/components/FooterLoading"
import { useApiFooterInfo } from "src/api/Api"

{/*
  機能名:フッター
*/}
export default function Footer() {

  {/* API実行 */ }
  const { data, error, isValidating } = useApiFooterInfo()
  {/* ローディング処理 */ }
  if (isValidating) return <FooterLoading />

  return (
    <footer className="z-20 fixed bottom-0 left-0 w-full">
      {/* <!--Copyright section--> */}
      <div className="w-full bg-footer-color p-4 text-center text-footer-text-color">
        © 2023 Copyright{' '}
        <Link
          className="text-footer-text-color"
          href={data.copy_right_url}
          target="_blank"
        >
          {data.copy_right}
        </Link>
      </div>
    </footer>
  )
}
