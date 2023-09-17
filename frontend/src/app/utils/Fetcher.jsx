{/*
  機能名:fetcher
*/}
export const fetcher = (url) => fetch(url).then(res => res.json())