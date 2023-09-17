{/*
  機能名:内部エラー500
*/}
export default function Error() {
  return (
    <main className="flex justify-center md:pt-24 sm:ml-64">
      <div className="bg-red-100 border border-red-400 text-red-700 py-10 px-5 md:px-24 rounded" role="alert">
        <strong className="font-bold">内部エラー500</strong><br />
        <span className="block sm:inline">管理者に問い合わせて下さい。</span>
      </div>
    </main>
  )
}