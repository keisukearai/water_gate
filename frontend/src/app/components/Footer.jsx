import 'src/app/globals.css'
import Link from 'next/link'

{/*
  機能名:フッター
*/}
export default function Footer() {
  return (
    <footer className="z-20 fixed bottom-0 left-0 w-full">
      {/* <!--Copyright section--> */}
      <div className="w-full bg-neutral-300 p-4 text-center">
        © 2023 Copyright{' '}
        <Link
          className="text-neutral-800"
          href={process.env.NEXT_PUBLIC_COPY_RIGHT_URL}
          target="_blank"
        >
          {process.env.NEXT_PUBLIC_COPY_RIGHT_NAME}
        </Link>
      </div>
    </footer>
  )
}
