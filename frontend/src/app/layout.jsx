'use client'
import 'src/app/globals.css'
import { Inter } from 'next/font/google'
import { useCallback, useState } from 'react'
import SidebarMenu from 'src/app/components/SidebarMenu'
import Footer from 'src/app/components/Footer'
import Header from 'src/app/components/Header'

const inter = Inter({ subsets: ['latin'] })

{/*
  全システムのルートレイアウト
*/}
export default function RootLayout({ children }) {

  {/* メニュー開閉用の状態 */}
  const [menuOpen, setMenuOpen] = useState(true)

  {/* メニュー開閉用のハンドラ */}
  const handleMenuOpen = useCallback(() => {
    return setMenuOpen(!menuOpen)
  }, [menuOpen])

  // console.log("layout:" + menuOpen)

  return (
    <html lang="ja">
      <body className={inter.className} suppressHydrationWarning={true}>
        {/* ヘッダー */}
        <Header handleMenuOpen={handleMenuOpen} menuOpen={menuOpen} />
        {/* サイドバー */}
        <SidebarMenu menuOpen={menuOpen} />
        {/* 子コンポーネント */}
        {children}
        {/* フッター */}
        <Footer />
      </body>
    </html>
  )
}
