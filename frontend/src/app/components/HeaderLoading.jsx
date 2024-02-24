import 'src/app/globals.css'

{/*
  機能名:ヘッダーローディング
*/}
export default function HeaderLoading(props) {
  return (
    <header>
      <div className="z-20 w-full relative">
        <div className="fixed top-0 left-0 flex h-20 w-full text-header-text-color border-b-2 border-neutral-300 bg-gradient-to-r from-cyan-800 to-cyan-600">
          <div className="text-header-text-color text-center flex justify-center items-center px-10 text-2xl font-semibold font-mono">
          </div>
        </div>
      </div>
    </header>
  )
}
