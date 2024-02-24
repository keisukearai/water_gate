import AreaMap from "src/app/components/AreaMap"

export const metadata = {
  title: '地域マップ',
  description: 'ゲートが設置されている地域のマップ情報',
}

{/*
  画面名:地域マップ
*/}
export default function map() {

  return (
    <AreaMap />
  )
}
