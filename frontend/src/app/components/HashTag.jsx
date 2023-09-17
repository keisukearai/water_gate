{/*
  機能名:ハッシュタグ
*/}
export function HashTag(props) {
  return (
    <div className="pt-1 my-4 md:mb-2">
      <span className={`inline-flex items-center justify-center text-base w-15 h-8 mr-5 p-3 text-stone-900 bg-stone-200 rounded-md border border-stone-300
            ${props.menuSelectedName === '' ? "hidden" : ""}`}>
        #{props.menuSelectedName}
      </span>
      <span className={`inline-flex items-center justify-center text-base w-15 h-8 mr-5 p-3 text-stone-900 bg-stone-200 rounded-md border border-stone-300
          ${props.areaSelectedName === '' ? "hidden" : ""}`}>
        #{(props.areaSelectedName !== '') ? props.areaSelectedName : ''}
      </span>
    </div>
  )
}
