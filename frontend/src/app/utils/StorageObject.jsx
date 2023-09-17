{/*
  機能名:ストーレージオブジェクト
*/}

{/* ページ表示情報 */}
export const PageObject = {
  currentPage: 0,
  state: null,
  stateName: null,
  area: null,
  areaName: null,
}

{/* ローカルストレージ取得時の判定 */}
export const isTypeofWindow = () => {
  return (typeof window !== 'undefined') ? true : false
}