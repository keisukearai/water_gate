{/*
  機能名:ハッシュタグ
*/}
export function HashTag(props) {
  // console.log(props.selectedName)
  return (
    <div className="pt-1 my-4 md:mb-2 text-start">
      <span className="inline-flex items-center justify-center text-base w-15 h-8 mr-5 p-3 bg-gray-100 text-gray-800 rounded-md border border-stone-300">
        #{props.selectedName}
      </span>
    </div>
  )
}
