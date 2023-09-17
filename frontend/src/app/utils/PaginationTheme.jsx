{/*
  機能名:ページネーションテーマ
  pages.selector.baseのw-9で1マスのサイズを変更
*/}
export const paginationTheme = {
  pages: {
    base: 'xs:mt-0 mt-2 inline-flex items-center -space-x-px',
    showIcon: 'inline-flex',
    previous: {
      base: 'ml-0 rounded-l-lg border border-gray-300 bg-white py-2 px-3 leading-tight text-gray-500 enabled:hover:bg-gray-100 enabled:hover:text-gray-700 dark:border-gray-700 dark:bg-gray-800 dark:text-gray-400 enabled:dark:hover:bg-gray-700 enabled:dark:hover:text-white',
      icon: 'h-5 w-5',
    },
    next: {
      base: 'rounded-r-lg border border-gray-300 bg-white py-2 px-3 leading-tight text-gray-500 enabled:hover:bg-gray-100 enabled:hover:text-gray-700 dark:border-gray-700 dark:bg-gray-800 dark:text-gray-400 enabled:dark:hover:bg-gray-700 enabled:dark:hover:text-white',
      icon: 'h-5 w-5',
    },
    selector: {
      base: 'w-9 border border-gray-300 bg-white py-2 leading-tight text-gray-500 enabled:hover:bg-gray-100 enabled:hover:text-gray-700 dark:border-gray-700 dark:bg-gray-800 dark:text-gray-400 enabled:dark:hover:bg-gray-700 enabled:dark:hover:text-white',
      active:
        'bg-zinc-200 text-zinc-600 hover:bg-zinc-100 hover:text-zinc-700 dark:border-gray-700 dark:bg-gray-700 dark:text-white',
      disabled: 'opacity-50 cursor-normal',
    },
  },
};