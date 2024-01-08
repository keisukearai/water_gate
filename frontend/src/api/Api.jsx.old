import useSWR from 'swr'
import { fetcher } from 'src/app/utils/Fetcher'

{/*
  機能名:API関数群
*/}
{/* APIホスト名 */}
const api_host_name = process.env.NEXT_PUBLIC_API_HOST_NAME
const api_dummy_host_name = process.env.NEXT_PUBLIC_API_DUMMY_HOST_NAME

{/* 一覧の表示件数 */}
const limit = process.env.NEXT_PUBLIC_LIST_MAX_ROW

{/* 一覧情報取得 */}
export function useApiContenList(currentPage) {

  // APIURL
  const url = `${api_dummy_host_name}/products?limit=${limit}&skip=${(currentPage - 1) * limit}`

  {/* API実行 */}
  const { data, error, isValidating } = useSWR(url, fetcher)

  {/* 結果返却 */}
  return {
    data: data,
    error: error,
    isValidating: isValidating
  }
}

{/* 詳細情報取得 */}
export function useApiContenDatail(slug) {

  // APIURL
  // const url = `${api_dummy_host_name}/products/${slug}`
  const url = `${api_host_name}/watergatedetai?id=${slug}`

  {/* API実行 */}
  const { data, error, isValidating } = useSWR(url, fetcher)

  {/* 結果返却 */}
  return {
    data: data,
    error: error,
    isValidating: isValidating
  }
}

{/* 地域情報取得 */}
export function useAreaInfo() {

  // APIURL
  const url = `${api_host_name}/area`

  {/* API実行 */}
  const { data, error, isValidating } = useSWR(url, fetcher)
  // console.log(`data=${data}, error=${error}, isValidating=${isValidating}`)
  // console.log(data)

  {/* 結果返却 */}
  return {
    data: data,
    error: error,
    isValidating: isValidating
  }
}